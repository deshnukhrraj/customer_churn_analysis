# Step-by-Step Guide: Push Your Project to GitHub

## ✅ Prerequisites
- GitHub account created
- Git installed on your computer
- Project files ready

---

## 📋 Step 1: Test Locally First

Before pushing to GitHub, make sure everything works:

```bash
# 1. Train the models
python train_model.py

# 2. Run the Streamlit app
streamlit run app.py

# 3. Test predictions in the browser
```

If both work correctly, proceed to GitHub upload.

---

## 🌐 Step 2: Create GitHub Repository

### Option A: Using GitHub Website (Easiest for Beginners)

1. **Go to GitHub**: https://github.com
2. **Click** the `+` icon (top right) → "New repository"
3. **Fill in details**:
   - Repository name: `customer-churn-prediction`
   - Description: `ML project to predict customer churn using Decision Tree and Logistic Regression`
   - Visibility: **Public** (or Private)
   - ❌ **DO NOT** check "Initialize with README" (we already have one)
4. **Click** "Create repository"

### Option B: Using GitHub CLI

```bash
gh repo create customer-churn-prediction --public
```

---

## 💻 Step 3: Initialize Git Locally

Open terminal/command prompt in your project folder:

```bash
# Navigate to your project folder
cd /path/to/customer-churn-prediction

# Initialize Git repository
git init

# Add all files to staging
git add .

# Check what will be committed
git status

# Create first commit
git commit -m "Initial commit: Customer churn prediction project"
```

---

## 🔗 Step 4: Connect to GitHub

**Get your repository URL from GitHub** (should look like):
```
https://github.com/YOUR_USERNAME/customer-churn-prediction.git
```

**Connect your local repo to GitHub**:

```bash
# Add GitHub as remote origin
git remote add origin https://github.com/YOUR_USERNAME/customer-churn-prediction.git

# Verify it's added
git remote -v
```

---

## 🚀 Step 5: Push to GitHub

```bash
# Push to GitHub (first time)
git push -u origin main

# OR if your branch is called 'master':
git push -u origin master
```

### If you get an error about branch names:

```bash
# Rename branch to 'main'
git branch -M main

# Then push
git push -u origin main
```

### If you need to authenticate:

**Option 1: Personal Access Token (Recommended)**
1. Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Generate new token with `repo` permissions
3. Use token as password when Git asks

**Option 2: GitHub CLI**
```bash
gh auth login
```

---

## ✅ Step 6: Verify Upload

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/customer-churn-prediction`
2. You should see all your files:
   - ✅ train_model.py
   - ✅ app.py
   - ✅ requirements.txt
   - ✅ README.md
   - ✅ .gitignore

---

## 📦 Step 7: Handle Model Files

**Option A: Include model files in repo** (for small projects)

```bash
# The models are currently ignored - remove them from .gitignore
# Edit .gitignore and remove or comment out:
# *.joblib

# Then add and commit models
git add *.joblib
git commit -m "Add trained model files"
git push
```

**Option B: Don't commit models** (recommended for larger models)

Users will run `train_model.py` to generate their own models.

Add this to your README:
```markdown
**Important**: Run `python train_model.py` before starting the app to generate model files.
```

---

## 🌐 Step 8: Deploy to Streamlit Cloud (Optional)

1. Go to: https://share.streamlit.io/
2. Click "New app"
3. Select your GitHub repo: `YOUR_USERNAME/customer-churn-prediction`
4. Main file path: `app.py`
5. Click "Deploy"

**Important for Streamlit Cloud deployment**:

If you didn't commit model files, add this to the top of `app.py`:

```python
import os

# Check if models exist, if not, train them
if not os.path.exists('decision_tree_model.joblib'):
    import subprocess
    subprocess.run(['python', 'train_model.py'])
```

---

## 🔄 Future Updates

When you make changes:

```bash
# Check what changed
git status

# Add changes
git add .

# Commit with message
git commit -m "Describe your changes here"

# Push to GitHub
git push
```

---

## 🆘 Common Issues and Solutions

### Issue 1: "Permission denied (publickey)"
**Solution**: Use HTTPS URL instead of SSH
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/customer-churn-prediction.git
```

### Issue 2: "Failed to push - rejected"
**Solution**: Pull first, then push
```bash
git pull origin main --rebase
git push origin main
```

### Issue 3: "Large files warning"
**Solution**: Don't commit large model files, let users generate them
```bash
# Remove large files from Git
git rm --cached *.joblib
git commit -m "Remove large model files"
git push
```

### Issue 4: "Authentication failed"
**Solution**: Use Personal Access Token
1. Create token on GitHub
2. Use token as password when pushing

---

## 📝 Quick Reference Commands

```bash
# Check status
git status

# Add files
git add .

# Commit
git commit -m "Your message"

# Push
git push

# Pull latest changes
git pull

# View commit history
git log --oneline

# Create new branch
git checkout -b feature-branch-name
```

---

## ✨ You're Done!

Your project is now on GitHub! 🎉

**Next Steps**:
- ⭐ Add a nice banner image to README
- 📝 Update README with your name/contact
- 🌐 Share the GitHub link
- 🚀 Deploy to Streamlit Cloud
- 📊 Add project to your portfolio

---

**Need Help?**
- GitHub Docs: https://docs.github.com/
- Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
- Streamlit Deployment: https://docs.streamlit.io/streamlit-community-cloud/get-started
