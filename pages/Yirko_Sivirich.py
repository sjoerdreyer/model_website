import streamlit as st
from PIL import Image


col1, col2, col3 = st.columns([4,4,2])

col2.markdown("<a style='text-align: center; href=url'>https://yirkosivirich.com/</a>", unsafe_allow_html=True)


yirkoS1 = Image.open('raw_data/yirkoS1.jpeg')
yirkoS2 = Image.open('raw_data/yirkoS2.jpeg')
yirkoS3 = Image.open('raw_data/yirkoS3.jpeg')

col7, col8, col9, col10, col11 = st.columns([1,10,10,10,1])

col8.image(yirkoS1)
col9.image(yirkoS2)
col10.image(yirkoS3)

col4, col5, col6 = st.columns([4,4,2])

col5.markdown("<a style='text-align: center; href=url'>https://yirkosivirich.com/</a>", unsafe_allow_html=True)
