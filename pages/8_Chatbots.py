from pathlib import Path

import streamlit as st

# --- GENERAL SETTINGS ---
PAGE_TITLE = "LAF Solutions | Chatbots"
PAGE_ICON = "favicon.ico"
NAME = "Chatbots"
DESCRIPTION = """
Conversing at the intersection of technology and human interaction, our chatbots seamlessly connect and engage, enhancing user experiences like never before.
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

with st.sidebar:
    pass
#st.sidebar.success("Select a page above.")