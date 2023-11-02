# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 16:59:00 2023

@author: Pawan
"""

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
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}



PROJECTS = {
    "🏆 Hotel Management System - Web app with MYSQL database": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
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
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL,
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL, Firebase
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

    
    
    
# --- WORK HISTORY ---
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

    