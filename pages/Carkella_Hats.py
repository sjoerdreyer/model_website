import streamlit as st
from PIL import Image
from lottie import load_lottiefile
from streamlit_lottie import st_lottie


col1,col2,col3 = st.columns([2,3,2])
with col2:
    l_cam_r = load_lottiefile('lottie_json_files/left_camera_right.json')
    st_lottie(l_cam_r)



#Carkella
carkella1 = Image.open('raw_data/carkella1.jpeg')
carkella2 = Image.open('raw_data/carkella2.jpeg')
carkella3 = Image.open('raw_data/carkella3.jpeg')
carkella4 = Image.open('raw_data/carkella4.jpg')
carkella5 = Image.open('raw_data/carkella5.jpg')
carkella6 = Image.open('raw_data/carkella6.jpg')

col7, col8, col10, col11 = st.columns([1,6,6,1])

col8.image(carkella3)
col10.image(carkella5)

col12, col13, col14, col15, col16, col17 = st.columns([1,5,5,5,5,1])

col13.image(carkella2)
col14.image(carkella1)
col15.image(carkella4)
col16.image(carkella6)


# col7, col8, col9, col10, col11 = st.columns([1,5,7,5,1])

# carkella1 = Image.open('raw_data/carkella1.jpeg')
# carkella2 = Image.open('raw_data/carkella2.jpeg')
# carkella3 = Image.open('raw_data/carkella3.jpeg')

# col8.image(carkella2)
# col9.image(carkella3)
# col10.image(carkella1)


# col12, col13, col14, col15, col16 = st.columns([1,5,7,5,1])

# carkella4 = Image.open('raw_data/carkella4.jpg')
# carkella5 = Image.open('raw_data/carkella5.jpg')
# carkella6 = Image.open('raw_data/carkella6.jpg')

# col13.image(carkella4)
# col14.image(carkella5)
# col15.image(carkella6)



col4, col5, col6 = st.columns([4,4,2])

col5.markdown("<a style='text-align: center; href=url'>https://carkella.com/</a>", unsafe_allow_html=True)

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
