import streamlit as st

import general_settings

# --- GENERAL SETTINGS ---
NAME = "Forecasting"
DESCRIPTION = """
Peering into the future with analytical precision, our forecasting solutions empower informed decisions in an uncertain world.
"""

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

st.title(NAME)
st.write(DESCRIPTION)

with st.sidebar:
    pass