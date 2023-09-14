from pathlib import Path

import streamlit as st

import requests
from PIL import Image
import io

def calculate_image_size_in_kb(height, width, color_depth):
    # Calculate the size in bytes
    size_in_bytes = height * width * (color_depth // 8)  # Divide by 8 to convert bits to bytes
    # Convert bytes to kilobytes
    size_in_kb = size_in_bytes / 1024.0  # 1 KB = 1024 bytes
    return size_in_kb

def compress_image(image, max_size_kb=200):
    # Open the uploaded image with PIL
    image = Image.open(uploaded_file)
    img_format = image.format.lower()

    # Get original image
    compressed_image = image.resize((int(image.width), int(image.height)))

    color_mode = compressed_image.mode
    # Extract the color depth from the color mode
    if color_mode == "1":
        color_depth = 1  # 1-bit image (binary)
    elif color_mode in ["L", "P"]:
        color_depth = 8  # 8-bit image (grayscale or palettized)
    elif color_mode == "RGB":
        color_depth = 24  # 8 bits per channel (Red, Green, Blue)
    elif color_mode == "RGBA":
        color_depth = 32  # 8 bits per channel (Red, Green, Blue, Alpha)
    elif color_mode == "CMYK":
        color_depth = 32  # 8 bits per channel (Cyan, Magenta, Yellow, Key/Black)
    else:
        # Handle other color modes as needed
        color_depth = None

    size_in_kb = calculate_image_size_in_kb(compressed_image.size[0], compressed_image.size[1], color_depth)
    st.write(f"Image original size is {size_in_kb:.2f} KB")
    while size_in_kb > max_size_kb:
        # Compress the image by resizing it to a smaller size
        compressed_image = compressed_image.resize((int(compressed_image.width * 0.9), int(compressed_image.height * 0.9)))
        size_in_kb = calculate_image_size_in_kb(compressed_image.size[0], compressed_image.size[1], color_depth)

    st.write(f"Image compressed to {size_in_kb:.2f} KB")
    # Convert the compressed image back to bytes
    compressed_image_bytes = io.BytesIO()
    compressed_image.save(compressed_image_bytes, format=img_format)
    
    # Reset the file pointer to the beginning of the buffer
    compressed_image_bytes.seek(0)

    return compressed_image_bytes

# --- REQUEST SETTINGS ---
URL = "https://api.ocr-pytesseract.lafsolutions.com.br/ocr/"

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
uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg"])
# Add a select-from-options widget
selected_language = st.selectbox("Select a language", ["eng", "por"])

if uploaded_file is not None:
    #with st.spinner("Compressing file..."):
        #compressed_image_bytes = compress_image(uploaded_file)

    with st.spinner("Loading ocr..."):
        request_params = {"output_type": "string", "lang": selected_language, "config": "--psm 6", "nice": 0, "timeout": 0}

        files = []
        filename = uploaded_file.name
        #file_data = compressed_image_bytes.read()
        file_data = uploaded_file.read()
        files.append(('files', (filename, file_data)))

        request = requests.post(url=URL, params=request_params, files=files) 
        data_request = request.json()
        ocr = data_request['results'][filename]

        st.success(f"{ocr}")

with st.sidebar:
    pass
#st.sidebar.success("Select a page above.")