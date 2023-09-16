from pathlib import Path

import streamlit as st

import requests
from PIL import Image, ImageEnhance
import io
import base64

# --- REQUEST SETTINGS ---
URL = "https://api.ocr-layoutparser.lafsolutions.com.br/ocr/"
# URL = "http://127.0.0.1:8000/ocr/"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "LAF Solutions | Computer Vision"
PAGE_ICON = "favicon.ico"
NAME = "Computer Vision"
DESCRIPTION = """
Optical Character Recognition (OCR) is a technology that converts printed or handwritten text from images into machine-readable text.
"""

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
current_dir = current_dir.parent # Since we added the file into /pages
css_file = current_dir / "styles" / "main.css"

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.title("Optical Character Recognition (OCR)")
st.write(DESCRIPTION)

# Add a file uploader widget
uploaded_file = st.file_uploader("Upload a picture", key="uploaded_pic", type=["png", "jpg"])
# Add a select-from-options widget
selected_language = st.selectbox("Select a language", ["eng", "por"])
if uploaded_file:
    file_data = uploaded_file.read()

    st.image(file_data, output_format="PNG")

    with st.spinner("Loading ocr..."):
        request_params = {"lang": selected_language}

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