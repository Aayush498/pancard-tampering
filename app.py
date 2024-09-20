import streamlit as st
from PIL import Image
import numpy as np
import cv2

st.title("PAN Card Tampering Detection")

# Upload original and tampered images
st.subheader("Upload the original PAN card image")
original_image = st.file_uploader("Choose the original image", type=["jpg", "jpeg", "png"])

st.subheader("Upload the suspected tampered PAN card image")
tampered_image = st.file_uploader("Choose the tampered image", type=["jpg", "jpeg", "png"])

# Function to compare images
def detect_tampering(original, tampered):
    # Load images and convert to grayscale
    original_gray = cv2.cvtColor(np.array(original), cv2.COLOR_RGB2GRAY)
    tampered_gray = cv2.cvtColor(np.array(tampered), cv2.COLOR_RGB2GRAY)

    # Resize tampered image to match original size
    tampered_gray = cv2.resize(tampered_gray, (original_gray.shape[1], original_gray.shape[0]))

    # Compute difference between the two images
    diff = cv2.absdiff(original_gray, tampered_gray)

    # If there are non-zero differences, tampering is detected
    if np.sum(diff) > 0:
        return "Tampering Detected!"
    else:
        return "No Tampering Detected"

# Process images after upload
if original_image is not None and tampered_image is not None:
    original = Image.open(original_image)
    tampered = Image.open(tampered_image)

    # Display both images side by side
    st.image([original, tampered], caption=["Original Image", "Tampered Image"], width=300)

    # Run tampering detection
    result = detect_tampering(original, tampered)
    
    st.subheader("Result")
    st.write(result)
