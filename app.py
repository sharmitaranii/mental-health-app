import streamlit as st
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
