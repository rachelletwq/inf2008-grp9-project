# Integrated Smart Bank System

A brief description of what this project does and who it's for
This system is for usage for Bank's to aid with their banking analysis and make use of the various machine learning models as guides for their decisions.

To start, the first step in running the python kernel file which all the codes are in, please ensure that all the different libraries required are installed with the following command:

pip install -r requirements.txt

The kernel file will be loaded with 2 files, account_data.csv which is used for the Loan Fraud Detection and BankChurners.csv.

To use the kernel file, open a IDE (Visual Studio Code, Jupyter Notebook) of your choice

We have also included a Graphical User Interface (GUI) which consists of the following features:
1. Loan Fraud Detection with Input
2. Credit Card Attrition Prediction with Input
3. Credit Card Recommendation System

These are features which would align with a bank's interest considering that loan frauds could harm a bank's reputation as a financial institution and its finances as well. Having the credit card features would also help aid bank staffs in identifying potential customers who will attrite so they are able to make better informed decisions to retain their customers and also for new customers, they are able to make use of certain parameters which are usually used in determining a customer's credit card tier.

To use the GUI, please go to the file directory where the app.py file is and run the following command in your Command Line Interface (CLI) such as command prompt (CMD) or PowerShell (PS):

streamlit -m run app.py


References for Project:
account_data.csv: https://www.kaggle.com/datasets/whenamancodes/credit-card-customers-prediction
BankChurners.csv: https://www.kaggle.com/datasets/ayushkumarnamdeo/dataset-for-bank-loan-fraud-detection-system?select=account_data.csv
