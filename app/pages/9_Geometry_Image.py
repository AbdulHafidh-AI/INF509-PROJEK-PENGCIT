import streamlit as st
from PIL import Image
import numpy as np

def nearest_interpolation(image, dimension):
    '''Nearest neighbor interpolation method to convert small image to original image
    Parameters:
    image (PIL.Image): Small image
    dimension (tuple): resizing image dimension

    Returns:
    PIL.Image: Resized image
    '''
    return image.resize(dimension, Image.NEAREST)

def bilinear_interpolation(image, dimension):
    '''Bilinear interpolation method to convert small image to original image
    Parameters:
    image (PIL.Image): Small image
    dimension (tuple): resizing image dimension

    Returns:
    PIL.Image: Resized image
    '''
    return image.resize(dimension, Image.BILINEAR)

def lanczos_interpolation(image, dimension):
    '''Cubic interpolation method to convert small image to original image
    Parameters:
    image (PIL.Image): Small image
    dimension (tuple): resizing image dimension

    Returns:
    PIL.Image: Resized image
    '''
    return image.resize(dimension, Image.LANCZOS)

st.title("Geometrical Image")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width="never")

    # Slider to adjust scale percent
    scale_percent = st.slider("Scale Percent", 1, 1000, 30)

    # Display the original image
    img = Image.open(uploaded_image)
    st.header("Original Image")
    st.image(img, use_column_width="never")

    # Display the resized image using nearest neighbor interpolation
    st.header("Resized (Nearest Neighbor)")
    width = int(img.size[0] * scale_percent / 100)
    height = int(img.size[1] * scale_percent / 100)
    dim = (width, height)

    resized_nearest = nearest_interpolation(img, dim)
    st.image(resized_nearest, use_column_width=True)

    # Display the resized image using bilinear interpolation
    st.header("Resized (Bilinear)")
    resized_bilinear = bilinear_interpolation(img, dim)
    st.image(resized_bilinear, use_column_width=True)

    st.header("Resized (Lanczos)")
    resized_cubic = lanczos_interpolation(img, dim)
    st.image(resized_cubic, use_column_width=True)
    
    

    # # Add vertical spacing using Markdown
    # st.markdown("<div style='height:500px'></div>", unsafe_allow_html=True)
    
    # st.header("Resized (Nearest Neighbor actual size)")
    # st.image(resized_nearest, use_column_width="never")

    # st.header("Resized (Bilinear actual size)")
    # st.image(resized_bilinear, use_column_width="never")

    # st.header("Resized (Lanczos actual size)")
    # st.image(resized_cubic, use_column_width="never")
