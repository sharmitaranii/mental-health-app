# 🧠 Mental Health Treatment Predictor

This is a Streamlit web application that predicts whether a person is likely to seek mental health treatment based on workplace and personal factors. It uses a machine learning model trained on survey data related to mental health in the tech industry.

 Live App: [Click to view the app](https://mental-health-app-zqzwenvb2crazdbwvc6bon.streamlit.app/)

 Colab Notebook: [Exploratory Data Analysis](https://colab.research.google.com/drive/1-caJDOKOnJQ10irVeaRKtCirz5fCGxUc?usp=sharing)

# Project Overview
Mental health is a critical aspect often overlooked in workplace environments, especially in the tech industry. This application aims to assess whether an individual is likely to seek treatment for mental health issues based on their responses to key personal and work-related questions.

# Features
 - Interactive Streamlit web application

 - Predictive modeling using machine learning algorithms

 - User-friendly interface for inputting personal and workplace factors

 - Real-time prediction of mental health treatment likelihood

# Dataset
The dataset used is the Mental Health in Tech Survey from Kaggle, which includes responses from tech professionals regarding their mental health and workplace environment.
 Kaggle Dataset link:  https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey

# Exploratory Data Analysis
A comprehensive EDA was conducted to understand the data distribution, identify missing values, and explore relationships between variables. Key steps included:

   - Data cleaning and preprocessing

   - Visualization of categorical and numerical features

   - Correlation analysis

    For detailed analysis, refer to the Colab Notebook.

# Modeling
Several machine learning models were evaluated, including:

  -Logistic Regression

  -Random Forest Classifier

  -Support Vector Machine

The Random Forest Classifier was selected based on its superior performance metrics. Hyperparameter tuning was performed using GridSearchCV to optimize model performance.

# Deployment
The final model was deployed using Streamlit, providing an accessible web interface for users to input their information and receive predictions regarding their likelihood of seeking mental health treatment.

# Installation
To run the application locally:
- Clone the repository:
  git clone https://github.com/sharmitaranii/mental-health-app.git

- Navigate to the project directory:
  cd mental-health-app

- Install the required packages:
  pip install -r requirements.txt

- Run the Streamlit application:
  streamlit run app.py

# Usage
Upon running the application, a web interface will open where users can input various personal and workplace-related factors. After submitting the information, the application will display the prediction regarding the likelihood of seeking mental health treatment.

# Results
The Random Forest model achieved the following performance metrics:

Accuracy: 85%

Precision: 82%

Recall: 80%

F1-Score: 81%

These metrics indicate a robust model capable of providing reliable predictions.

# Future Work
Incorporate additional features to improve model accuracy

Implement user authentication for personalized experiences

Expand the dataset to include more diverse demographics

Integrate feedback mechanisms for continuous improvement

# Author
  Sharmita Rani
  LinkedIn: https://www.linkedin.com/in/sharmitarani/
