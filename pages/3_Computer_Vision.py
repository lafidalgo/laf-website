from pathlib import Path

import streamlit as st

import requests

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
    with st.spinner("Loading ocr..."):
        request_params = {"output_type": "string", "lang": selected_language, "config": "--psm 6", "nice": 0, "timeout": 0}

        files = []
        filename = uploaded_file.name
        file_data = uploaded_file.read()
        files.append(('files', (filename, file_data)))

        request = requests.post(url=URL, params=request_params, files=files) 
        data_request = request.json()
        ocr = data_request['results'][filename]

        st.write(f"{ocr}")

with st.sidebar:
    pass
#st.sidebar.success("Select a page above.")