import streamlit as st

import general_settings

import requests
from PIL import Image
import io
import base64

# --- REQUEST SETTINGS ---
URL = "https://api.ocr-layoutparser.lafsolutions.com.br/ocr/"
# URL = "http://127.0.0.1:8000/ocr/"

# --- GENERAL SETTINGS ---
NAME = "Optical Character Recognition (OCR) - Layout Parser"
DESCRIPTION = """
Optical Character Recognition (OCR) is a technology that converts printed or handwritten text from images into machine-readable text.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

st.title(NAME)
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