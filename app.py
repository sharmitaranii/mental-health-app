import streamlit as st
<<<<<<< HEAD
import joblib
import pandas as pd

# Load model
model = joblib.load('model.pkl')

st.title("Mental Health Treatment Predictor")
st.write("This app predicts whether a person is likely to seek mental health treatment based on workplace and personal factors.")

# Define input fields
age = st.number_input("Age", 15, 100, 30)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
self_employed = st.selectbox("Self-employed", ["Yes", "No"])
family_history = st.selectbox("Family history of mental illness", ["Yes", "No"])
remote_work = st.selectbox("Remote work allowed?", ["Yes", "No"])
tech_company = st.selectbox("Works in tech company?", ["Yes", "No"])
benefits = st.selectbox("Mental health benefits?", ["Yes", "No", "Don't know"])
care_options = st.selectbox("Care options provided?", ["Yes", "No", "Not sure"])
wellness_program = st.selectbox("Wellness program?", ["Yes", "No", "Don't know"])
seek_help = st.selectbox("Resources to seek help?", ["Yes", "No", "Don't know"])
anonymity = st.selectbox("Anonymity guaranteed?", ["Yes", "No", "Don't know"])
leave = st.selectbox("Ease of taking mental health leave", ["Very easy", "Somewhat easy", "Somewhat difficult", "Very difficult", "Don't know"])
mental_health_consequence = st.selectbox("Mental health consequence if discussed?", ["Yes", "No", "Maybe"])
phys_health_consequence = st.selectbox("Physical health consequence if discussed?", ["Yes", "No", "Maybe"])
coworkers = st.selectbox("Willing to discuss with coworkers?", ["Yes", "No", "Some of them"])
supervisor = st.selectbox("Willing to discuss with supervisor?", ["Yes", "No", "Some of them"])
mental_health_interview = st.selectbox("Discuss mental health in interview?", ["Yes", "No", "Maybe"])
phys_health_interview = st.selectbox("Discuss physical health in interview?", ["Yes", "No", "Maybe"])
mental_vs_physical = st.selectbox("Mental vs Physical support perception", ["Yes", "No", "Don't know"])
obs_consequence = st.selectbox("Seen negative consequence at work?", ["Yes", "No"])
work_interfere = st.selectbox("Does mental health interfere with work?", ["Never", "Rarely", "Sometimes", "Often"])
no_employees = st.selectbox("Company size", ["1-5", "6-25", "26-100", "100-500", "500-1000", "More than 1000"])
country = st.selectbox("Country", ["United States", "India", "United Kingdom", "Canada", "Germany", "Other"])
age_original = age  # For feature matching
gender_cleaned = 0 if gender == "Male" else 1 if gender == "Female" else 2

# Prepare input DataFrame
input_data = pd.DataFrame([{
    'Age': age,
    'Age_original': age_original,
    'Gender_cleaned': gender_cleaned,
    'self_employed': self_employed,
    'remote_work': remote_work,
    'work_interfere': work_interfere,
    'leave': leave,
    'coworkers': coworkers,
    'supervisor': supervisor,
    'mental_health_interview': mental_health_interview,
    'phys_health_interview': phys_health_interview,
    'mental_vs_physical': mental_vs_physical,
    'obs_consequence': obs_consequence,
    'mental_health_consequence': mental_health_consequence,
    'phys_health_consequence': phys_health_consequence,
    'benefits': benefits,
    'care_options': care_options,
    'wellness_program': wellness_program,
    'seek_help': seek_help,
    'anonymity': anonymity,
    'tech_company': tech_company,              
    'no_employees': no_employees,               
    'Country': country                          
}])

# Make prediction
prediction = model.predict(input_data)[0]

# Show result
#st.subheader("Prediction Result:")
#st.write(" Likely to seek treatment" if prediction == "Yes" else " Not likely to seek treatment")git init

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    result = "✅ Likely to seek treatment" if prediction == "Yes" else "❌ Not likely to seek treatment"
    st.subheader("Prediction Result:")
    st.success(result)
=======
import pandas as pd
import numpy as np
import joblib

# Load the trained pipeline and threshold
@st.cache_resource
def load_model():
    model = joblib.load("best_rf_pipeline.pkl")  # File must be in the same folder
    threshold = 0.60  # Tuned threshold
    return model, threshold

model, threshold = load_model()

# Page config
st.set_page_config(page_title="Mental Health Risk Predictor", layout="centered")
st.title("🧠 Mental Health Risk Predictor")
st.markdown("""
This app predicts whether a person in tech may need mental health support based on their responses.  
Threshold-tuned for real-world deployment (⚖️ recall-focused).
""")

# User input form
with st.form("input_form"):
    st.subheader("📋 Fill in the survey:")
    age = st.slider("Age", 18, 65, 30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    family_history = st.selectbox("Family history of mental illness?", ["Yes", "No"])
    work_interfere = st.selectbox("Mental health interferes with work?", ["Never", "Rarely", "Sometimes", "Often"])
    benefits = st.selectbox("Employer provides mental health benefits?", ["Yes", "No", "Don't know"])
    care_options = st.selectbox("Access to mental health resources at work?", ["Not sure", "Some options", "Yes"])
    anonymity = st.selectbox("Is anonymity protected when seeking help?", ["Yes", "No", "Don't know"])
    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    input_df = pd.DataFrame({
        "Age": [age],
        "Gender_cleaned": [gender],
        "family_history": [family_history],
        "work_interfere": [work_interfere],
        "benefits": [benefits],
        "care_options": [care_options],
        "anonymity": [anonymity]
    })

    proba = model.predict_proba(input_df)[0][1]
    prediction = int(proba >= threshold)

    st.subheader("🔎 Prediction Result")
    st.metric("Probability of Mental Health Risk", f"{proba:.2f}")
    if prediction == 1:
        st.error("⚠️ At Risk — Recommend follow-up or support.")
    else:
        st.success("✅ Not currently at risk.")
>>>>>>> 2ddb871f6f4c74ae96b8bfbacfb958d99e1644f4
