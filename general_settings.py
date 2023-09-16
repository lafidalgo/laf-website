import streamlit as st
from pathlib import Path
import os

PAGE_TITLE = "LAF Solutions"
PAGE_ICON = "favicon.ico"

def config_page():
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

def load_css(root_dir):
    css_file = root_dir / "styles" / "main.css"

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def get_root_dir():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir_path = Path(root_dir)
    return root_dir_path