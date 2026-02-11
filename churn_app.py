import streamlit as st
import pandas as pd
# Data load karein
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

st.title("Customer Churn Analysis")

# 📊 Bar Chart: Churn Count
st.subheader("Total Churn Distribution")
churn_count = df['Churn'].value_counts()
st.bar_chart(churn_count)

# 📈 Line Chart: Tenure vs Monthly Charges
st.subheader("Tenure vs Monthly Charges")
st.line_chart(df[['tenure', 'MonthlyCharges']].head(50))


st.title("📊 Customer Churn Predictor Live")
st.write("Ye aapki asli deployed app ka preview hai!")

# Inputs
tenure = st.slider("Tenure (Months)", 1, 72, 12)
monthly = st.number_input("Monthly Charges", 18, 120, 70)

if st.button("Predict"):
    st.balloons() # Thoda celebration!
    st.success(f"Success! Model is analyzing Tenure: {tenure}")
