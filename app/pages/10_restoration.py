import streamlit as st
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter, median_filter, rank_filter

def apply_lowpass_filter(image, sigma=1):
    return gaussian_filter(image, sigma=sigma)

def apply_median_filter(image, size=3):
    return median_filter(image, size=size)

def apply_rank_order_filter(image, rank=3):
    return rank_filter(image, rank, size=3)

def apply_outlier_method(image, threshold=30):
    cleaned = np.where(np.abs(image - np.median(image)) <= threshold, image, np.median(image))
    return cleaned

def apply_gaussian_noise(image, sigma=25):
    row, col, ch = image.shape
    gauss = np.random.normal(0, sigma, (row, col, ch))
    noisy = image + gauss
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)

def apply_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    row, col, ch = image.shape
    noisy = np.copy(image)

    # Salt noise
    salt_pixels = np.random.choice((0, 255), size=(row, col, ch), p=[salt_prob, 1 - salt_prob])
    noisy[salt_pixels == 0] = 255

    # Pepper noise
    pepper_pixels = np.random.choice((0, 255), size=(row, col, ch), p=[pepper_prob, 1 - pepper_prob])
    noisy[pepper_pixels == 0] = 0

    return noisy.astype(np.uint8)

    
def main():
    """Image Restoration"""
    st.title("Image Restoration")

    activities = ["Noise Removal", "Image Denoising"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Noise Removal":
        noise_removal()
    elif choice == "Image Denoising":
        image_denoising()

def noise_removal():

    st.title("Image Noise Generator")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert image to numpy array
        image_array = np.array(image)

        # Gaussian Noise
        st.subheader("Gaussian Noise")
        sigma = st.slider("Select sigma value for Gaussian noise:", 0.1, 100.0, 25.0)
        noisy_image_gaussian = apply_gaussian_noise(image_array, sigma=sigma)
        st.image(noisy_image_gaussian, caption="Image with Gaussian Noise", use_column_width=True)


        # Salt and Pepper Noise
        st.subheader("Salt and Pepper Noise")
        salt_prob = st.slider("Select probability for salt noise:", 0.01, 0.1, 0.02)
        pepper_prob = st.slider("Select probability for pepper noise:", 0.01, 0.1, 0.02)
        noisy_image_salt_pepper = apply_salt_and_pepper_noise(image_array, salt_prob=salt_prob, pepper_prob=pepper_prob)
        st.image(noisy_image_salt_pepper, caption="Image with Salt and Pepper Noise", use_column_width=True)

        # Save Button
        if st.button("Save Images"):
            # Save the images locally
            Image.fromarray(noisy_image_gaussian).save("noisy_image_gaussian.png")
            Image.fromarray(noisy_image_salt_pepper).save("noisy_image_salt_pepper.png")
            st.success("Images saved successfully!")

def image_denoising():
    st.title("Image Processing App")

    # Upload image through Streamlit
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image using PIL
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert the image to a NumPy array
        img_array = np.array(image)

        # Choose the filter type
        filter_type = st.selectbox("Select Filter", ["Lowpass Filter", "Median Filter", "Rank Order Filter", "Outlier Method"])

        # Apply the selected filter
        if filter_type == "Lowpass Filter":
            sigma = st.slider("Select Sigma for Lowpass Filter", 0.1, 10.0, 1.0, step=0.1)
            filtered_image = apply_lowpass_filter(img_array, sigma=sigma)
        elif filter_type == "Median Filter":
            size = st.slider("Select Size for Median Filter", 3, 21, 3, step=2)
            filtered_image = apply_median_filter(img_array, size=size)
        elif filter_type == "Rank Order Filter":
            rank = st.slider("Select Rank for Rank Order Filter", 1, 10, 3, step=1)
            filtered_image = apply_rank_order_filter(img_array, rank=rank)
        elif filter_type == "Outlier Method":
            threshold = st.slider("Select Threshold for Outlier Method", 1, 100, 30, step=1)
            filtered_image = apply_outlier_method(img_array, threshold=threshold)

        # Display the filtered image
        st.image(filtered_image, caption=f"{filter_type} Result", use_column_width=True)

        # Save the filtered image
        if st.button("Save Image"):
            # Convert NumPy array back to PIL Image
            filtered_pil_image = Image.fromarray(filtered_image)

            # Save the filtered image
            filtered_pil_image.save("filtered_image.png")
            st.success("Filtered image saved successfully!")


if __name__ == '__main__':
    main()

