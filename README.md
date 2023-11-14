# Churn Analysis Project

## Overview

This project aims to analyze customer churn in a telecommunications company using Python. Churn analysis helps identify factors contributing to customer attrition, allowing businesses to make informed decisions and implement retention strategies.

## Dataset

The dataset (`churn_data.csv`) contains information about customers, including demographics, services subscribed, and churn status.

### Columns

- `customerID`: Customer ID
- `gender`: Gender (Male/Female)
- `SeniorCitizen`: Whether the customer is a senior citizen (1, 0)
- `Partner`: Whether the customer has a partner or not (Yes, No)
- `Dependents`: Whether the customer has dependents or not (Yes, No)
- `tenure`: Number of months the customer has stayed with the company
- `PhoneService`: Whether the customer has a phone service or not (Yes, No)
- `MultipleLines`: Whether the customer has multiple lines or not (Yes, No, No phone service)
- `InternetService`: Customer’s internet service provider (DSL, Fiber optic, No)
- `OnlineSecurity`: Whether the customer has online security or not (Yes, No, No internet service)
- `OnlineBackup`: Whether the customer has online backup or not (Yes, No, No internet service)
- `DeviceProtection`: Whether the customer has device protection or not (Yes, No, No internet service)
- `TechSupport`: Whether the customer has tech support or not (Yes, No, No internet service)
- `StreamingTV`: Whether the customer has streaming TV or not (Yes, No, No internet service)
- `StreamingMovies`: Whether the customer has streaming movies or not (Yes, No, No internet service)
- `Contract`: The contract term of the customer (Month-to-month, One year, Two year)
- `PaperlessBilling`: Whether the customer has paperless billing or not (Yes, No)
- `PaymentMethod`: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
- `MonthlyCharges`: The amount charged to the customer monthly
- `TotalCharges`: The total amount charged to the customer
- `Churn`: Whether the customer churned or not (Yes or No)

## Project Structure

- **data_preprocessing.py**: Python script for data preprocessing.
- **exploratory_analysis.py**: Python script for exploratory data analysis.
- **churn_analysis.ipynb**: Jupyter Notebook answering churn analysis questions.
- **requirements.txt**: List of Python packages and versions.

## Results

- Overall churn rate is 26.54%
- Females churn only slightly more than males (26.92% for females, 26.16% for males)
- Customers who churned stayed for an average of almost 18 months
- The variable that had the most impact on whether or not a customer churn was the type of contract they had. Month-to-month had a churn rate of over 40%, one-years had a little over 10% churn rate, and two-years had less than 5% churn rate
- Customer who had more than one service were about 7% more likely to churn than those who only had one service
- Possibly the most surprising churn factor was Payment Method. Those who paid by electronic check were almost 3x as likely to those who paid by bank transfer, automatic credit card, or mailed check.
- Over 350 people churned within the first month
- People who had fiber optic internet were more than twice as likely than those with DSL and about 5x as likely than those who had no internet to churn.



