import streamlit as st

import general_settings

# --- GENERAL SETTINGS ---
NAME = "Natural Language Processing (NLP)"
DESCRIPTION = """
Empowering language with intelligence, our NLP solutions bridge the gap between humans and machines, enabling seamless communication and understanding.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

st.title(NAME)
st.write(DESCRIPTION)

with st.sidebar:
    pass