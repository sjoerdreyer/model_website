import streamlit as st
from PIL import Image
from lottie import load_lottiefile
from streamlit_lottie import st_lottie


col1,col2,col3 = st.columns([2,3,2])
with col2:
    flash = load_lottiefile('lottie_json_files/flash_photographer.json')
    st_lottie(flash)


saga_f = Image.open('raw_data/sagaf.jpeg')
st.image(saga_f)


col4, col5, col6 = st.columns([3,4,1])

col5.markdown("<a style='text-align: center; href=url'>https://tienda.falabella.com/falabella-cl/</a>", unsafe_allow_html=True)

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
