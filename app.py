from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV K Pawan Bangera"
PAGE_ICON = ":wave:"
NAME = "K Pawan Bangera"
DESCRIPTION = """
Software Engineer
"""
EMAIL = "pawanbangera4231@gmail.com"
SOCIAL_MEDIA = {
    "Email": "pawanbangera142@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/k-pawan-bangera-3865441ba/",
    "GitHub": "https://github.com/PawanBangera1",
    "Twitter": "https://twitter.com",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

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





# ---QUALIFICATIONS ---
st.write('\n')
st.subheader("Qulifications")
st.write("---")

st.write('\n')
st.write("✔️", "**Yenepoya Institute Of Technology mangalore**")
st.write("""
          - Year : 2020-2024
          - Course : Bachelor Of Computer Science And Engineering
          - CGPA : 8.4/10""")




st.write('\n')
st.write("✔️", "**Gunashree Pre-University Siddakatte mangalore**")
st.write("""
          - Year : 2018-2020
          - Course : PCMB
          """)





st.write('\n')
st.write("✔️", "**Gunashree Vidyalaya Siddakatte mangalore**")
st.write("""
          - Year : 2018
          - Course : SSLC
          """)
st.write('\n')








# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL,
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL, Firebase
"""
)




# --- Internship ---
st.write('\n')
st.subheader("Internship")
st.write("---")

# --- JOB 1
st.markdown("🚧 [**Zephyr Technologies And Solutions PVT LTD**](https://zephyrtechnologies.co/)")
st.write("**Data Science Intern | August 2023 – September 2023**")
st.write(
    """
- ►I've collaborated with a team of data scientists to extract valuable insights from large datasets, enhancing decision 
making. Proficient in Python and pandas, I've cleaned, preprocessed, and transformed raw data for analysis.
- ► Leveraging tools like Matplotlib and Seaborn, I've effectively conveyed findings to both technical and non-technical 
stakeholders through data visualizations. This targeted approach highlights my contributions and expertise in data 
analysis and communication.
"""
)



    
  
    
  
    
  
    
    
# --- project ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- project 1 ----
st.write("🏆", "**Hotel Management System**")
st.write("08/2022 - 10/2022")
st.write(
    """
- ► Designed and implemented hotel management website as part of a 3-person team, utilizing HTML, CSS, Java, SQL.
"""
)

# --- project 2
st.write('\n')
st.write("🏆", "**Intestinal Disease Prediction Using ML**")
st.write("08/2023 – 10/2023")
st.write(
    """
- ► Designed and implemented a cutting-edge project focused on Intestinal Disease Prediction utilizing Machine 
Learning(ML), Image Processing techniques, TensorFlow, and Streamlit for an intuitive user interface. Achieved an 
impressive accuracy of 90%.
"""
)

# --- project 3
st.write('\n')
st.write("🏆", "**Healthcare Android Application System**")
st.write("04/2023 - 06/2023")
st.write(
    """
- ►Designed and implemented Healthcare Android Application as part of a 2-person team, utilizing Java, XML.

"""
)

# --- project 4
st.write('\n')
st.write("🏆", "**Multiple Disease Prediction Using ML**")
st.write("09/2023 - Present")
st.write(
    """
- ►Designed and implemented a cutting-edge project focused on multiple Disease Prediction utilizing Machine 
Learning(ML) and Streamlit and showcasing expertise in feature engineering and classification. Ongoing project.
"""
)



st.write('\n')
st.subheader("Certifications")
st.write("---")

# --- JOB 1
st.markdown("🚧 [**Python [ Guvi]**](https://youtu.be/Sb0A9i6d320)")
st.markdown("🚧 [**Spoken Tutorial By IIT Bombay [C, C++, Python]**](https://youtu.be/Sb0A9i6d320)")
st.markdown("🚧 [**HTML and CSS [ Priple]**](https://youtu.be/Sb0A9i6d320)")
st.markdown("🚧 [**Google Cloud Big Data and ML and Fundamentals**](https://youtu.be/Sb0A9i6d320)")
st.markdown("🚧 [**Machine Learning With Python [Cognitive Class]**](https://youtu.be/Sb0A9i6d320)")

