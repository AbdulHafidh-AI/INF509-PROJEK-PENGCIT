import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

def perform_dilation(image_data, dilation_size=5):
    pil_image = Image.open(image_data)
    img = np.array(pil_image)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (dilation_size, dilation_size))
    dilation = cv2.dilate(img, kernel, iterations=1)
    return img, dilation

def perform_erosion(image_data, erosion_size=5):
    pil_image = Image.open(image_data)
    img = np.array(pil_image)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (erosion_size, erosion_size))
    erosion = cv2.erode(img, kernel, iterations=1)
    return img, erosion

def perform_opening(image_data, opening_size=19):
    pil_image = Image.open(image_data)
    img = np.array(pil_image)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (opening_size, opening_size))
    opening_morph = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return img, opening_morph

def perform_closing(image_data, closing_size=23):
    pil_image = Image.open(image_data)
    img = np.array(pil_image)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (closing_size, closing_size))
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return img, closing

st.title("Morphological Operations with Streamlit")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    size = st.slider("Kernel Size", min_value=1, max_value=30, value=5)

    # Bagi tampilan citra menjadi dua baris dan dua kolom
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.write("Dilation")
    img, dilation = perform_dilation(uploaded_image, size)
    col1.image(dilation, caption="Dilation Result", use_column_width=True)

    col2.write("Erosion")
    img, erosion = perform_erosion(uploaded_image, size)
    col2.image(erosion, caption="Erosion Result", use_column_width=True)

    col3.write("Opening")
    img, opening = perform_opening(uploaded_image, size)
    col3.image(opening, caption="Opening Result", use_column_width=True)

    col4.write("Closing")
    img, closing = perform_closing(uploaded_image, size)
    col4.image(closing, caption="Closing Result", use_column_width=True)
