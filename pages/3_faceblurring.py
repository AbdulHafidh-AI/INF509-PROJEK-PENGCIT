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
def blur_detected_objects(our_image, detections):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)

    for (x, y, w, h) in detections:
        roi = img[y:y+h, x:x+w]
        blurred_roi = cv2.GaussianBlur(roi, (25, 25), 0)  # You can adjust the blur kernel size as needed
        img[y:y+h, x:x+w] = blurred_roi

    return img

def detect_faces(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # blur detected faces
        img = blur_detected_objects(our_image, faces)
    return img, faces 

def detect_eyes(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        # blur detected eyes
        img = blur_detected_objects(our_image, eyes)
    return img



def main():
    """Face Detection App"""
    st.title("Face Detection App")
    st.header("Built with Streamlit and OpenCV")

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
        if st.button("Process"):
            if feature_choice == 'Faces':
                result_img, result_faces = detect_faces(our_image)
                st.image(result_img)
                st.success("Found {} faces".format(len(result_faces)))
            elif feature_choice == 'Eyes':
                result_img = detect_eyes(our_image)
                st.image(result_img)

    elif choice == 'About':
        st.subheader("About Face Detection App")
        st.markdown("Built with Streamlit by Tekno Senpai / IPK 5")

if __name__ == '__main__':
    main()
