import streamlit as st

from PIL import Image

width = st.slider('What is the width in pixels?', 0, 700, 350)
height = st.slider('What is the height in pixels?', 0, 700, 350)

#upload the image

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    image = Image.open(uploaded_image)

    st.image(image, caption='test', width=width)