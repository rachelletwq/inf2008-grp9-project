import streamlit as st
import numpy as np
import joblib  # To load trained model

# Load the trained model and scaler
best_model_loan = joblib.load(r"loan_fraud.pkl")
scaler = joblib.load(r"loan_scaler.pkl")

st.title("Loan Fraud Prediction App")
st.write("Enter the customer's details below to predict if they are likely to commit fraud.")

# Dropdown Mappings
occupation_map = {
    "Accountant": 0, "Architect": 1, "Artist": 2, "Chef": 3, "Clerk": 4, "Designer": 5, "Doctor": 6,
    "Engineer": 7, "Entrepreneur": 8, "Lawyer": 9, "Manager": 10, "Musician": 11, "Retired": 12,
    "Self-employed": 13, "Software Developer": 14, "Student": 15, "Teacher": 16, "Technician": 17, "Unemployed": 18
}

marital_status_map = {"Divorced": 0, "Married": 1, "Single": 2}
residential_status_map = {"Live with Parents": 0, "Own": 1, "Rent": 2}
purpose_map = {"Auto": 0, "Education": 1, "Home": 2, "Medical": 3, "Personal": 4, "Travel": 5}
collateral_map = {"No": 0, "Yes": 1}
application_behavior_map = {"Normal": 0, "Rapid": 1}
location_map = {"Local": 0, "Unusual": 1}
change_behavior_map = {"No": 0, "Yes": 1}
account_activity_map = {"Normal": 0, "Unusual": 1}
payment_behavior_map = {"Defaulted": 0, "Late": 1, "On-time": 2}
blacklists_map = {"No": 0, "Yes": 1}
employment_verification_map = {"Not Verified": 0, "Verified": 1}
past_financial_malpractices_map = {"No": 0, "Yes": 1}
device_info_map = {"Desktop": 0, "Laptop": 1, "Mobile": 2, "Tablet": 3}
social_media_map = {"No": 0, "Yes": 1}
consistency_map = {"Consistent": 0, "Inconsistent": 1}
referral_map = {"Online": 0, "Referral": 1}

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=35)
occupation = st.selectbox("Occupation", list(occupation_map.keys()))
marital_status = st.selectbox("Marital Status", list(marital_status_map.keys()))
dependents = st.number_input("Dependents", min_value=0, max_value=10, value=3)
residential_status = st.selectbox("Residential Status", list(residential_status_map.keys()))
address_duration = st.number_input("Address Duration (years)", min_value=0, max_value=50, value=5)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=750)
income_level = st.number_input("Income Level ($)", min_value=0, value=50000)
loan_amount = st.number_input("Loan Amount Requested ($)", min_value=0, value=100000)
loan_term = st.number_input("Loan Term (months)", min_value=1, max_value=360, value=10)
purpose = st.selectbox("Purpose of Loan", list(purpose_map.keys()))
collateral = st.selectbox("Collateral", list(collateral_map.keys()))
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=50.0, value=6.5)
previous_loans = st.number_input("Previous Loans", min_value=0, value=2)
existing_liabilities = st.number_input("Existing Liabilities", min_value=0, value=1)
application_behavior = st.selectbox("Application Behavior", list(application_behavior_map.keys()))
location_of_application = st.selectbox("Location of Application", list(location_map.keys()))
change_in_behavior = st.selectbox("Change in Behavior", list(change_behavior_map.keys()))
account_activity = st.selectbox("Account Activity", list(account_activity_map.keys()))
payment_behavior = st.selectbox("Payment Behavior", list(payment_behavior_map.keys()))
blacklists = st.selectbox("Blacklists", list(blacklists_map.keys()))
employment_verification = st.selectbox("Employment Verification", list(employment_verification_map.keys()))
past_financial_malpractices = st.selectbox("Past Financial Malpractices", list(past_financial_malpractices_map.keys()))
device_information = st.selectbox("Device Information", list(device_info_map.keys()))
social_media_footprint = st.selectbox("Social Media Footprint", list(social_media_map.keys()))
consistency_in_data = st.selectbox("Consistency in Data", list(consistency_map.keys()))
referral = st.selectbox("Referral", list(referral_map.keys()))
time_category = st.selectbox("Time Category", [0, 1, 2])  # No mapping given, keeping as numeric

# Convert inputs to numerical values
loanCustomer_info = np.array([[
    age, occupation_map[occupation], marital_status_map[marital_status], dependents, residential_status_map[residential_status],
    address_duration, credit_score, income_level, loan_amount, loan_term, purpose_map[purpose], collateral_map[collateral],
    interest_rate, previous_loans, existing_liabilities, application_behavior_map[application_behavior],
    location_map[location_of_application], change_behavior_map[change_in_behavior], account_activity_map[account_activity],
    payment_behavior_map[payment_behavior], blacklists_map[blacklists], employment_verification_map[employment_verification],
    past_financial_malpractices_map[past_financial_malpractices], device_info_map[device_information], 
    social_media_map[social_media_footprint], consistency_map[consistency_in_data], referral_map[referral], time_category
]])

# Scale input data
loanCustomer_info_scaled = scaler.transform(loanCustomer_info)

# Prediction Button
if st.button("Predict Fraud Risk"):
    predictedFraud = best_model_loan.predict(loanCustomer_info_scaled)
    result = "Fraud" if predictedFraud[0] == 1 else "Not Fraud"
    st.subheader(f"Prediction: {result}")
