from pathlib import Path
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


# File Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/'styles'/'main.css'
resume_file = current_dir/'assets'/'KremerResume2023.pdf'
logo_file = current_dir/'assets'/'Logo-removebg.png'

#Settings
PAGE_TITLE = 'Digital Resume | Noah Kremer'
NAME = 'Noah Kremer'
DESCRIPTION = '''
GIS Specialist at Schneider Geospatial
'''
EMAIL = 'noahkremer20@gmail.com'
LINKS = {
    'LinkedIn':'https://www.linkedin.com/in/noah-kremer-1a13851b6/',
    'GitHub':'https://www.github.com/nkremer20'
}
UNI_DESC = [
    'Graduated with a 3.82 cumulative GPA. On the Dean’s List every semester. Graduated Cum Laude.',
    'Taken courses on Geographic Information Science/Systems, GPS, Remote Sensing, Unmanned Aerial Systems, Python Programming for GIS applications and data analysis, and Web Mapping.'
]
SKILLS = [
    "ESRI’s ArcGIS Software (ArcMap, ArcGIS Pro, ArcGIS Online)",
	'ArcGIS Server and ArcGIS Online Organization Deployment and Administration',
	'ArcGIS Online web app creation (Dashboards, Web App Builder, Experience Builder, Field Maps)',
	'Python programming for GIS automation and data analysis',
	'Creating Model Builder workflows to automate GIS tasks',
	'Some SQL experience',
	'Microsoft Office (Excel, Word, PowerPoint)'
]
PROJECTS = [
    'Using Python to run a viewshed analysis over 100’s of points in a valley in Afghanistan.',
	'Created a campus accessibility web map of the University of Northern Iowa’s campus.',
	'Using machine learning to predict the outcome of presidential elections.',
	'Creation of dashboards and web apps to provide easy editing and data visualization capabilities for clients',
	'Scripts to pull data from an ArcGIS Online Hosted Feature Service and create reports of street sign inventories.',
	'Creating automated map book scripts for clients'
]
EMPLOYMENT = {
    'GeoTREE':[
        'Cedar Falls, IA', 
        'GIS Research Assistant', 
        'June 2019 – December 2020',
        'Responsibilities included using primarily ArcGIS Pro to complete GIS projects/analysis for clients. Projects have included digitizing features for a county in eastern Iowa, collecting spatial data using RTK-GPS, and managing databases.'
        ],
    'City of Waukee': [
        'Waukee, IA',
        'GIS Intern',
        'June 2020 – August 2020',
        'Responsibilities included primarily using ArcGIS Pro to complete GIS projects/analysis, collecting spatial and topographic data using RTK-GPS, using legal descriptions to digitize easements, use construction drawings to map features such as fiber optic lines, and updating databases.'
    ],
    'Schneider Geospatial':[
        'Ankeny, IA',
        'GIS Specialist',
        'April 2021 - Now',
        'Responsibilities include remote and on-site consulting for county and city government clients on best use cases of GIS for their organizations. Primary projects include GIS software download/maintenance, ArcGIS Online Organization set-up and administration, creation of web apps in ArcGIS Online (Dashboards, Web App Builder, Experience Builder, Field Maps), creating and administrating GIS databases (server and file geodatabases), maintaining and submitting GIS data to State and Federal Government Organizations (NG911, Agricultural Land Valuation, Redistricting), automating repetitive GIS tasks using Python and Modelbuilder, and creating static maps and web maps.'
    ]
}

st.set_page_config(page_title=PAGE_TITLE)

#Styling and Opening files
with open(css_file) as f:
    st.markdown("<style>{}</stlye>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDF = pdf_file.read()
logo = Image.open(logo_file)

#Resume Header
col1, col2, col3 = st.columns([1.5,2,1], gap='medium')
with col1:
    st.write('#')
    st.image(logo)
with col2:
    #st.write('#')
    st.title(NAME)
    st.write("**GIS Specialist at Schneider Geospatial**")
    st.write(f'Email: {EMAIL}')
    st.download_button(
        label="Click Here to Download Resume",
        data = PDF,
        file_name = resume_file.name,
        mime = "application/octet-stream"
    )
with col3:
    st.write('#')
    st.write('#')
    st.write('#')
    st.markdown("**Links**")
    for index, (platform, link) in enumerate(LINKS.items()):
        st.write(f"[{platform}]({link})")

st.write("___")

#Education
st.subheader("Education")
st.write('**University of Northern Iowa**, Bachelor of Science in GIS with an emphasis on Unmanned Aerial Systems')
for i in range(len(UNI_DESC)):
    st.write(f'►  {UNI_DESC[i]}')
st.write("___")

#Employment
st.subheader("Employment")
for job, info in EMPLOYMENT.items():
    st.write(f'**{job}**, {info[0]}')
    st.write(f'_{info[1]}_')
    st.write(f'Employment Date: {info[2]}')
    st.write(info[3])
    st.write('#')
st.write("___")

#Skills
st.subheader("Skills")
for i in range(len(SKILLS)):
    st.write(f'✔️  {SKILLS[i]}')
st.write("___")

#Projects
st.subheader("Projects")
for i in range(len(PROJECTS)):
    st.write(f'✔️  {PROJECTS[i]}')