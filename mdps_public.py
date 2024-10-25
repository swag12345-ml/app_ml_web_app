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
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', "Parkinson's Prediction"],
                           menu_icon='hospital-fill', 
                           icons=['activity', 'heart', 'person'], 
                           default_index=0)

# Set page title and layout
st.set_page_config(page_title="Disease Prediction System", layout="wide")

# Define a function for a custom header
def custom_header(title):
    st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{title}</h1>", unsafe_allow_html=True)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    custom_header('Diabetes Prediction using Machine Learning')

    # Input fields in a stylish format
    input_data = {
        "Number of Pregnancies": st.number_input('Number of Pregnancies', min_value=0),
        "Glucose Level": st.number_input('Glucose Level', min_value=0),
        "Blood Pressure": st.number_input('Blood Pressure value', min_value=0),
        "Skin Thickness": st.number_input('Skin Thickness value', min_value=0),
        "Insulin Level": st.number_input('Insulin Level', min_value=0),
        "BMI": st.number_input('BMI value', min_value=0.0),
        "Diabetes Pedigree Function": st.number_input('Diabetes Pedigree Function value', min_value=0.0),
        "Age of the Person": st.number_input('Age of the Person', min_value=0),
    }

    if st.button('Diabetes Test Result'):
        user_input = [float(value) for value in input_data.values()]
        diab_prediction = diabetes_model.predict([user_input])
        result = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(result)

# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    custom_header('Heart Disease Prediction using Machine Learning')

    # Input fields in a stylish format
    heart_input_data = {
        "Age": st.number_input('Age'),
        "Sex": st.selectbox('Sex', [0, 1]),  # 0: Female, 1: Male
        "Chest Pain Type": st.selectbox('Chest Pain types', range(0, 4)),  # assuming 0-3 types
        "Resting Blood Pressure": st.number_input('Resting Blood Pressure'),
        "Serum Cholesterol": st.number_input('Serum Cholestoral in mg/dl'),
        "Fasting Blood Sugar": st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1]),  # 0: False, 1: True
        "Resting ECG Results": st.selectbox('Resting Electrocardiographic results', range(0, 3)),
        "Max Heart Rate Achieved": st.number_input('Maximum Heart Rate achieved'),
        "Exercise Induced Angina": st.selectbox('Exercise Induced Angina', [0, 1]),  # 0: No, 1: Yes
        "ST Depression": st.number_input('ST depression induced by exercise'),
        "Slope of ST Segment": st.selectbox('Slope of the peak exercise ST segment', range(0, 3)),
        "Major Vessels Colored": st.number_input('Major vessels colored by fluoroscopy', min_value=0),
        "Thal": st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', [0, 1, 2]),
    }

    if st.button('Heart Disease Test Result'):
        user_input = [float(value) for value in heart_input_data.values()]
        heart_prediction = heart_disease_model.predict([user_input])
        result = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(result)

# Parkinson's Prediction Page
elif selected == "Parkinson's Prediction":
    custom_header("Parkinson's Disease Prediction using ML")

    # Input fields in a stylish format
    parkinsons_input_data = {
        "MDVP:Fo(Hz)": st.number_input('MDVP:Fo(Hz)'),
        "MDVP:Fhi(Hz)": st.number_input('MDVP:Fhi(Hz)'),
        "MDVP:Flo(Hz)": st.number_input('MDVP:Flo(Hz)'),
        "MDVP:Jitter(%)": st.number_input('MDVP:Jitter(%)'),
        "MDVP:Jitter(Abs)": st.number_input('MDVP:Jitter(Abs)'),
        "MDVP:RAP": st.number_input('MDVP:RAP'),
        "MDVP:PPQ": st.number_input('MDVP:PPQ'),
        "Jitter:DDP": st.number_input('Jitter:DDP'),
        "MDVP:Shimmer": st.number_input('MDVP:Shimmer'),
        "MDVP:Shimmer(dB)": st.number_input('MDVP:Shimmer(dB)'),
        "Shimmer:APQ3": st.number_input('Shimmer:APQ3'),
        "Shimmer:APQ5": st.number_input('Shimmer:APQ5'),
        "MDVP:APQ": st.number_input('MDVP:APQ'),
        "Shimmer:DDA": st.number_input('Shimmer:DDA'),
        "NHR": st.number_input('NHR'),
        "HNR": st.number_input('HNR'),
        "RPDE": st.number_input('RPDE'),
        "DFA": st.number_input('DFA'),
        "spread1": st.number_input('spread1'),
        "spread2": st.number_input('spread2'),
        "D2": st.number_input('D2'),
        "PPE": st.number_input('PPE'),
    }

    if st.button("Parkinson's Test Result"):
        user_input = [float(value) for value in parkinsons_input_data.values()]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        result = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(result)
