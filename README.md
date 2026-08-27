#  Telecom Customer Churn Prediction App

##  Project Overview
#  Live Demo

 **Try the application online:**

https://customer-churn-prediction-app-kbev3spdvbevozdto62ld5.streamlit.app/

The live application allows users to enter customer information and generate churn predictions in real time.

---

The **Telecom Customer Churn Prediction App** is an end-to-end **Machine Learning application** designed to predict whether a telecom customer is likely to **leave the service (Churn)** or remain with the company.

Customer churn is an important business problem for telecom companies because retaining existing customers is often more valuable than acquiring new ones.

This project uses historical customer data and machine learning techniques to identify customer behavior patterns associated with churn.

The trained model is integrated into an interactive **Streamlit web application**, allowing users to enter customer information and receive a real-time churn prediction.

---

#  Problem Statement

Telecom companies manage a large number of customers with different usage patterns, service plans, contract types, and billing behaviors.

Some customers may become dissatisfied and eventually leave the service.

Manually identifying these customers can be difficult when dealing with a large customer base.

This project aims to use machine learning to:

* Predict customer churn
* Identify customers who may be at risk
* Provide real-time predictions
* Support customer retention strategies
* Help businesses take proactive actions
* Demonstrate an end-to-end ML deployment workflow

---

#  System Architecture

```text id="8q4q5g"
                Telecom Customer Dataset
                         │
                         ▼
                ┌─────────────────┐
                │ Data Preparation │
                │ & Preprocessing  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Feature          │
                │ Engineering      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ ML Model        │
                │ Training        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Model Evaluation│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Streamlit App   │
                └────────┬────────┘
                         │
                         ▼
                  Customer Input
                         │
                         ▼
                 Churn Prediction
                         │
                  ┌──────┴──────┐
                  ▼             ▼
               Churn         No Churn
```

---

##  Technology Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Streamlit Cloud](https://img.shields.io/badge/Streamlit%20Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-217346?style=for-the-badge&logo=files&logoColor=white)

---

#  Key Features

##  Real-Time Churn Prediction

Users can enter customer information into the Streamlit application and receive an immediate prediction.

The system predicts whether the customer is likely to:

```text id="lq0r7p"
CHURN
```

or:

```text id="f2d7cp"
NOT CHURN
```

---

##  Interactive User Interface

The application provides an easy-to-use interface with:

* Input fields
* Sliders
* Selection boxes
* Customer attributes
* Prediction button
* Real-time prediction result

This allows users without programming knowledge to interact with the machine learning model.

---

##  Cloud Hosted Application

The application is deployed using **Streamlit Cloud**, making it accessible through a web browser without requiring local Python or machine learning setup.

---

#  Dataset

The project uses the **Telco Customer Churn** dataset:

```text id="9j4v8k"
WA_Fn-UseC_-Telco-Customer-Churn.csv
```

The dataset contains customer-level information that can be used to understand service usage, account characteristics, and churn behavior.

Typical customer attributes include areas such as:

* Customer tenure
* Contract information
* Service subscriptions
* Payment information
* Monthly charges
* Total charges
* Customer demographics
* Churn status

---

#  Machine Learning Workflow

The project follows a complete machine learning pipeline.

```text id="1j4s0e"
Raw Customer Data
        │
        ▼
Data Cleaning
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Train/Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Streamlit Deployment
        │
        ▼
Real-Time Prediction
```

---

# 1️ Data Preparation

The telecom customer dataset is first prepared for machine learning.

The preprocessing workflow can include:

* Handling missing values
* Removing unnecessary columns
* Converting data types
* Encoding categorical variables
* Preparing numerical features
* Validating customer records

---

# 2️ Feature Engineering

Customer information is transformed into machine-learning-compatible features.

Examples of useful customer characteristics include:

```text id="qf6oz1"
Tenure
Monthly Charges
Total Charges
Contract Type
Payment Method
Internet Service
Phone Service
Additional Services
```

These features allow the model to identify behavioral patterns associated with customer churn.

---

# 3️ Model Training

The project uses **Scikit-Learn** for machine learning.

The model is trained using historical customer records where the churn outcome is already known.

The objective is to learn patterns that distinguish:

```text id="b3c2s5"
Customers who Churn
        vs.
Customers who Stay
```

---

# 4️ Model Prediction

Once the model has been trained, new customer information can be passed to the model.

```text id="f0p1nr"
Customer Information
        ↓
Preprocessing
        ↓
Machine Learning Model
        ↓
Prediction
        ↓
Churn / No Churn
```

---

#  Business Value

Customer churn prediction can help telecom businesses identify customers who may be at risk of leaving.

The predictions can potentially support:

* Customer retention campaigns
* Personalized offers
* Targeted discounts
* Service improvement strategies
* Customer support prioritization
* Business decision-making

For example, a company could prioritize potentially high-risk customers for proactive retention efforts.

---

#  Project Structure

```text id="8w2zqe"
customer-churn-prediction-app/
│
├── churn_app.py
│   └── Main Streamlit application
│
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── Telecom customer dataset
│
├── requirements.txt
│   └── Required Python libraries
│
└── README.md
    └── Project documentation
```

---

#  How to Run Locally

## Prerequisites

Make sure the following are installed:

* Python 3.x
* pip
* Git

---

## 1. Clone the Repository

```bash id="0j8y6m"
git clone https://github.com/saaa637/customer-churn-prediction-app.git
```

Navigate to the project directory:

```bash id="8j2u1x"
cd customer-churn-prediction-app
```

---

## 2. Install Dependencies

Install the required libraries:

```bash id="6r3v7e"
pip install -r requirements.txt
```

---

## 3. Run the Streamlit Application

Start the application using:

```bash id="m8q5x2"
streamlit run churn_app.py
```

The application will then open in your browser.

---

#  Requirements

The project dependencies are maintained in:

```text id="0kq1q7"
requirements.txt
```

The application primarily uses:

```text id="8z2c6p"
pandas
numpy
scikit-learn
streamlit
```

---

#  End-to-End Application Workflow

```text id="4e6f9r"
User Opens Application
          │
          ▼
Customer Information Input
          │
          ▼
Input Preprocessing
          │
          ▼
Machine Learning Model
          │
          ▼
Churn Probability / Prediction
          │
          ▼
┌──────────────────────────┐
│ Customer Likely to Churn │
│          OR              │
│ Customer Likely to Stay  │
└──────────────────────────┘
```

---

#  Key Highlights

* End-to-end machine learning project
* Telecom customer churn prediction
* Real-time prediction system
* Interactive Streamlit interface
* Customer behavior analysis
* Scikit-Learn based ML workflow
* Pandas and NumPy data processing
* Cloud deployment using Streamlit
* GitHub-based project management
* Easy-to-use prediction interface

---

#  Business Use Case

A telecom organization can use a churn prediction system as part of its customer retention strategy.

The system can help answer questions such as:

* Which customers may be at risk of leaving?
* Which customer characteristics are associated with churn?
* Which customers should receive retention offers?
* How can customer retention efforts be prioritized?

The prediction system can therefore serve as a starting point for developing more advanced customer retention analytics.

---

#  Future Enhancements

##  Advanced Machine Learning

Future versions could compare multiple algorithms such as:

* Logistic Regression
* Random Forest
* Decision Tree
* Gradient Boosting
* XGBoost

Model performance could then be compared using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

---

##  Churn Probability Score

Instead of only showing a binary result, the application could display the probability of churn.

Example:

```text id="w3a1t4"
Churn Probability: 82%

Risk Level: HIGH
```

This would allow businesses to prioritize high-risk customers.

---

##  Customer Risk Segmentation

Customers could be divided into:

```text id="c8x5v1"
Low Risk
Medium Risk
High Risk
```

This could make the application more useful for customer retention teams.

---

##  Retention Recommendations

The application could provide personalized recommendations based on predicted churn risk, such as:

* Discount offers
* Contract upgrades
* Customer support follow-up
* Service recommendations
* Personalized retention campaigns

---

##  Production Enhancements

Future versions could include:

* Database integration
* Automated model retraining
* Customer history tracking
* API-based predictions
* Model monitoring
* Advanced authentication
* Real-time analytics dashboard

---

#  Project Information

**Project Name:** Telecom Customer Churn Prediction App

**Project Type:** Machine Learning & Predictive Analytics

**Domain:** Telecom / Customer Analytics

**ML Task:** Binary Classification

**Prediction:** Churn / No Churn

**Programming Language:** Python

**ML Framework:** Scikit-Learn

**Web Framework:** Streamlit

**Deployment:** Streamlit Cloud

---

#  Skills Demonstrated

This project demonstrates practical knowledge of:

* Machine Learning
* Classification
* Predictive Analytics
* Customer Churn Analysis
* Data Preprocessing
* Feature Engineering
* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Web Application Development
* Model Deployment
* Git
* GitHub
* Cloud Deployment

---

#  Live Application

 **Live Demo:**

https://customer-churn-prediction-app-kbev3spdvbevozdto62ld5.streamlit.app/

---

#  License

This project is intended for educational, portfolio, and machine learning demonstration purposes.
