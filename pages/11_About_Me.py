import streamlit as st
from PIL import Image

import general_settings

# --- GENERAL SETTINGS ---
NAME = "Luiz Augusto Fidalgo"
DESCRIPTION = """
Bachelor of Electrical Engineering & AI Consultant, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "luiz.fidalgo@hotmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/luiz-augusto-fidalgo/",
    "GitHub": "https://github.com/lafidalgo/",
}
PROJECTS = {
    "🏆 OCR Pytesseract - Extract text from images": "https://www.lafsolutions.com.br/OCR_Pytesseract",
    "🏆 OCR Layout Parser - Extract text and layout from images": "https://www.lafsolutions.com.br/OCR_Layout_Parser",
    "🏆 Local Whisper AI - Extract text from audio": "https://www.lafsolutions.com.br/Whisper_AI",
}

root_dir = general_settings.get_root_dir()
general_settings.config_page()
general_settings.load_css(root_dir)

# --- PATH SETTINGS ---
resume_file = root_dir / "assets" / "CV.pdf"
profile_pic = root_dir / "assets" / "profile-pic.png"


# --- LOAD PDF & PROFIL PIC ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- ✔️ University Exchange: **University of Rome Tor Vergata, Italy** (Feb. 2023 - Aug.2023)
- ✔️ Bachelor of Electrical Engineering: **University of Brasília (UnB), Brazil** (2018 - 2023)
- ✔️ Final Thesis:  Inventory monitoring through weight variation using low power consumption techniques and wireless communication
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C, C++, ESP-IDF, Code Composer, Arduino IDE
- 🛠️ Hardware Development: Circuits Design, PCB Design, Soldering, 3D Printing
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**AI Consultant | SnowFox AI**")
st.write("09/2023 - Present")
st.write(
    """
- ► Developed a machine learning application that performs Visual Document Understanding (VDU) to extract complex information from contracts and balance sheets
- ► Had experience with the full cycle of a machine learning project, from data collection to model deployment
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Hardware Development Intern | Orion Telecommunications**")
st.write("03/2021 - 12/2022")
st.write(
    """
- ► Worked with hardware and firmware development at the spin-off BeSX.
- ► Participated in the development of 5 sensor prototypes.
- ► Participated in the production, testing and installation of over 200 units of one of the developed sensors.
- ► Awarded as the company's Outstanding Intern of 2021.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Academic Researcher | CNPq**")
st.write("07/2020 - 01/2023")
st.write(
    """
- ► Responsible for the development of an assistive human-computer communication methodology for typing.
- ► Article published in the scientific journal [IJCAT](https://www.inderscience.com/info/inarticle.php?artid=130290).
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**CEO | ENETEC - Junior Consulting**")
st.write("01/2020 - 12/2020")
st.write(
    """
- ► Responsible for managing the junior enterprise's internal strategy and conducting its adaptation during the pandemic.
- ► Leadership of 39 members throughout the year.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


with st.sidebar:
    pass