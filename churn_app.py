import streamlit as st
import pandas as pd

st.title("📊 Customer Churn Predictor Live")
st.write("Ye aapki asli deployed app ka preview hai!")

# Inputs
tenure = st.slider("Tenure (Months)", 1, 72, 12)
monthly = st.number_input("Monthly Charges", 18, 120, 70)

if st.button("Predict"):
    st.balloons() # Thoda celebration!
    st.success(f"Success! Model is analyzing Tenure: {tenure}")
