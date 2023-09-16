import streamlit as st

import general_settings

# --- GENERAL SETTINGS ---
NAME = "Predictions"
DESCRIPTION = """
Unlocking the potential of data, our predictive solutions empower informed decision-making by foreseeing future outcomes with analytical precision.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

st.title(NAME)
st.write(DESCRIPTION)

with st.sidebar:
    pass