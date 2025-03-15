import streamlit as st
import numpy as np
import pandas as pd
import joblib  # To load trained model

# Load the trained model
xgb_model = joblib.load(r"Card_Reco_Sys.pkl")

st.title("Credit Card Recommendation System")
st.write("Enter the customer's details below for the system to recommend the most suitable credit card category.")

# Dropdown Mappings
gender_map = {"Female": 0, "Male": 1}
income_category_map = {"$120K+": 0, "$40K - $60K": 1, "$60K - $80K": 2, "$80K - $120K": 3, "Less than $40K": 4}
education_level_map = {"College": 0, "Doctorate": 1, "Graduate": 2, "High School": 3, "Post Graduate": 4, "Uneducated": 5}
card_category_map = {0: "Blue", 1: "Gold", 2: "Platinum", 3: "Silver"}

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=35)
gender = st.selectbox("Gender", list(gender_map.keys()))
income_category = st.selectbox("Income Category", list(income_category_map.keys()))
education_level = st.selectbox("Education Level", list(education_level_map.keys()))
credit_limit = st.number_input("Credit Limit", min_value=0, max_value=10000000, value=50000)

# Convert inputs to numerical values
card_reco_cust_info = pd.DataFrame({
    "Customer_Age": [age],
    "Gender": [gender_map[gender]],
    "Income_Category": [income_category_map[income_category]],
    "Education_Level": [education_level_map[education_level]],
    "Credit_Limit": [credit_limit]
})

# Prediction Button
if st.button("Recommend Credit Card"):
    recommendation = xgb_model.predict(card_reco_cust_info)
    predicted_code = recommendation[0]
    card_category_name = card_category_map.get(predicted_code)
    st.subheader(f"Recommended Card Category: {card_category_name}")