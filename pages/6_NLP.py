from pathlib import Path

import streamlit as st
from st_audiorec import st_audiorec

import requests

# --- REQUEST SETTINGS ---
URL = "https://api.ocr-pytesseract.lafsolutions.com.br/ocr/"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "LAF Solutions | NLP"
PAGE_ICON = "favicon.ico"
NAME = "Natural Language Processing (NLP)"
DESCRIPTION = """
Empowering language with intelligence, our NLP solutions bridge the gap between humans and machines, enabling seamless communication and understanding.
"""
AUDIO_TRANSCRIPT_DESCRIPTION = """
Audio transcription is the process of converting spoken language or audio content into written text. It involves listening to the audio and transcribing it verbatim, capturing spoken words, and sometimes including contextual information like speaker identification and timestamps. This text-based representation makes audio content accessible, searchable, and easier to analyze or reference.
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

st.header("Audio Transcription")
st.write(AUDIO_TRANSCRIPT_DESCRIPTION)

# Add a file uploader widget
uploaded_file = st.file_uploader("Choose a file", type=["wav", "mp3"])

# Add a audio recording widget
st.write("Or record an audio")
wav_audio_data = st_audiorec()

if uploaded_file is not None:
    with st.spinner("Loading ocr..."):
        request_params = {"output_type": "string", "lang": "eng", "config": "--psm 6", "nice": 0, "timeout": 0}

        files = []
        filename = uploaded_file.name
        file_data = uploaded_file.read()
        files.append(('files', (filename, file_data)))

        #request = requests.post(url=URL, params=request_params, files=files) 
        #data_request = request.json()
        #ocr = data_request['results'][filename]

        #st.write(f"{ocr}")
        st.write(files)

if wav_audio_data is not None:
    with st.spinner("Loading ocr..."):
        #st.audio(wav_audio_data, format='audio/wav')
        request_params = {"output_type": "string", "lang": "eng", "config": "--psm 6", "nice": 0, "timeout": 0}

        files = []
        filename = "record.wav"
        file_data = wav_audio_data
        files.append(('files', (filename, file_data)))

        #request = requests.post(url=URL, params=request_params, files=files) 
        #data_request = request.json()
        #ocr = data_request['results'][filename]

        #st.write(f"{ocr}")
        st.write(files)

with st.sidebar:
    pass
#st.sidebar.success("Select a page above.")