from pathlib import Path

import streamlit as st

import requests
from PIL import Image, ImageEnhance
import io
import base64
from streamlit_cropperjs import st_cropperjs

def compress_image(uploaded_file, max_size_kb=200):
    """
    Compress an image to a maximum size in kilobytes by resizing.
    """
    # Open the uploaded image
    image = Image.open(uploaded_file)
    img_format = image.format.lower()

    # Convert the image to grayscale (black and white)
    image = image.convert('L')

    # Convert the maximum size to bytes
    max_size_bytes = max_size_kb * 1024

    # Get the current image size in bytes
    original_image_bytes = io.BytesIO()
    image.save(original_image_bytes, optimize=True, format=img_format)
    original_image_size_bytes = original_image_bytes.tell()

    # Calculate the scale factor to fit within the desired size
    scale_factor = (max_size_bytes / original_image_size_bytes) ** 0.5

    # Resize the image with the calculated scale factor
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Create an in-memory buffer to store the resized image
    compressed_image_bytes = io.BytesIO()

    # Save the resized image to the buffer
    resized_image.save(compressed_image_bytes, optimize=True, format=img_format)

    # Reset the buffer and return the compressed image bytes
    compressed_image_bytes.seek(0)
    return compressed_image_bytes


# --- REQUEST SETTINGS ---
URL = "https://api.ocr-pytesseract.lafsolutions.com.br/ocr/"
# URL = "http://127.0.0.1:8000/ocr/"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "LAF Solutions | Computer Vision"
PAGE_ICON = "favicon.ico"
NAME = "Computer Vision"
DESCRIPTION = """
Unveiling the unseen through pixels and algorithms, our computer vision technology redefines how we perceive and interact with the visual world.
"""
OCR_DESCRIPTION = """
Optical Character Recognition (OCR) is a technology that converts printed or handwritten text from images into machine-readable text. It plays a crucial role in digitizing documents, automating data entry, and enhancing accessibility for individuals with visual impairments. Advancements in deep learning and AI continue to improve OCR's accuracy and expand its applications in various industries.
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
current_dir = current_dir.parent # Since we added the file into /pages
css_file = current_dir / "styles" / "main.css"

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title(NAME)
st.write(DESCRIPTION)

st.header("Optical Character Recognition (OCR)")
st.write(OCR_DESCRIPTION)

# Add a file uploader widget
uploaded_file = st.file_uploader("Upload a picture", key="uploaded_pic", type=["png", "jpg"])
# Add a select-from-options widget
selected_language = st.selectbox("Select a language", ["eng", "por"])
if uploaded_file:
    pic = uploaded_file.read()
    cropped_pic = st_cropperjs(pic=pic, btn_text="Detect!", key="foo")
    if cropped_pic:
        st.image(cropped_pic, output_format="PNG")
        file_data = cropped_pic
        with st.spinner("Loading ocr..."):
            request_params = {"output_type": "string", "lang": selected_language, "config": "--psm 6", "nice": 0, "timeout": 0}

            files = []
            filename = uploaded_file.name
            files.append(('files', (filename, file_data)))
            
            request = requests.post(url=URL, params=request_params, files=files) 
            data_request = request.json()
            ocr = data_request['results'][filename]['ocr']

            st.success(f"{ocr}")

            final_image_base64 = data_request['results'][filename]['final_image_base64']
            final_image_base64 = Image.open(io.BytesIO(base64.b64decode(final_image_base64)))
            st.image(final_image_base64)

with st.sidebar:
    pass
#st.sidebar.success("Select a page above.")