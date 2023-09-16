import streamlit as st
from st_audiorec import st_audiorec

import general_settings

import requests

# --- REQUEST SETTINGS ---
URL = "https://api.ocr-pytesseract.lafsolutions.com.br/ocr/"

# --- GENERAL SETTINGS ---
NAME = "Audio Transcription"
DESCRIPTION = """
Empowering language with intelligence, our NLP solutions bridge the gap between humans and machines, enabling seamless communication and understanding.
"""
AUDIO_TRANSCRIPT_DESCRIPTION = """
Audio transcription is the process of converting spoken language or audio content into written text. It involves listening to the audio and transcribing it verbatim, capturing spoken words, and sometimes including contextual information like speaker identification and timestamps. This text-based representation makes audio content accessible, searchable, and easier to analyze or reference.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

st.title(NAME)
st.write(DESCRIPTION)

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