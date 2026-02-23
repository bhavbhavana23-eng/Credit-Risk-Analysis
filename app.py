import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("Credit Risk Prediction App")

st.write("Enter Customer Details")

age = st.number_input("Age", min_value=18, max_value=100)
credit_amount = st.number_input("Credit Amount")
duration = st.number_input("Loan Duration (months)")

if st.button("Predict"):
    
    input_data = np.array([[age, credit_amount, duration]])
    
    prediction = model.predict(input_data)
    
    if prediction == 1:
        st.success("Good Credit Risk ✅")
    else:
        st.error("Bad Credit Risk ❌")