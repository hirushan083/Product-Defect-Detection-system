# Product Defect Detection Web App

A **Convolutional Neural Network (CNN)** based web application for detecting defects in manufactured products.  
The application allows users to upload images of products and instantly determine whether they are **Defective** or **Non-Defective**.

This project demonstrates the complete workflow of a deep learning-based computer vision system

* Data preprocessing
* CNN model training
* Performance evaluation
* Deployment as a web app for real-time inference

## 🧠 Features

 * Binary classification**: Defective / Non-Defective
 * Image preprocessing**: Resizing, normalization
 * Real-time predictions** via Streamlit web interface
 * Confidence score** displayed with each prediction
 * Lightweight deployment** using Google Drive hosted model to avoid GitHub file size limits
 * Visualization** of uploaded images in the web app

## 🚀 Tech Stack

| Component          | Technology / Library |
|-------------------|-------------------|
| Deep Learning Model | TensorFlow / Keras CNN |
| Web App Frontend    | Streamlit |
| Image Processing    | Pillow, NumPy |
| Model Hosting       | Google Drive (for `.h5` model) |
| Version Control     | GitHub |
| Deployment          | Streamlit Community Cloud |


## 📁 Project Structure

defect_detection_webapp/

* app.py           # Streamlit web app code
* requirements.txt # Python dependencies
* README.md        # Project documentation

**Note:** The trained model file (`.h5`) is **hosted externally** via Google Drive and automatically

* Install dependencies

      pip install -r requirements.txt

* Run the app locally

      streamlit run app.py

* Open the URL shown in the terminal (usually http://localhost:8501)

* Upload a product image to get predictions (casting_data file in the dataset)

🌐 Deployment

The app is deployed on Streamlit Community Cloud:
[Your Streamlit App Link Here](https://defect-det-system.streamlit.app/)

The trained model is automatically downloaded from Google Drive on first launch.

🔧 How It Works

* Upload Image: User uploads a product image via the web interface.
* Preprocessing: Image resized to 224x224 pixels and normalized.
* Prediction: CNN model predicts defect status and computes confidence.
* Result Display: Shows Defective / Non-Defective with confidence percentage.

📊 Model Performance

Trained on Casting Product Dataset from Kaggle:
[Kaggle Dataset Link](https://www.kaggle.com/datasets/ravirajsinh45/casting-product-image-data-for-quality-inspection)
CNN achieved high accuracy for binary defect detection (can add metrics here if available).

💡 Future Improvements

* Use Transfer Learning with ResNet or EfficientNet for higher accuracy
* Add batch image testing
* Add dashboard for model performance visualization
* Optimize model using TensorFlow Lite for edge deployment
* Real-time camera input support

📄 References

* Kaggle Dataset:[Casting Product Image Data](https://www.kaggle.com/datasets/ravirajsinh45/casting-product-image-data-for-quality-inspection)
* TensorFlow / Keras Documentation: https://www.tensorflow.org/
* Streamlit Documentation: https://docs.streamlit.io/

👨‍💻 Author

Name – Kavindu hirushan (Electrical & Electronics Engineering Student)

* Email: kavinduhirushan083@gmail.com
* GitHub: https://github.com/hirushan083
