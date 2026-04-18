import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Reflectivity Analyzer (Sign-Focused)")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = np.array(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 1: enhance contrast
    gray = cv2.equalizeHist(gray)

    # Step 2: threshold to detect bright regions
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Step 3: find contours (bright regions)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        st.error("No reflective region detected")
    else:
        # Get largest bright region (likely sign board)
        largest = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(largest)

        # Extract region
        sign_region = gray[y:y+h, x:x+w]

        st.image(sign_region, caption="Detected Reflective Region")

        # Analyze only this region
        brightness = np.mean(sign_region)
        contrast = np.std(sign_region)

        st.write("Region Brightness:", round(brightness, 2))
        st.write("Region Contrast:", round(contrast, 2))

        # Final decision
        if brightness > 150 and contrast > 40:
            st.success("Good Reflectivity")
        elif brightness > 100:
            st.warning("Moderate Reflectivity")
        else:
            st.error("Poor Reflectivity")