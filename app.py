import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import gdown
import os

# Google Drive model setup
MODEL_URL = "https://drive.google.com/uc?export=download&id=1wD2zAEl6iCkry91W5rAqSalQV_uwnwIX"
MODEL_PATH = "defect_detection_cnn_model.h5"

if not os.path.exists(MODEL_PATH):
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)

# Load model
@st.cache_resource
def load_cnn_model():
    from tensorflow.keras.models import load_model
    return load_model(MODEL_PATH)

model = load_cnn_model()

# App Title
st.title("🔍 Product Defect Detection")
st.write("Upload an image to detect product defects.")

# Upload image
uploaded_file = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    # Prediction
    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.success(f"✅ Non-Defective ({prediction*100:.2f}% confidence)")
    else:
        st.error(f"❌ Defective ({(1-prediction)*100:.2f}% confidence)")
