import streamlit as st
import numpy as np
import pickle

# Load the trained model from the pickle file
model_pkl_file = "C:\\Users\\sanat\\Downloads\\trained_model.sav"
loaded_model = pickle.load(open(model_pkl_file, 'rb'))

# Streamlit app title and description
st.title("Heart Disease Predictor")
st.write("This app predicts whether a person has heart disease based on various attributes.")

# Input fields for user input
st.sidebar.header("Enter Patient Attributes")

age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1, value=40)
sex = st.sidebar.radio("Sex", ["Male", "Female"])
cp = st.sidebar.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.sidebar.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, step=1, value=120)
chol = st.sidebar.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, step=1, value=200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
restecg = st.sidebar.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T Wave Abnormality", "Probable Ventricular Hypertrophy"])
thalach = st.sidebar.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300, step=1, value=150)
exang = st.sidebar.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.sidebar.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
slope = st.sidebar.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
ca = st.sidebar.number_input("Number of Major Vessels (0-3) Colored by Flourosopy", min_value=0, max_value=3, step=1, value=0)
thal = st.sidebar.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# Create input data array
input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])

# Reshape the input data
input_data = input_data.reshape(1, -1)

# Predict button
if st.sidebar.button("Predict"):
    # Make prediction
    prediction = loaded_model.predict(input_data)

    # Display prediction result
    if prediction[0] == 0:
        st.success("The person is predicted to have heart disease.")
    else:
        st.success("The person is predicted to not have heart disease.")
