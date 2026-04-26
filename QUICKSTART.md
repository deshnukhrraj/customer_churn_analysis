# 🚀 QUICK START GUIDE

## What I Fixed for You

Your original Colab notebook had everything in one file. I've separated it into:

✅ **train_model.py** - Trains and saves your ML models
✅ **app.py** - Clean Streamlit app (loads the saved models)
✅ **requirements.txt** - All Python dependencies
✅ **README.md** - Professional project documentation
✅ **.gitignore** - Tells Git what not to upload
✅ **GITHUB_GUIDE.md** - Step-by-step GitHub instructions

## Why Your Original Streamlit Wasn't Working

The issue was that when you separated the files, the Streamlit app couldn't find:
1. ❌ Model files (wrong paths)
2. ❌ Feature lists (not saved properly)
3. ❌ Scaler object (needed for Logistic Regression)

## How This Version Fixes It

✅ **Proper file structure** - Models and app are separated correctly
✅ **Saved objects** - All 6 required .joblib files are saved
✅ **Correct imports** - Models load from saved files, not from memory
✅ **Error handling** - Clear messages if models aren't trained yet
✅ **Caching** - Uses @st.cache_resource for faster loading

## 📋 Step-by-Step Instructions

### 1️⃣ Download All Files

Download the `customer-churn-prediction` folder containing:
- train_model.py
- app.py  
- requirements.txt
- README.md
- GITHUB_GUIDE.md
- .gitignore

### 2️⃣ Set Up Your Environment

```bash
# Open terminal/command prompt
cd customer-churn-prediction

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Train the Models

```bash
python train_model.py
```

This creates 6 files:
- decision_tree_model.joblib
- logistic_regression_model.joblib
- scaler.joblib
- dt_features.joblib
- categorical_cols.joblib
- lr_features.joblib

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Browser opens at http://localhost:8501

### 5️⃣ Test Predictions

1. Enter customer details in sidebar
2. Click "Predict Churn"
3. See results from both models!

## 🌐 Push to GitHub

Follow the complete guide in **GITHUB_GUIDE.md** for:
- Creating a GitHub repo
- Pushing your code
- Deploying to Streamlit Cloud

**Quick version:**

```bash
# In your project folder
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/customer-churn-prediction.git
git push -u origin main
```

## ⚠️ Important Notes

### Data Download
The script downloads data automatically. If it fails due to network restrictions:
1. Manually download from: https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv
2. Save as `telco_data.csv` in your project folder
3. Run `python train_model.py` again

### Model Files in Git
By default, model files (.joblib) are NOT ignored. Options:

**Option A**: Commit models (good for small projects)
- Just push everything as-is
- Users can use the app immediately

**Option B**: Don't commit models (professional approach)
- Uncomment `*.joblib` in .gitignore
- Users run `python train_model.py` first
- Keeps repo size small

### Streamlit Cloud Deployment
If you didn't commit models, Streamlit Cloud won't have them. Solutions:

1. **Commit the models** (easiest)
2. **Auto-train on startup** - Add to app.py:
```python
import os
if not os.path.exists('decision_tree_model.joblib'):
    import subprocess
    subprocess.run(['python', 'train_model.py'])
```

## 🆘 Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "FileNotFoundError: decision_tree_model.joblib"
```bash
python train_model.py
```

### "Streamlit command not found"
```bash
pip install streamlit
```

### Git push rejected
```bash
git pull origin main --rebase
git push origin main
```

## 📊 Project Structure

```
customer-churn-prediction/
│
├── train_model.py          # Run this FIRST to create models
├── app.py                  # Run this SECOND for web app
├── requirements.txt        # Dependencies
├── README.md              # Project documentation
├── GITHUB_GUIDE.md        # GitHub instructions
├── .gitignore             # Git ignore rules
│
└── Generated after training:
    ├── decision_tree_model.joblib
    ├── logistic_regression_model.joblib
    ├── scaler.joblib
    ├── dt_features.joblib
    ├── categorical_cols.joblib
    └── lr_features.joblib
```

## ✅ Checklist

- [ ] Downloaded all files
- [ ] Installed requirements: `pip install -r requirements.txt`
- [ ] Trained models: `python train_model.py`
- [ ] Tested app: `streamlit run app.py`
- [ ] Pushed to GitHub (see GITHUB_GUIDE.md)
- [ ] (Optional) Deployed to Streamlit Cloud

## 🎉 You're All Set!

Your project is now properly structured and ready for GitHub!

**Next Steps:**
1. Customize README.md with your name
2. Add screenshots to README
3. Deploy to Streamlit Cloud
4. Share on LinkedIn/portfolio

---

**Questions?** Check the detailed GITHUB_GUIDE.md or README.md for more info!
