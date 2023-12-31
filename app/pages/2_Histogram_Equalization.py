import cv2
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
import tempfile
import os

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
    
    # Ubah citra ke grayscale jika belum
    if len(image.shape) == 3:
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        grayscale_image = image  # Citra sudah grayscale
    
    # Bagi tampilan menjadi dua kolom
    col1, col2 = st.columns(2)
    
    # Tampilkan citra grayscale di kolom pertama
    col1.write("Citra Asli")
    col1.image(grayscale_image,use_column_width=True)
    
    st.set_option('deprecation.showPyplotGlobalUse', False) # Untuk menghindari warning dikarenakan regulasi baru pada streamlit

    # Tampilkan histogram citra grayscale di kolom kedua
    col2.write("Histogram Citra")
    hist_values, bins, _ = plt.hist(grayscale_image.ravel(), 256, [0, 256])
    col2.pyplot()


    # CODE UNTUK EKUALISASI HISTOGRAM DAN MENAMPILKAN CITRA YANG TELAH DI EKUALISASI HISTOGRAMNYA
    equalized_image = cv2.equalizeHist(grayscale_image)
    
    col3, col4 = st.columns(2)

    

    # Tampilkan citra grayscale yang sudah di equalisasi histogramnya
    col3.write("Citra yang sudah di equalisasi histogramnya")
    col3.image(equalized_image, use_column_width=True)

    # Tampilkan histogram equalization citra grayscale
    col4.write("Histogram Equalization Citra ")
    hist_values_eq, bins_eq, _ = plt.hist(equalized_image.ravel(), 256, [0, 256])
    col4.pyplot()


    col5, col6 = st.columns(2)

    # Menampilkan citra RGB yang sudah di equalisasi histogramnya

    # Ubah citra ke RGB

    if len(image.shape) == 3:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        rgb_image = image

    # Ubah citra RGB ke HSV
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # Ekualisasi histogram pada channel V

    hsv_image[:, :, 2] = cv2.equalizeHist(hsv_image[:, :, 2])

    # Ubah citra HSV ke RGB

    equalized_rgb_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)

    # Tampilkan citra RGB yang sudah di equalisasi histogramnya

    col5.write("Citra RGB yang sudah di equalisasi histogramnya")
    col5.image(equalized_rgb_image, use_column_width=True)

    # Tampilkan histogram equalization citra RGB

    col6.write("Histogram Equalization Citra RGB")

    color = ('r', 'g', 'b')
    for i, col in enumerate(color):
        histr = cv2.calcHist([equalized_rgb_image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])

    col6.pyplot()

    

