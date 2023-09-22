import streamlit as st


st.set_page_config(
    page_title="Pengolahan Citra",
    page_icon="👋",
)


st.title("Projek Pengolahan Citra")
st.header("By Kelompok 1")


### Menampilkan creator yang membuat web ini
col1, col2, col3 = st.columns(3)

with col1:

    st.write("""
   ### Faqih
   """)
    st.image('public/assets/image/about_us/Faqih.png')



with col2:

   st.write("""
   ### Abdul
   """)
   st.image('public/assets/image/about_us/Abdul.png')




with col3:
   st.write("""
   ### Furqan 
   """)
   st.image('public/assets/image/about_us/Furqan.png')


st.write("Projek ini bertujuan untuk memenuhi tugas mata kuliah Pengolahan Citra. Projek ini dibuat oleh Faqih, Abdul, dan Furqan.")