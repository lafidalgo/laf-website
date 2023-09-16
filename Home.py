import streamlit as st
from PIL import Image

import general_settings

# --- GENERAL SETTINGS ---
NAME = "LAF Solutions"
DESCRIPTION = """
Transforming tomorrow through AI innovation, pioneer intelligent solutions for a smarter world.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

# --- PATH SETTINGS ---
logo_pic = root_dir / "assets" / "Logo e nome lateral - escuro.png"

logo = Image.open(logo_pic)
st.image(logo, width=700)

st.write(DESCRIPTION)

with st.sidebar:
    pass