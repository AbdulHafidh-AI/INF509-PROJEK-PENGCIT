import cv2
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

    # Mengaplikasikan canny untuk mendeteksi tepi
    edges = cv2.Canny(grayscale_image,100,200)

    # Menampilkan citra hasil deteksi tepi

    col2.write("Citra hasil deteksi tepi")

    col2.image(edges,use_column_width=True)



