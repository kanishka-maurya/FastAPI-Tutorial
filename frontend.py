import streamlit as st
import requests

st.header("Insurance Premium Classifier")

API_URL = "http://127.0.0.1:8000/predict" 

age = st.number_input("Age", key="age", min_value=18, max_value=100, value=30, step=1)
weight = st.number_input("Weight (in kg)", key="weight", min_value=30, max_value=120, value=70, step=1)
height = st.number_input("Height (in cm)", key="height", min_value=100, max_value=250, value=170, step=1)
smoker = st.selectbox("Smoker", options=[True, False], key="smoker")
income_lpa = st.number_input("Income (in LPA)", key="income_lpa", min_value=0.5, max_value=50.0, value=5.0, step=0.1)
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker, 
        "city": city,
        "occupation": occupation
    }
    
    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()

        if response.status_code == 200 and "response" in result:
            prediction = result["response"]
            st.success(f"Predicted Insurance Premium Category: **{prediction['predicted_category']}**")
            st.write("🔍 Confidence:", prediction["confidence"])
            st.write("📊 Class Probabilities:")
            st.json(prediction["class_probabilities"])

        else:
            st.error(f"Status: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")