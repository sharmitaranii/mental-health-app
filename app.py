import streamlit as st
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
