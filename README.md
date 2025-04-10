# 🧠 Mental Health Risk Predictor

A Streamlit web app that predicts whether a person working in tech may be at risk of mental health challenges, based on survey inputs.  
Trained on real industry survey data and optimized for **high recall** to prioritize support over missed cases.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://YOUR-STREAMLIT-APP-LINK)  
_(Replace with your Streamlit Cloud URL after deployment)_

---

## 📊 Project Highlights

- 🔍 **Goal:** Predict risk of mental health issues in the tech industry
- ✅ **Pipeline:** Data cleaned, modeled with Random Forest, SHAP analysis, and threshold tuning
- 🎯 **Threshold-tuned** for real-world recall vs. precision tradeoff
- ⚙️ **Deployed with Streamlit** for instant browser-based predictions

---

## 💻 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- SHAP (optional analysis)
- Git & GitHub

---

## ✨ Features

- Interactive user form
- Tuned probability threshold (not just default 0.5!)
- Predicts risk of mental health struggles
- Clean, responsive UI
- Deployable on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🧠 Model Overview

- **Model used:** RandomForestClassifier (with `RandomizedSearchCV` tuning)
- **Best accuracy:** ~83%
- **Threshold tuned to prioritize recall**
- **Important features:** work_interfere, family_history, benefits, age

---

## 🛠 How to Run Locally

1. **Clone this repo**
   ```bash
   git clone https://github.com/YOUR-USERNAME/mental-health-app.git
   cd mental-health-app
