import streamlit as st
from PIL import Image

col1, col2, col3 = st.columns([4,4,2])

col2.markdown("<a style='text-align: center; href=url'>https://carkella.com/</a>", unsafe_allow_html=True)

carkella1 = Image.open('raw_data/carkella1.jpeg')
carkella2 = Image.open('raw_data/carkella2.jpeg')
carkella3 = Image.open('raw_data/carkella3.jpeg')


col7, col8, col9, col10, col11 = st.columns([1,5,7,5,1])

col8.image(carkella2)
col9.image(carkella3)
col10.image(carkella1)



col4, col5, col6 = st.columns([4,4,2])

col5.markdown("<a style='text-align: center; href=url'>https://carkella.com/</a>", unsafe_allow_html=True)
