import cv2
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
import tempfile
import os


st.header("Vintage Image")

st.write("Pada halaman ini, kita akan mencoba untuk memberikan efek vintage pada citra yang diunggah dengan filter sepia.")

# upload file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Simpan citra yang diunggah sebagai file sementara
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Baca citra yang diunggah
    image = cv2.imread(temp_file_path)

    # Hapus file sementara
    os.remove(temp_file_path)

    # menambahkan efek sepia

    sepia_filter = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])

    sepia_img = image @ sepia_filter.T

    sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)

    # menampilkan citra asli dan citra yang sudah diberi efek sepia

    col1, col2 = st.columns(2)

    col1.write("Citra Asli")

    col1.image(image, use_column_width=True)

    col2.write("Citra yang sudah diberi efek sepia")

    #
    # save image to local storage

    cv2.imwrite('sepia_img.jpg', sepia_img)

    col2.image('sepia_img.jpg', use_column_width=True)



