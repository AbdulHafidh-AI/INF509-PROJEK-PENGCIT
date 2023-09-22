import cv2
import streamlit as st
import tempfile
import os

st.header("Edge Detection")
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



    st.write("Algoritma Canny adalah algoritma deteksi tepi yang dikembangkan oleh John F. Canny pada tahun 1986. Algoritma ini bekerja dengan cara mendeteksi gradien dari citra, kemudian menggunakan teknik non-maksimum supression untuk menghilangkan tepi palsu, dan menggunakan thresholding untuk menentukan tepi yang valid.")

    st.header('Langkah-Langkah Algoritma Canny')

    st.subheader('1. Penghalusan (Smoothing)')
    st.write("Langkah pertama adalah menghaluskan citra dengan menggunakan filter Gaussian. "
            "Hal ini bertujuan untuk mengurangi noise pada citra, sehingga tepi yang dideteksi lebih akurat.")

    st.subheader('2. Pemetaan Gradien (Gradient Mapping)')
    st.write("Langkah kedua adalah menghitung gradien dari citra. Gradien adalah ukuran perubahan intensitas warna dari satu piksel ke piksel lainnya. "
            "Algoritma Canny menggunakan dua filter untuk menghitung gradien, yaitu filter gradien x dan filter gradien y.")

    st.subheader('3. Non-Maksimum Suppression')
    st.write("Langkah ketiga adalah menggunakan teknik non-maksimum suppression untuk menghilangkan tepi palsu. "
            "Teknik ini bekerja dengan cara hanya mempertahankan piksel tepi yang merupakan lokal maksimum dari gradien.")

    st.subheader('4. Thresholding')
    st.write("Langkah keempat adalah menggunakan thresholding untuk menentukan tepi yang valid. "
            "Algoritma Canny menggunakan dua threshold, yaitu threshold rendah dan threshold tinggi. "
            "Piksel yang gradiennya lebih besar dari threshold tinggi akan dianggap sebagai tepi, sedangkan piksel yang gradiennya lebih kecil dari threshold rendah akan dianggap bukan tepi.")

    st.subheader('5. Tracking Tepi (Edge Tracking)')
    st.write("Langkah kelima adalah menggunakan tracking tepi untuk menghubungkan tepi yang terputus. "
            "Tracking tepi bekerja dengan cara menghubungkan tepi yang memiliki gradien yang sama.")



