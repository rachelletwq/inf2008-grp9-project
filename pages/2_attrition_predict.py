import streamlit as st
import numpy as np
import joblib  # To load trained model

# Load the trained model and scaler
best_model_attr = joblib.load(r"CreditCard_Attr.pkl")
scaler = joblib.load(r"credit_scaler.pkl")

st.title("Credit Card Attrition Prediction App")
st.write("Enter the customer's details below to predict their attrition risk.")

# Dropdown Mappings
gender_map = {"Female": 0, "Male": 1}
education_level_map = {"College": 0, "Doctorate": 1, "Graduate": 2, "High School": 3, "Post Graduate": 4, "Uneducated": 5}
marital_status_map = {"Divorced": 0, "Married": 1, "Single": 2}
income_category_map = {"$120K+": 0, "$40K - $60K": 1, "$60K - $80K": 2, "$80K - $120K": 3, "Less than $40K": 4}
card_category_map = {"Blue": 0, "Gold": 1, "Platinum": 2, "Silver": 3}
total_revolving_bal_range_map = {"500": 8, "1000": 7, "1500": 6, "2000": 5, "2500": 4, "3000": 3, "3500": 2, "4000": 1}
avg_open_to_buy_range_map = {"5000": 8, "10000": 7, "15000": 6, "20000": 5, "25000": 4, "30000": 3, "35000": 2, "40000": 1}

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=35)
gender = st.selectbox("Gender", list(gender_map.keys()))
dependent_count = st.number_input("Dependent Count", min_value=0, max_value=10, value=3)
education_level = st.selectbox("Education Level", list(education_level_map.keys()))
marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()))
income_category = st.selectbox("Income Category", list(income_category_map.keys()))
card_category = st.selectbox("Card Category", list(card_category_map.keys()))
months_on_book = st.number_input("Months On Book", min_value=0, max_value=99, value=24)
total_relationship_count = st.number_input("Total Relationship Count", min_value=0, max_value=10, value=3)
months_inactive_12_mon = st.number_input("Inactive Months (12M)", min_value=0, max_value=12, value=1)
contacts_count_12_mon = st.number_input("Contacts Count (12M)", min_value=0, max_value=12, value=3)
credit_limit = st.number_input("Credit Limit", min_value=0, max_value=100000, value=12000)
total_revolving_bal = st.number_input("Total Revolving Balance", min_value=0, max_value=10000, value=2000)
avg_open_to_buy = st.number_input("Average Open To Buy", min_value=0, max_value=100000, value=10000)
total_amt_chg = st.number_input("Total Amount Change (Q4 to Q1)", min_value=0.0, max_value=12.0, value=1.5)
total_trans_amt = st.number_input("Total Transaction Amount", min_value=0, max_value=100000, value=5000)
total_trans_ct = st.number_input("Total Transaction Count", min_value=0, max_value=1000, value=50)
total_ct_chg = st.number_input("Total Transaction Count Change (Q4 to Q1)", min_value=0.0, max_value=12.0, value=1.2)
avg_utilization_ratio = st.number_input("Average Utilization Ratio", min_value=0.0, max_value=1.0, value=0.35)
income = st.number_input("Income", min_value=0, max_value=500000, value=75000)
percentage_expenditure = st.number_input("Expenditure Percentage", min_value=0.0, max_value=500000.0, value=0.25)
avg_spent_per_trans = st.number_input("Average Spent Per Transaction", min_value=0, max_value=1000, value=120)
total_revolving_bal_range = st.selectbox("Total Revolving Balance Range", list(total_revolving_bal_range_map.keys()))
avg_open_to_buy_range = st.selectbox("Average Open To Buy Range", list(avg_open_to_buy_range_map.keys()))
pseudo_credit_score = st.number_input("Pseudo Credit Score", min_value=0.0, max_value=10000.0, value=720.5)

# Convert inputs to numerical values
cc_customer_info = np.array([[
    age, gender_map[gender], dependent_count, education_level_map[education_level], marital_status_map[marital_status], 
    income_category_map[income_category], card_category_map[card_category], months_on_book, total_relationship_count, 
    months_inactive_12_mon, contacts_count_12_mon, credit_limit, total_revolving_bal, avg_open_to_buy, total_amt_chg, 
    total_trans_amt, total_trans_ct, total_ct_chg, avg_utilization_ratio, income, percentage_expenditure, avg_spent_per_trans, 
    total_revolving_bal_range_map[total_revolving_bal_range], avg_open_to_buy_range_map[avg_open_to_buy_range], pseudo_credit_score
]])

# Scale input data
cc_customer_info_scaled = scaler.transform(cc_customer_info)

# Prediction Button
if st.button("Predict Customer Attrition"):
    predictedAttrition = best_model_attr.predict(cc_customer_info_scaled)
    result = "Attrited" if predictedAttrition[0] == 0 else "Not Attrited"
    st.subheader(f"Customer is Predicted to be: {result}")