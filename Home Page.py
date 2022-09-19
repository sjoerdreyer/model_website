import streamlit as st
from PIL import Image

# HTML color codes : https://htmlcolorcodes.com/color-picker/
# HTML emojis : https://www.quackit.com/character_sets/emoji/emoji_v3.0/unicode_emoji_v3.0_characters_all.cfm


st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Sjoerd as a Model",
                   page_icon = ":tada:",
                   layout='wide')

st.sidebar.success("Select from the menu above.")

st.markdown("<h2 style='text-align: center; color: #2A79CC;'>&#x1F44B Hi! Im Sjoerd &#x1F44B</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #2A79CC;'>From the Netherlands &#x1F1F3&#x1F1F1 born and raised in Peru &#x1F1F5&#x1F1EA</h2>", unsafe_allow_html=True)

wallaroo_beach = Image.open('raw_data/wallaroo3.jpeg')
st.image(wallaroo_beach)

st.markdown("<h4 style='text-align: center; color: #82CAF8;'>I like to use my image to create value for brands</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #82CAF8;'>Am I a fit for YOUR brand?</h4>", unsafe_allow_html=True)
st.write('------------')

st.markdown("<h6 style='text-align: center; color: #82CAF8;'>Contact me at:</h6>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: center; color: #82CAF8;'>&#x1F4E7 sjoerdreyer@gmail.com &#x1F4E7</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: #82CAF8;'>&#x1F4F2 +31653406466 &#x1F4F2</h6>", unsafe_allow_html=True)
