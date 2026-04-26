"""
Customer Churn Prediction - Streamlit App
This app uses pre-trained models to predict customer churn
"""

import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

@st.cache_resource
def load_models():
    """Load all saved models and objects"""
    try:
        model = joblib.load('decision_tree_model.joblib')
        log_reg_model = joblib.load('logistic_regression_model.joblib')
        scaler = joblib.load('scaler.joblib')
        dt_features = joblib.load('dt_features.joblib')
        categorical_cols = joblib.load('categorical_cols.joblib')
        lr_features = joblib.load('lr_features.joblib')
        return model, log_reg_model, scaler, dt_features, categorical_cols, lr_features
    except FileNotFoundError as e:
        st.error(f"❌ Model files not found! Please run 'train_model.py' first to generate the models.")
        st.stop()

# Load models
model, log_reg_model, scaler, dt_features, categorical_cols, lr_features = load_models()

# App title and description
st.title("📊 Customer Churn Prediction")
st.markdown("""
This app predicts whether a customer is likely to churn (leave the service) using two machine learning models:
- **Decision Tree Classifier**
- **Logistic Regression**

Enter customer details in the sidebar and click **Predict Churn** to see the results.
""")

# Sidebar for inputs
st.sidebar.header("📝 Customer Details")

# Basic Information
st.sidebar.subheader("Basic Information")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.sidebar.selectbox("Has Partner", ["No", "Yes"])
dependents = st.sidebar.selectbox("Has Dependents", ["No", "Yes"])
tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)

# Services
st.sidebar.subheader("Services")
phone_service = st.sidebar.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["No internet service", "No", "Yes"])
online_backup = st.sidebar.selectbox("Online Backup", ["No internet service", "No", "Yes"])
device_protection = st.sidebar.selectbox("Device Protection", ["No internet service", "No", "Yes"])
tech_support = st.sidebar.selectbox("Tech Support", ["No internet service", "No", "Yes"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])

# Account Information
st.sidebar.subheader("Account Information")
contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["No", "Yes"])
payment_method = st.sidebar.selectbox("Payment Method", 
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.sidebar.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0, step=5.0)
total_charges = st.sidebar.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=500.0, step=50.0)

# Predict button
predict_button = st.sidebar.button("🔮 Predict Churn", type="primary", use_container_width=True)

# Create input dictionary
raw_data = {
    'gender': 1 if gender == "Male" else 0,
    'SeniorCitizen': 1 if senior_citizen == "Yes" else 0,
    'Partner': 1 if partner == "Yes" else 0,
    'Dependents': 1 if dependents == "Yes" else 0,
    'tenure': tenure,
    'PhoneService': 1 if phone_service == "Yes" else 0,
    'PaperlessBilling': 1 if paperless_billing == "Yes" else 0,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'MultipleLines': multiple_lines,
    'InternetService': internet_service,
    'OnlineSecurity': online_security,
    'OnlineBackup': online_backup,
    'DeviceProtection': device_protection,
    'TechSupport': tech_support,
    'StreamingTV': streaming_tv,
    'StreamingMovies': streaming_movies,
    'Contract': contract,
    'PaymentMethod': payment_method
}

# Main area
if not predict_button:
    st.info("👈 Enter customer details in the sidebar and click **Predict Churn** to see predictions")
    
    # Show example customer profile
    st.subheader("Example Customer Profile")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tenure", "12 months")
        st.metric("Contract", "Month-to-month")
    with col2:
        st.metric("Monthly Charges", "$50.00")
        st.metric("Internet Service", "DSL")
    with col3:
        st.metric("Total Charges", "$500.00")
        st.metric("Payment Method", "Electronic check")

else:
    # Convert raw data to DataFrame
    input_df = pd.DataFrame([raw_data])
    
    st.subheader("🎯 Prediction Results")
    
    # Create two columns for side-by-side comparison
    col1, col2 = st.columns(2)
    
    # === DECISION TREE PREDICTION ===
    with col1:
        st.markdown("### 🌳 Decision Tree Model")
        
        # Prepare data for Decision Tree
        dt_input = input_df[dt_features]
        dt_prediction = model.predict(dt_input)[0]
        dt_probability = model.predict_proba(dt_input)[0]
        
        if dt_prediction == 1:
            st.error(f"**Prediction: LIKELY TO CHURN** 😟")
            st.metric("Churn Probability", f"{dt_probability[1]:.1%}", delta=f"{dt_probability[1]-0.5:.1%}")
        else:
            st.success(f"**Prediction: LIKELY TO STAY** 😊")
            st.metric("Stay Probability", f"{dt_probability[0]:.1%}", delta=f"{dt_probability[0]-0.5:.1%}")
        
        # Show probabilities
        st.write("**Detailed Probabilities:**")
        prob_df_dt = pd.DataFrame({
            'Outcome': ['Will Stay', 'Will Churn'],
            'Probability': [f"{dt_probability[0]:.1%}", f"{dt_probability[1]:.1%}"]
        })
        st.dataframe(prob_df_dt, use_container_width=True, hide_index=True)
    
    # === LOGISTIC REGRESSION PREDICTION ===
    with col2:
        st.markdown("### 📈 Logistic Regression Model")
        
        # Prepare data for Logistic Regression (one-hot encode and scale)
        lr_input_encoded = pd.get_dummies(input_df, columns=categorical_cols, drop_first=True)
        lr_input_final = lr_input_encoded.reindex(columns=lr_features, fill_value=0)
        lr_input_scaled = scaler.transform(lr_input_final)
        
        lr_prediction = log_reg_model.predict(lr_input_scaled)[0]
        lr_probability = log_reg_model.predict_proba(lr_input_scaled)[0]
        
        if lr_prediction == 1:
            st.error(f"**Prediction: LIKELY TO CHURN** 😟")
            st.metric("Churn Probability", f"{lr_probability[1]:.1%}", delta=f"{lr_probability[1]-0.5:.1%}")
        else:
            st.success(f"**Prediction: LIKELY TO STAY** 😊")
            st.metric("Stay Probability", f"{lr_probability[0]:.1%}", delta=f"{lr_probability[0]-0.5:.1%}")
        
        # Show probabilities
        st.write("**Detailed Probabilities:**")
        prob_df_lr = pd.DataFrame({
            'Outcome': ['Will Stay', 'Will Churn'],
            'Probability': [f"{lr_probability[0]:.1%}", f"{lr_probability[1]:.1%}"]
        })
        st.dataframe(prob_df_lr, use_container_width=True, hide_index=True)
    
    # Show agreement/disagreement
    st.markdown("---")
    if dt_prediction == lr_prediction:
        st.success("✅ **Both models agree on the prediction!**")
    else:
        st.warning("⚠️ **Models disagree** - consider reviewing customer details or using ensemble approach")
    
    # Customer summary
    with st.expander("📋 View Customer Summary"):
        summary_col1, summary_col2 = st.columns(2)
        with summary_col1:
            st.write("**Demographics:**")
            st.write(f"- Gender: {gender}")
            st.write(f"- Senior Citizen: {senior_citizen}")
            st.write(f"- Partner: {partner}")
            st.write(f"- Dependents: {dependents}")
            st.write(f"- Tenure: {tenure} months")
        
        with summary_col2:
            st.write("**Account Details:**")
            st.write(f"- Contract: {contract}")
            st.write(f"- Payment Method: {payment_method}")
            st.write(f"- Monthly Charges: ${monthly_charges:.2f}")
            st.write(f"- Total Charges: ${total_charges:.2f}")
            st.write(f"- Paperless Billing: {paperless_billing}")

# Footer
st.markdown("---")
st.caption("💡 **Tip:** Higher churn probability indicates the customer is more likely to cancel their service.")
