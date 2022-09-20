import streamlit as st
from PIL import Image

from lottie import load_lottiefile
from streamlit_lottie import st_lottie


# Lottie files : https://lottiefiles.com/
# HTML color codes : https://htmlcolorcodes.com/color-picker/
# HTML emojis : https://www.quackit.com/character_sets/emoji/emoji_v3.0/unicode_emoji_v3.0_characters_all.cfm


st.set_option('deprecation.showPyplotGlobalUse', False)

#Tab title
st.set_page_config(page_title="Sjoerd de Wit",
                   page_icon = ":tada:",
                   layout='wide')

#Sidebar menu
st.sidebar.success("Select from the menu above.")

# MainMenu visibility hidden
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

#Padding
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)



st.markdown("<h2 style='text-align: center; color: #2A79CC;'>&#x1F44B Hi i'm Sjoerd &#x1F44B</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #2A79CC;'>&#x1F1F3&#x1F1F1 From the Netherlands &#x1F1F3&#x1F1F1</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #2A79CC;'>&#x1F1F5&#x1F1EA Born and raised in Peru &#x1F1F5&#x1F1EA</h5>", unsafe_allow_html=True)

# st.write('------------')
# col1,col2,col3 = st.columns(3)
# with col2:
#     welcome = load_lottiefile('lottie_json_files/welcome_.json')
#     st_lottie(welcome)
# st.markdown("<h5 style='text-align: center; color: #2A79CC;'>To my modelling portofolio</h5>", unsafe_allow_html=True)


st.write('------------')

wallaroo_beach = Image.open('raw_data/wallaroo3.jpeg')
st.image(wallaroo_beach)


# with col5:
#     model_lottie = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_efenfp40.json")
#     st_lottie(model_lottie)



st.write(' ')

st.markdown("<h5 style='text-align: center; color: #2A79CC;'>I employ my image to create value for brands</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: #2A79CC;'>Use the drop down menu on the left to browse through my details and past projects</h5>", unsafe_allow_html=True)

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
