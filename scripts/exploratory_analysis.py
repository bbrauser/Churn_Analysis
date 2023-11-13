import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data/churn_data.csv')

# Changing TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display summary statistics of numerical features
print("\nSummary Statistics:")
print(df.describe())

# Visualize the distribution of the target variable (Churn)
plt.figure(figsize=(8, 5))
sns.countplot(x='Churn', data=df, hue='Churn', palette='viridis', legend=False)
plt.title('Distribution of Churn')

# Visualize the distribution of categorical variables
categorical_columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines',
                        'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']

plt.figure(figsize=(15, 15))
for i, column in enumerate(categorical_columns, 1):
    ax = plt.subplot(4, 4, i)
    sns.countplot(x=column, data=df, hue='Churn', palette='Set2', legend=False, ax=ax)
    plt.title(f'Distribution of {column}')
    plt.xticks(rotation=45)

# Visualize the correlation matrix (excluding non-numeric columns)
corr_numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[corr_numerical_columns].corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')

# Visualize the distribution of numerical features
dist_numerical_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']

plt.figure(figsize=(15, 5))
for i, column in enumerate(dist_numerical_columns, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[column], bins=20, kde=True, color='skyblue')
    plt.title(f'Distribution of {column}')

plt.tight_layout()
plt.show()