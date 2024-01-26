import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Load your custom model for COVID, NORMAL, PNEUMONIA classification

#model = tf.keras.models.load_model(r"C:\Users\Harshali\ds\Disease Recognition\artifacts\training/model.h5")

 model = tf.keras.models.load_model(r"C:\Users\Harshali\Downloads\Disease_Recognition\model\model.h5")
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
        .prediction-container {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .upload-section {
            background-color: #fafafa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .upload-header {
            font-size: 1.5rem;
            color: #333;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# File upload section
with st.container():
    st.markdown("<h2 class='upload-header'>Upload a Chest X-ray Image</h2>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Drag and drop file here\nLimit 200MB per file • JPG, JPEG, PNG", type=["jpg", "jpeg", "png"], key="file-upload")

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

    # Color-coded confidence level
    confidence_color = "green" if np.max(predictions) > 0.5 else "red"

    # Display the result in a nice layout
    st.image(image, caption=f"Predicted: {predicted_class}", use_column_width=True)
    
    # Prediction container with background color
    with st.container():
        st.markdown(f"## Prediction: **<span class='colorful-text'>{predicted_class}</span>**", unsafe_allow_html=True)
        st.write(f"Confidence Level: <span style='color:{confidence_color}; font-weight:bold;'>{np.max(predictions):.2%}</span>", unsafe_allow_html=True)


# add##