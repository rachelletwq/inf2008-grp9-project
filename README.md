# Integrated Smart Bank System
This project leverages machine learning to enhance banking operations, providing predictive insights for fraud detection, credit card attrition analysis, and a credit card recommendation system. Built with Streamlit, it offers an all-in-one interactive interface where users can select features to use, input relevant data, and receive real-time predictions.


# Introduction
This Integrated Smart Bank System is designed to assit finanical institution in banking analysis and risk mitigations through machine learning. The system consists of the following features:

1. Loan Fraud Detection 
   - Identifies fraudulent loan applications to minimize financial losses.

2. Credit Card Attrition Prediction 
   - Helps banks anticipate customer churn, allowing proactive retention strategies to reduce revenue loss.
   
3. Credit Card Recommendation system
   - Recommends most suitable credit cards for customers 

These are features which would align with a bank's interest considering that loan frauds could harm a bank's reputation as a financial institution and its finances as well. Having the credit card features would also help aid bank staffs in identifying potential customers who will attrite so they are able to make better informed decisions to retain their customers and also for new customers, they are able to make use of certain parameters which are usually used in determining a customer's credit card tier.


# Datasets

This system consists two primary datasets:

1. account_data.csv - Used for Loan Fraud Detection

2. BankChurners.csv - Used for Credit Card Attrition Predictions

## Data Sources

1. account_data.csv: https://www.kaggle.com/datasets/whenamancodes/credit-card-customers-prediction

2. BankChurners.csv: https://www.kaggle.com/datasets/ayushkumarnamdeo/dataset-for-bank-loan-fraud-detection-system?select=account_data.csv

# How to Run the Jupter Notebook
### Install Required Dependencies
To start, the first step in running the python kernel file which all the codes are in, please ensure that all the different libraries required are installed with the following command:
```bash
pip install -r requirements.txt
```
### Required Data Files

This system consists two primary datasets:

1. account_data.csv - Used for Loan Fraud Detection

2. BankChurners.csv - Used for Credit Card Attrition Predictions

Ensure these files are present in the same directory as the Python kernel file

### Running the Jupyter Notebook
To run the system, open a IDE (Visual Studio Code, Jupyter Notebook) of your choice, load and execute the kernel file.


# How to Launch the GUI
This project GUI provides the following features:

1. Loan Fraud Detection 
   - Detect fraudulent transactions based on historical data

2. Credit Card Attrition Prediction 
   - Predict whether a customer is likely to close their account
   
3. Credit Card Recommendation system
   - Suggest suitable credit card tires for new customers 

To use the GUI, please go to the file directory where the app.py file is and run the following command in your Command Line Interface (CLI) such as command prompt (CMD) or PowerShell (PS):
```bash
streamlit run app.py
```


# Feature Engineering
To enhance predictive accuracy, several key **feature engineering** techniques were applied to the datasets:

### **Data Preprocessing Steps**
- **Handling Missing Values** – All missing values were removed to maintain data integrity.
- **Categorical Encoding** – Categorical features were transformed into numerical representations using **Label Encoding**.
- **Feature Selection** – Irrelevant columns such as `TimeofTransaction` were excluded to avoid data redundancy.
- **Data Transformation** – Selected categorical columns were encoded using **One-Hot Encoding** to enhance machine learning compatibility.

### **Numerical Features**
| Feature | Description |
|---------|-------------|
| **Transaction Amount** | Total amount spent per transaction |
| **Account Age** | Duration since account creation (in years) |
| **Number of Transactions** | Total number of transactions in a given period |
| **Credit Score** | Customer’s creditworthiness rating |
| **Loan-to-Income Ratio** | Ratio of loan amount to income, indicating risk level |

### **Categorical Features**
| Feature | Description |
|---------|-------------|
| **Card Type** | Type of credit card used (Gold, Platinum, etc.) |
| **Transaction Category** | Classification of transaction types (Retail, Travel, Food, etc.) |
| **Fraud Label** | Indicates if a transaction was fraudulent |

### **Derived Features**
- **Transaction Frequency** – Tracks the number of transactions over different time windows.
- **Spending Pattern Score** – Assigns a score based on spending behavior.
- **Recent Large Transactions** – Identifies if a customer has made unusually large purchases recently.
- **Average Transaction Size** – Computes the mean transaction value for each customer.

Feature engineering enhances model performance by extracting **meaningful patterns** from raw data, enabling more accurate predictions for fraud detection, attrition analysis, and credit card recommendations.

---

# Why This Project Matters
Fraudulent activities and customer attrition pose significant risks to financial institutions. This system helps banks:

**Reduce Fraudulent Transactions** – Identifies fraud patterns early.  
**Improve Customer Retention** – Predicts and prevents customer churn.  
**Enhance Decision-Making** – Provides valuable insights for financial analysis.  

# References for Project:
account_data.csv: https://www.kaggle.com/datasets/whenamancodes/credit-card-customers-prediction
BankChurners.csv: https://www.kaggle.com/datasets/ayushkumarnamdeo/dataset-for-bank-loan-fraud-detection-system?select=account_data.csv
