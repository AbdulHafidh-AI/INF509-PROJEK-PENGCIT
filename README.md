# INF509-PROJEK-PENGCIT (Group 1)

## Team Member
Our team consist 3 people:
1. ABDUL HAFIDH 
2. AHMAD FAQIH AL GHIFFARY
3. FURQAN AL GHIFARI ZULVA

## Overview

This project consists of six main components aimed at enhancing and processing images. Each component serves a specific purpose:

1. **Histogram Equalization**: This component stratifies the histogram to improve image clarity.

2. **Face Blurring**: Utilizing Haarcascade for face detection, this part detects faces, draws bounding boxes around them, and applies Gaussian blur to obscure facial features.

3. **Edge Detection**: The Canny algorithm is used in this component to detect the edges of an image.

4. **Image Segmentation**: This segment employs a pretrained model for image segmentation, particularly for objects related to chemical materials. To use the pre-trained PyTorch model, please download it from [here](https://zenodo.org/record/3697767) or [here](https://drive.google.com/file/d/1wWGPoa7aKBlvml6Awe4AzJUbNlR72K6X/view?usp=sharing) and place it in the 'model' folder.

5. **Image Colorization**: An autoencoder approach is implemented here. ResNet-18 is used as the encoder to extract features, and the decoder reconstructs the image, effectively colorizing grayscale images.

6. **Vintage Image Effect**: In this part, a sepia filter is applied to give images a vintage look.


# How to run this web???

## Create Virtual Environment

<pre><code> python3 -m venv env </code> </pre>

## Activate the virtual environment

<pre><code> source env/bin/activate </code> </pre>

## Install the requirement library

<pre><code> pip3 install -r requirements.txt </code> </pre>

## Finally turn on streamlit server on your local computer

<pre><code> streamlit run app/1_homepage.py </code></pre>


# Citation 

## Image segmentation Reference

```
@article{eppel2020computer,
  title={Computer vision for recognition of materials and vessels in chemistry lab settings and the vector-LabPics data set},
  author={Eppel, Sagi and Xu, Haoping and Bismuth, Mor and Aspuru-Guzik, Alan},
  journal={ACS central science},
  volume={6},
  number={10},
  pages={1743--1752},
  year={2020},
  publisher={ACS Publications}
}

```

