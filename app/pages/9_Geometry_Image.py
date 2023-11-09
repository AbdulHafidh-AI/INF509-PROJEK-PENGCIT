import streamlit as st
import cv2
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
from math import sqrt,floor
import numpy as np

def nearest_interpolation(image, dimension):
    '''Nearest neighbor interpolation method to convert small image to original image
    Parameters:
    img (numpy.ndarray): Small image
    dimension (tuple): resizing image dimension

    Returns:
    numpy.ndarray: Resized image
    '''
    new_image = np.zeros((dimension[0], dimension[1], image.shape[2]))

    enlarge_time = int(
        sqrt((dimension[0] * dimension[1]) / (image.shape[0]*image.shape[1])))

    for i in range(dimension[0]):
        for j in range(dimension[1]):
            row = floor(i / enlarge_time)
            column = floor(j / enlarge_time)

            new_image[i, j] = image[row, column]

    return new_image

def bilinear_interpolation(image, dimension):
    '''Bilinear interpolation method to convert small image to original image
    Parameters:
    img (numpy.ndarray): Small image
    dimension (tuple): resizing image dimension

    Returns:
    numpy.ndarray: Resized image
    '''
    height = image.shape[0]
    width = image.shape[1]

    scale_x = (width)/(dimension[1])
    scale_y = (height)/(dimension[0])

    new_image = np.zeros((dimension[0], dimension[1], image.shape[2]))

    for k in range(3):
        for i in range(dimension[0]):
            for j in range(dimension[1]):
                x = (j+0.5) * (scale_x) - 0.5
                y = (i+0.5) * (scale_y) - 0.5

                x_int = int(x)
                y_int = int(y)

                # Prevent crossing
                x_int = min(x_int, width-2)
                y_int = min(y_int, height-2)

                x_diff = x - x_int
                y_diff = y - y_int

                a = image[y_int, x_int, k]
                b = image[y_int, x_int+1, k]
                c = image[y_int+1, x_int, k]
                d = image[y_int+1, x_int+1, k]

                pixel = a*(1-x_diff)*(1-y_diff) + b*(x_diff) * \
                    (1-y_diff) + c*(1-x_diff) * (y_diff) + d*x_diff*y_diff

                new_image[i, j, k] = pixel.astype(np.uint8)

    return new_image


st.title("Geometrical Image")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # membuat slider untuk mengatur scale_percent

    scale_percent = st.slider("Scale Percent", 1, 100, 50)

    # Bagi tampilan citra menjadi dua baris dan dua kolom
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

   # Menampilkan citra asli

    img = Image.open(uploaded_image)

    col1.header("Original Image")

    col1.image(img, use_column_width=True)

   

    # Menampilkan citra yang telah diubah ukurannya

    col2.header("Resized Image")

    width = int(img.size[0] * scale_percent / 100)

    height = int(img.size[1] * scale_percent / 100)

    dim = (width, height)

    resized = img.resize(dim)

    col2.image(resized, use_column_width=True)

    # Menampilkan citra yang telah diubah ukurannya dengan metode nearest interpolation

    


    



    


    

