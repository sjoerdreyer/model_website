import streamlit as st
from PIL import Image


col1, col2, col3 = st.columns([3,4,1])

col2.markdown("<a style='text-align: center; href=url'>https://unsplash.com/es/s/fotos/portraits</a>", unsafe_allow_html=True)


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

col4, col5, col6 = st.columns([3,4,1])

col5.markdown("<a style='text-align: center; href=url'>https://unsplash.com/es/s/fotos/portraits</a>", unsafe_allow_html=True)
