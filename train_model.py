"""
Customer Churn Prediction - Model Training Script
This script loads data, trains models, and saves them for deployment
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

def load_and_preprocess_data():
    """Load and preprocess the customer churn dataset"""
    print("Loading data...")
    
    # Try to load from local file first, then from URL
    try:
        df = pd.read_csv('telco_data.csv')
        print("✓ Loaded data from local file")
    except FileNotFoundError:
        print("Local file not found, downloading from URL...")
        try:
            url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
            df = pd.read_csv(url)
            # Save for future use
            df.to_csv('telco_data.csv', index=False)
            print("✓ Downloaded and saved data")
        except Exception as e:
            print(f"❌ Error downloading data: {e}")
            print("\nPlease download the dataset manually from:")
            print("https://github.com/IBM/telco-customer-churn-on-icp4d/tree/master/data")
            print("Save it as 'telco_data.csv' in this directory")
            raise
    
    print(f"Dataset shape: {df.shape}")
    
    # Fix TotalCharges column (has spaces, should be numeric)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
    
    # Convert Yes/No columns to 1/0
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
    df['Dependents'] = df['Dependents'].map({'Yes': 1, 'No': 0})
    df['PhoneService'] = df['PhoneService'].map({'Yes': 1, 'No': 0})
    df['PaperlessBilling'] = df['PaperlessBilling'].map({'Yes': 1, 'No': 0})
    
    print("Data preprocessing complete!")
    return df

def train_decision_tree(X, y, features):
    """Train Decision Tree model"""
    print("\n" + "="*50)
    print("Training Decision Tree Model...")
    print("="*50)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print(f"Model Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Stayed', 'Churned']))
    
    # Feature importance
    importance_df = pd.DataFrame({
        'Feature': features,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print("\nTop 5 Important Features:")
    print(importance_df.head())
    
    return model, X_test, y_test, y_pred

def train_logistic_regression(X_encoded, y_encoded, updated_features):
    """Train Logistic Regression model"""
    print("\n" + "="*50)
    print("Training Logistic Regression Model...")
    print("="*50)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y_encoded, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    log_reg_model = LogisticRegression(max_iter=1000, random_state=42)
    log_reg_model.fit(X_train_scaled, y_train)
    
    y_pred = log_reg_model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    print(f"Model Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Stayed', 'Churned']))
    
    return log_reg_model, scaler, X_test, y_test, y_pred

def save_models(model, log_reg_model, scaler, features, categorical_cols, updated_features):
    """Save all models and required objects"""
    print("\n" + "="*50)
    print("Saving models and objects...")
    print("="*50)
    
    joblib.dump(model, 'decision_tree_model.joblib')
    joblib.dump(log_reg_model, 'logistic_regression_model.joblib')
    joblib.dump(scaler, 'scaler.joblib')
    joblib.dump(features, 'dt_features.joblib')
    joblib.dump(categorical_cols, 'categorical_cols.joblib')
    joblib.dump(updated_features, 'lr_features.joblib')
    
    print("✓ decision_tree_model.joblib")
    print("✓ logistic_regression_model.joblib")
    print("✓ scaler.joblib")
    print("✓ dt_features.joblib")
    print("✓ categorical_cols.joblib")
    print("✓ lr_features.joblib")
    print("\nAll models saved successfully!")

def main():
    """Main training pipeline"""
    # Load and preprocess data
    df = load_and_preprocess_data()
    
    # ===== DECISION TREE MODEL =====
    # Features for Decision Tree (simple features only)
    features = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
                'tenure', 'PhoneService', 'PaperlessBilling',
                'MonthlyCharges', 'TotalCharges']
    
    X = df[features]
    y = df['Churn']
    
    dt_model, X_test_dt, y_test_dt, y_pred_dt = train_decision_tree(X, y, features)
    
    # ===== LOGISTIC REGRESSION MODEL =====
    # Identify categorical columns for one-hot encoding
    categorical_cols = df.select_dtypes(include='object').columns.tolist()
    categorical_cols = [col for col in categorical_cols if col not in ['customerID', 'Churn']]
    
    print(f"\nCategorical columns to encode: {categorical_cols}")
    
    # One-hot encode
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # Features for Logistic Regression (all encoded features)
    X_encoded = df_encoded.drop(['customerID', 'Churn'], axis=1)
    y_encoded = df_encoded['Churn']
    updated_features = X_encoded.columns.tolist()
    
    log_reg_model, scaler, X_test_lr, y_test_lr, y_pred_lr = train_logistic_regression(
        X_encoded, y_encoded, updated_features)
    
    # Save all models
    save_models(dt_model, log_reg_model, scaler, features, categorical_cols, updated_features)
    
    print("\n" + "="*50)
    print("Training complete! You can now run the Streamlit app.")
    print("="*50)

if __name__ == "__main__":
    main()
