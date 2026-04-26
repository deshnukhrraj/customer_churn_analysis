# Customer Churn Prediction

A machine learning project that predicts customer churn using **Decision Tree** and **Logistic Regression** models. Includes an interactive **Streamlit** web application for real-time predictions.

## 📊 Project Overview

This project analyzes telecom customer data to predict which customers are likely to churn (cancel their service). The models help identify at-risk customers so businesses can take proactive retention measures.

### Models Used:
- **Decision Tree Classifier** - Captures non-linear patterns
- **Logistic Regression** - Provides probabilistic predictions with feature scaling

## 🚀 Features

- **Dual Model Prediction**: Compare results from two different algorithms
- **Interactive Web App**: User-friendly Streamlit interface
- **Real-time Predictions**: Instant churn probability calculations
- **Feature Analysis**: Understand which factors contribute to churn
- **Visual Insights**: Clear presentation of prediction results

## 📁 Project Structure

```
customer-churn-prediction/
├── train_model.py              # Model training script
├── app.py                      # Streamlit web application
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
└── models/                     # Saved model files (generated after training)
    ├── decision_tree_model.joblib
    ├── logistic_regression_model.joblib
    ├── scaler.joblib
    ├── dt_features.joblib
    ├── categorical_cols.joblib
    └── lr_features.joblib
```

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 📚 Usage

### Step 1: Train the Models

Run the training script to download data, train models, and save them:

```bash
python train_model.py
```

This will:
- Download the Telco Customer Churn dataset
- Preprocess the data
- Train both Decision Tree and Logistic Regression models
- Save all models and required objects as `.joblib` files
- Display training accuracy and metrics

Expected output:
```
Loading data...
Dataset shape: (7043, 21)
Data preprocessing complete!

==================================================
Training Decision Tree Model...
==================================================
Training samples: 5634
Testing samples: 1409
Model Accuracy: 78.01%

==================================================
Training Logistic Regression Model...
==================================================
Training samples: 5634
Testing samples: 1409
Model Accuracy: 80.34%

==================================================
Saving models and objects...
==================================================
✓ decision_tree_model.joblib
✓ logistic_regression_model.joblib
✓ scaler.joblib
...
All models saved successfully!
```

### Step 2: Run the Streamlit App

Launch the web application:

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Step 3: Make Predictions

1. Enter customer details in the sidebar
2. Click "🔮 Predict Churn"
3. View predictions from both models
4. Compare results and probabilities

## 📊 Dataset

**Source**: [IBM Telco Customer Churn Dataset](https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv)

**Features**:
- Demographics: gender, senior citizen, partner, dependents
- Account info: tenure, contract type, payment method, billing
- Services: phone, internet, streaming, security, backup
- Charges: monthly charges, total charges

**Target**: Churn (Yes/No)

## 🎯 Model Performance

| Model | Accuracy |
|-------|----------|
| Decision Tree | ~78% |
| Logistic Regression | ~80% |

## 🔧 Troubleshooting

### Issue: "Model files not found"
**Solution**: Run `python train_model.py` first to generate model files

### Issue: Streamlit app doesn't start
**Solution**: 
```bash
pip install streamlit --upgrade
streamlit run app.py
```

### Issue: Import errors
**Solution**: 
```bash
pip install -r requirements.txt --upgrade
```

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set `app.py` as the main file
5. Deploy!

**Note**: Make sure to commit your `.joblib` model files or retrain on Streamlit Cloud

### Deploy to Heroku

1. Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Created by [Your Name]

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

## 📞 Contact

For questions or feedback, reach out at: [your.email@example.com]
