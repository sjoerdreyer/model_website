import streamlit as st
from PIL import Image

from lottie import load_lottiefile
from streamlit_lottie import st_lottie



col12,col13,col14 = st.columns([2,2,2])
with col13:
    ph_pol_y = load_lottiefile('lottie_json_files/photo_polaroid_yellow.json')
    st_lottie(ph_pol_y,
              speed=2)


front = Image.open('raw_data/front.jpeg')
left = Image.open('raw_data/left.jpeg')
right = Image.open('raw_data/right.jpeg')

col7, col8, col9, col10, col11 = st.columns([1,5,5,5,1])

col8.image(left)
col9.image(front)
col10.image(right)

col12, col13, col14 = st.columns([1,2,1])
frontfull = Image.open('raw_data/frontfull.jpeg')
col13.image(frontfull)

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
