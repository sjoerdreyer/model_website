import streamlit as st
from PIL import Image
from lottie import load_lottiefile
from streamlit_lottie import st_lottie


col12,col13,col14 = st.columns([2,3,2])
with col13:
    char_walk = load_lottiefile('lottie_json_files/character-walk.json')
    st_lottie(char_walk)


yirkoS1 = Image.open('raw_data/yirkoS1.jpeg')
yirkoS2 = Image.open('raw_data/yirkoS2.jpeg')
yirkoS3 = Image.open('raw_data/yirkoS3.jpeg')

col7, col8, col9, col10, col11 = st.columns([1,10,10,10,1])

col8.image(yirkoS1)
col9.image(yirkoS2)
col10.image(yirkoS3)

col4, col5, col6 = st.columns([4,4,2])

col5.markdown("<a style='text-align: center; href=url'>https://yirkosivirich.com/</a>", unsafe_allow_html=True)

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
