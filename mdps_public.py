# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 19:37:16 2024

@author: user
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Custom CSS for styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f0f5;
    }
    .title {
        text-align: center;
        color: #4A90E2;
        font-size: 2em;
        margin-bottom: 20px;
    }
    .input-container {
        background: #fff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .result {
        font-size: 1.5em;
        font-weight: bold;
        color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Function to create input fields in a styled container
def create_input_container(title, fields):
    st.markdown(f"<div class='input-container'><h3>{title}</h3>", unsafe_allow_html=True)
    cols = st.columns(len(fields))
    for col, (label, key) in zip(cols, fields.items()):
        with col:
            st.text_input(label, key=key)
    st.markdown("</div>", unsafe_allow_html=True)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.markdown("<h1 class='title'>Diabetes Prediction using Machine Learning</h1>", unsafe_allow_html=True)
    fields = {
        'Number of Pregnancies': 'pregnancies',
        'Glucose Level': 'glucose',
        'Blood Pressure': 'blood_pressure',
        'Skin Thickness': 'skin_thickness',
        'Insulin Level': 'insulin',
        'BMI': 'bmi',
        'Diabetes Pedigree Function': 'diabetes_pedigree',
        'Age': 'age'
    }
    create_input_container("Input Data", fields)

    if st.button('Diabetes Test Result'):
        user_input = [st.session_state[key] for key in fields.values()]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        result = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.markdown(f"<p class='result'>{result}</p>", unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.markdown("<h1 class='title'>Heart Disease Prediction using Machine Learning</h1>", unsafe_allow_html=True)
    fields = {
        'Age': 'age',
        'Sex': 'sex',
        'Chest Pain Type': 'chest_pain',
        'Resting Blood Pressure': 'resting_bp',
        'Cholesterol': 'cholesterol',
        'Fasting Blood Sugar': 'fasting_bs',
        'Resting ECG Results': 'rest_ecg',
        'Max Heart Rate': 'max_hr',
        'Exercise Angina': 'exercise_angina',
        'Oldpeak': 'oldpeak',
        'Slope': 'slope',
        'Major Vessels': 'major_vessels',
        'Thal': 'thal'
    }
    create_input_container("Input Data", fields)

    if st.button('Heart Disease Test Result'):
        user_input = [st.session_state[key] for key in fields.values()]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        result = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
        st.markdown(f"<p class='result'>{result}</p>", unsafe_allow_html=True)

# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":
    st.markdown("<h1 class='title'>Parkinson's Disease Prediction using Machine Learning</h1>", unsafe_allow_html=True)
    fields = {
        'MDVP:Fo(Hz)': 'fo',
        'MDVP:Fhi(Hz)': 'fhi',
        'MDVP:Flo(Hz)': 'flo',
        'MDVP:Jitter(%)': 'jitter_percent',
        'MDVP:Jitter(Abs)': 'jitter_abs',
        'MDVP:RAP': 'rap',
        'MDVP:PPQ': 'ppq',
        'Jitter:DDP': 'jitter_ddp',
        'MDVP:Shimmer': 'shimmer',
        'MDVP:Shimmer(dB)': 'shimmer_db',
        'Shimmer:APQ3': 'apq3',
        'Shimmer:APQ5': 'apq5',
        'MDVP:APQ': 'apq',
        'Shimmer:DDA': 'dda',
        'NHR': 'nhr',
        'HNR': 'hnr',
        'RPDE': 'rpde',
        'DFA': 'dfa',
        'spread1': 'spread1',
        'spread2': 'spread2',
        'D2': 'd2',
        'PPE': 'ppe'
    }
    create_input_container("Input Data", fields)

    if st.button("Parkinson's Test Result"):
        user_input = [st.session_state[key] for key in fields.values()]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        result = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.markdown(f"<p class='result'>{result}</p>", unsafe_allow_html=True)

