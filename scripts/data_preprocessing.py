import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('data/churn_data.csv')

print(df.isnull().sum())

def preprocess_data(data_path):
    
    # Load the dataset
    df = pd.read_csv(data_path)

    # Drop missing values if they total 15% or less of the total rows
    df = df.dropna(thresh= int(len(df) * .15))

    # Convert binary categorical columns to numerical
    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']
    label_encoder = LabelEncoder()
    for col in binary_cols:
        df[col] = label_encoder.fit_transform(df[col])

    # Convert other categorical columns to dummy variables
    categorical_cols = ['InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                        'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Split the data into features (X) and target variable (y)
    X = df.drop(['customerID', 'Churn'], axis=1)
    y = df['Churn']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardize numerical features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    data_path = "churn_data.csv"
    X_train, X_test, y_train, y_test = preprocess_data(data_path)