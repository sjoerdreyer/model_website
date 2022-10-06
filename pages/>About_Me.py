from datetime import date, datetime
import streamlit as st
from PIL import Image
import pandas as pd

from lottie import load_lottiefile
from streamlit_lottie import st_lottie


birthdate = datetime(1995,10,14)
today = datetime.today()
age = today - birthdate
age_in_s = age.total_seconds()
years_old = int(divmod(age_in_s, 31536000)[0])

sjoerd_model_dict = {
    'Firstname' : 'Sjoerd',
    'Lastname' : 'de Wit',
    'Gender' : 'Man',
    'Height (cm)' : 191,
    'Chest (cm)' : 99,
    'Waist (cm)' : 83,
    'Hips (cm)' : 97,
    'Shoe Size (EU)' : '46/47',
    'Age' : years_old,
    'Currently in' : 'Lisboa, PT'
}

st.write('------------')

col1, col2 = st.columns([4,8])
robot_lottie = load_lottiefile('lottie_json_files/hello_robot.json')

with col1:
    st_lottie(robot_lottie)


for key, value in sjoerd_model_dict.items():
    col1.markdown(f"<h6 style='text-align: center; color: #2A79CC;'>{key} : {value}</h6>", unsafe_allow_html=True)

col1.markdown(
    """<a style='display: block; text-align: center;' href="https://instagram.com/sjoerd_rdwve/">Instagram</a>
    """,
    unsafe_allow_html=True,
)


#Bike on beach
wallaroo_bike = Image.open('raw_data/wallaroo5.jpeg')
col2.image(wallaroo_bike)


st.write('------------')

col4,col5,col6 = st.columns(3)
with col5:
    cam_photos = load_lottiefile('lottie_json_files/camera_photos.json')
    st_lottie(cam_photos)

st.markdown("<h2 style='text-align: center; color: #2A79CC;'>Am I a fit for YOUR brand?</h2>", unsafe_allow_html=True)


st.markdown("<h5 style='text-align: center; color: #2A79CC;'>Contact me at:</h5>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: #2A79CC;'>&#x1F4E7 sjoerdreyer@gmail.com &#x1F4E7</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #2A79CC;'>&#x1F4F2 +31653406466 &#x1F4F2</h5>", unsafe_allow_html=True)

st.write('------------')
