import streamlit as st

import general_settings

# --- GENERAL SETTINGS ---
NAME = "Chatbots"
DESCRIPTION = """
Conversing at the intersection of technology and human interaction, our chatbots seamlessly connect and engage, enhancing user experiences like never before.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

st.title(NAME)
st.write(DESCRIPTION)

with st.sidebar:
    pass