import streamlit as st
from PIL import Image

from lottie import load_lottiefile
from streamlit_lottie import st_lottie

col27,col28,col29 = st.columns(3)
with col28:
    foto_flash = load_lottiefile('lottie_json_files/foto_flash.json')
    st_lottie(foto_flash)

#Bike on beach
wallaroo_bike = Image.open('raw_data/wallaroo5.jpeg')
wallaroo_bike2 = Image.open('raw_data/wallaroo6.jpeg')
col4, col5, col6, col7 = st.columns([1,3,3,1])
col5.image(wallaroo_bike)
col6.image(wallaroo_bike2)

#Beach
col1, col2, col3 = st.columns([1,3,1])
wallaroo_beach = Image.open('raw_data/wallaroo3.jpeg')
col2.image(wallaroo_beach)


#Hammock & table expl. kittens
wallaroo_hammock = Image.open('raw_data/wallaroo8.jpeg')
wallaroo_table = Image.open('raw_data/wallaroo9.jpeg')
col17,col18,col19,col20 = st.columns([1,20,20,1])
col18.image(wallaroo_hammock)
col19.image(wallaroo_table)

#Swing alone
col8, col9, col10 = st.columns([1,3,1])
wallaroo_beach2 = Image.open('raw_data/wallaroo4.jpeg')
col9.image(wallaroo_beach2)

#Hanging
wallaroo_s = Image.open('raw_data/wallaroo10.jpeg')
col24,col25,col26 = st.columns([1,3,1])
col25.image(wallaroo_s)

#Swing
wallaroo_swing = Image.open('raw_data/wallaroo7.jpeg')
col21,col22,col23 = st.columns([1,3,1])
col22.image(wallaroo_swing)




col14, col15, col16 = st.columns([3,4,1])

col15.markdown("<a style='text-align: center; href=url'>https://wallaroohats.com/</a>", unsafe_allow_html=True)

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
