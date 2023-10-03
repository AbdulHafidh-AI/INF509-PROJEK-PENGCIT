# Core Pkgs
import streamlit as st 
import cv2
from PIL import Image, ImageEnhance
import numpy as np 
import os

@st.cache
def load_image(img):
    im = Image.open(img)
    return im

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

# Function to apply blur to the detected objects
def blur_detected_objects(our_image, detections, blur_strength):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)

    # Pastikan kedua dimensi kernel adalah bilangan ganjil
    kernel_size = (blur_strength, blur_strength)
    if kernel_size[0] % 2 == 0:
        kernel_size = (kernel_size[0] + 1, kernel_size[1])
    if kernel_size[1] % 2 == 0:
        kernel_size = (kernel_size[0], kernel_size[1] + 1)

    for (x, y, w, h) in detections:
        roi = img[y:y+h, x:x+w]
        blurred_roi = cv2.GaussianBlur(roi, kernel_size, 0)
        img[y:y+h, x:x+w] = blurred_roi

    return img


def detect_faces(our_image, blur_strength):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    img = blur_detected_objects(our_image, faces, blur_strength)
    return img, faces 

def detect_eyes(our_image, blur_strength):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    img = blur_detected_objects(our_image, eyes, blur_strength)
    return img

def main():
    """Face Detection App"""
    st.title("Face Detection")
    st.header("Built by Kelompok 1")

    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Detection':
        st.subheader("Face Detection")
        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            st.image(our_image)

        # Face Detection
        task = ["Faces", "Eyes"]
        feature_choice = st.sidebar.selectbox("Find Features", task)
        
        blur_strength = st.slider("Set Blur Strength", 5, 50, 25)  # Mengatur kekuatan blur
        blur_strength = blur_strength // 5 * 5  # Membulatkan ke bilangan perkalian
        
        
        if feature_choice == 'Faces':
                result_img, result_faces = detect_faces(our_image, blur_strength)
                st.image(result_img)
                st.success("Found {} faces".format(len(result_faces)))
        elif feature_choice == 'Eyes':
                result_img = detect_eyes(our_image, blur_strength)
                st.image(result_img)

    elif choice == 'About':
        st.subheader("About Face Detection App")
        st.markdown("Built with Streamlit by Tekno Senpai / IPK 5")

if __name__ == '__main__':
    main()
