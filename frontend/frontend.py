import streamlit as st
import requests

st.set_page_config(page_title="Loan Prediction App", page_icon="🏦")

st.title("Loan Approval Prediction")
st.markdown("Fill the details below to check loan approval status")

# Inputs
dependents = st.number_input("Number of Dependents", min_value=0, step=1)

education = st.selectbox(
    "Education",
    options=[0, 1],
    format_func=lambda x: "Graduate" if x == 1 else "Not Graduate"
)

self_employed = st.selectbox(
    "Self Employed",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

loan_term = st.number_input("Loan Term (in months)", min_value=0, step=1)

cibil_score = st.number_input("CIBIL Score", min_value=0, step=1)

# Button
if st.button("Predict Loan Status"):

    data = {
        "no_of_dependents": int(dependents),
        "education": int(education),
        "self_employed": int(self_employed),
        "loan_term": int(loan_term),
        "cibil_score": int(cibil_score)
    }

    try:
        response = requests.post(
            url="http://127.0.0.1:8000/predict",
            json=data,
            timeout=5
        )

        if response.status_code == 200:
            result = response.json()

            if result["prediction"] == 1:
                st.success("✅ Loan Approved")
            else:
                st.error("❌ Loan Rejected")

            

        else:
            st.error("Backend error occurred")

    except requests.exceptions.ConnectionError:
        st.error("⚠ Could not connect to backend. Is FastAPI running?")
