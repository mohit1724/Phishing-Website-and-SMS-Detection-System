# 🛡️ AI-Powered Phishing Website Detection System

This project is a **machine learning-based phishing website detection system** designed to identify malicious and legitimate websites using data-driven techniques.  
It analyzes website features and predicts whether a given website is **safe or phishing**, helping users and organizations protect against online scams.

---

## 🚀 Project Overview

Phishing is one of the most common cyber threats where attackers mimic legitimate websites to steal sensitive user data.  
This system leverages **machine learning algorithms** to automatically classify URLs as *legitimate* or *phishing* based on extracted web features.

The project includes:
- Dataset preprocessing and feature extraction  
- Model training and evaluation  
- Accuracy and confusion matrix visualization  
- Real-time prediction capability for new URLs  

---

## 🧠 Technologies Used

- **Python 3.x**
- **Jupyter Notebook**
- **scikit-learn**
- **pandas**
- **numpy**
- **matplotlib**
- **joblib / pickle**

---

## ⚙️ How It Works

1. **Data Collection:**  
   A dataset containing website attributes is used (such as URL length, HTTPS presence, domain age, etc.).

2. **Feature Engineering:**  
   Extracted features help the model understand key indicators of phishing behavior.

3. **Model Training:**  
   ML algorithms (e.g., Decision Tree, Random Forest, Logistic Regression) are trained on labeled data.

4. **Evaluation:**  
   Accuracy, precision, recall, and confusion matrices measure model performance.

5. **Prediction:**  
   The trained model predicts if a new website URL is *legitimate* or *phishing*.

---

## 📊 Example Output

| URL | Prediction |
|-----|-------------|
| `https://www.google.com` | Legitimate ✅ |
| `http://login-paypal-update-info.com` | Phishing ⚠️ |

<img width="1895" height="856" alt="image" src="https://github.com/user-attachments/assets/7a42c879-492a-422e-b95d-02822385c2e3" />

