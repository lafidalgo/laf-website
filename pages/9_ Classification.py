import streamlit as st

import general_settings

# --- GENERAL SETTINGS ---
NAME = "Classification"
DESCRIPTION = """
From chaos to clarity, our classification systems discern patterns in data, illuminating insights that drive informed decisions.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

st.title(NAME)
st.write(DESCRIPTION)

with st.sidebar:
    pass