# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 00:26:20 2024

@author: Precision
"""

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('C:/Users/Precision/Desktop/Diabetes_Prediction/trained_model.sav', 'rb'))

# Function for Diabetes Prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return '🎉 The person is **not diabetic**.', 'success'
    else:
        return '⚠️ The person is **diabetic**.', 'danger'

# Main function for Streamlit app
def main():
    # Streamlit Page Configurations
    st.set_page_config(page_title="Diabetes Prediction App", page_icon="🩺", layout="centered")
    
    # Custom CSS for styling and animation
    st.markdown("""
        <style>
            .title {
                text-align: center;
                font-size: 2.8rem;
                color: white;
            }
            .result-success {
                background-color: #D4EDDA;
                color: #155724;
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                font-size: 1.2rem;
                animation: fadeIn 2s;
            }
            .result-danger {
                background-color: #F8D7DA;
                color: #721C24;
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                font-size: 1.2rem;
                animation: blink 1.5s infinite;
            }
            @keyframes blink {
                0% {opacity: 1;}
                50% {opacity: 0.5;}
                100% {opacity: 1;}
            }
            @keyframes fadeIn {
                from {opacity: 0;}
                to {opacity: 1;}
            }
        </style>
    """, unsafe_allow_html=True)
    
    # App Title
    st.markdown('<div class="title">🩺 Diabetes Prediction Web App</div>', unsafe_allow_html=True)

    # Sidebar for Inputs
    st.sidebar.title("🔧 Input Features")
    st.sidebar.write("Please provide the following details:")

    Pregnancies = st.sidebar.number_input('Number of Pregnancies', min_value=0, step=1)
    Glucose = st.sidebar.number_input('Glucose Level', min_value=0)
    BloodPressure = st.sidebar.number_input('Blood Pressure value', min_value=0)
    SkinThickness = st.sidebar.number_input('Skin Thickness value', min_value=0)
    Insulin = st.sidebar.number_input('Insulin Level', min_value=0)
    BMI = st.sidebar.number_input('BMI value', min_value=0.0, format="%.2f")
    DiabetesPedigreeFunction = st.sidebar.number_input('Diabetes Pedigree Function value', min_value=0.0, format="%.3f")
    Age = st.sidebar.number_input('Age of the Person', min_value=0, step=1)
    
    # Code for Prediction
    diagnosis = ''
    alert_type = 'success'

    # Main Section for Results
    st.write("## Prediction Results")
    if st.sidebar.button('🧪 Get Diabetes Test Result'):
        # Run the prediction
        diagnosis, alert_type = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        # Display results attractively
        if alert_type == 'success':
            st.markdown(f'<div class="result-success">{diagnosis}</div>', unsafe_allow_html=True)
            st.balloons()  # Show balloons for non-diabetic cases
        else:
            st.markdown(f'<div class="result-danger">{diagnosis}</div>', unsafe_allow_html=True)
            st.error("⚠️ **Warning: High Risk Detected! Please consult a doctor immediately.**")

if __name__ == '__main__':
    main()
