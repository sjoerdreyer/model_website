import streamlit as st
from PIL import Image


col1, col2, col3 = st.columns([3,4,1])

col2.markdown("<a style='text-align: center; href=url'>https://tienda.falabella.com/falabella-cl/</a>", unsafe_allow_html=True)


saga_f = Image.open('raw_data/sagaf.jpeg')
st.image(saga_f)


col4, col5, col6 = st.columns([3,4,1])

col5.markdown("<a style='text-align: center; href=url'>https://tienda.falabella.com/falabella-cl/</a>", unsafe_allow_html=True)
