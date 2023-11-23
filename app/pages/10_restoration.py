# Image restoration

""" 
Cleaning Salt and Pepper Noise with OpenCV

1. Lowpass filtering
2. Median filtering
3. Rank-oder filtering
4. Outlier Method

"""

import streamlit as st
import cv2
import numpy as np

def apply_lowpass_filter(image):
    # Apply lowpass filtering
    return cv2.GaussianBlur(image, (5, 5), 0)

def apply_median_filter(image):
    # Apply median filtering
    return cv2.medianBlur(image, 5)

def apply_rank_order_filter(image):
    # Apply rank-order filtering
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

def apply_outlier_method(image):
    # Apply outlier method
    return cv2.fastNlMeansDenoising(image, None, h=10, templateWindowSize=7, searchWindowSize=21)


st.title("Image Restoration")

# Upload image through Streamlit
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    # Read the image
    image = cv2.imread(uploaded_file.name)

    # Read the image using OpenCV directly from the file object
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)

    # Display the original image
    st.image(image, caption="Original Image", use_column_width=True)

    # Apply image restoration methods
    restored_lowpass = apply_lowpass_filter(image.copy())
    restored_median = apply_median_filter(image.copy())
    restored_rank_order = apply_rank_order_filter(image.copy())
    restored_outlier = apply_outlier_method(image.copy())

    # Display the restored images
    st.image(restored_lowpass, caption="Lowpass Filtering", use_column_width=True)
    st.image(restored_median, caption="Median Filtering", use_column_width=True)
    st.image(restored_rank_order, caption="Rank-order Filtering", use_column_width=True)
    st.image(restored_outlier, caption="Outlier Method", use_column_width=True)

        
