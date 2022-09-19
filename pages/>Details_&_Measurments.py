from datetime import date, datetime
import streamlit as st
from PIL import Image
import pandas as pd


birthdate = datetime(1995,10,14)
today = datetime.today()
age = today - birthdate
age_in_s = age.total_seconds()
years_old = int(divmod(age_in_s, 31536000)[0])

sjoerd_model_dict = {
    'Gender' : 'Man',
    'Firstname' : 'Sjoerd',
    'Lastname' : 'de Wit',
    'Height (cm)' : 191,
    'Chest (cm)' : 99,
    'Hips (cm)' : 83,
    'Waist (cm)' : 97,
    'Shoe Size (EU)' : '46/47',
    'Birth date' : '14 Oct 1995',
    'Age' : years_old,
    'Currently in' : 'Lisboa, PT'
}

st.write('------------')

col1, col2 = st.columns([5,4])
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
