import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Load your custom model for COVID, NORMAL, PNEUMONIA classification
model = tf.keras.models.load_model(r"C:\Users\Harshali\ds\Disease Recognition\artifacts\training/model.h5")

# Set page title and icon
st.set_page_config(page_title="Disease Recognition (Chest X-ray Classifier)", page_icon="🩺")

# Page heading with a colorful background
st.title("Disease Recognition [Chest X-ray Classifier]")
st.markdown(
    """
    <style>
        .big-font {
            font-size: 3rem !important;
        }
        .colorful-text {
            color: #e44d26;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# File upload section
uploaded_file = st.file_uploader("Choose a chest X-ray image", type=["jpg", "jpeg", "png"])

# Function to make predictions
def make_prediction(model, image):
    img_array = np.array(image.resize((224, 224)))
    img_array = np.expand_dims(img_array, axis=0)  # [batch_size, row, col, channel]
    predictions = model.predict(img_array)
    return predictions

# Display predictions and image
if uploaded_file is not None:
    # Read the image file
    image = Image.open(uploaded_file)

    # Make predictions
    predictions = make_prediction(model, image)

    # Map the predictions to class labels
    class_labels = ["COVID", "NORMAL", "PNEUMONIA"]
    predicted_class = class_labels[np.argmax(predictions)]
    confidence_level = np.max(predictions)

    # Color-coded confidence level
    confidence_color = "green" if confidence_level > 0.5 else "red"

    # Display the result in a nice layout
    st.image(image, caption=f"Predicted: {predicted_class}", use_column_width=True)
    st.markdown(f"## Prediction: **<span class='colorful-text'>{predicted_class}</span>**", unsafe_allow_html=True)
    st.write(f"Confidence Level: <span style='color:{confidence_color}; font-weight:bold;'>{confidence_level:.2%}</span>", unsafe_allow_html=True)

    # Display individual class probabilities with colors
    st.write("Prediction Probabilities:")
    for i, label in enumerate(class_labels):
        probability_color = f"color: {'green' if predictions[0][i] > 0.5 else 'red'}"
        st.write(f"<span style='{probability_color}; font-weight:bold;'>{label}:</span> {predictions[0][i]:.2%}", unsafe_allow_html=True)
#     add