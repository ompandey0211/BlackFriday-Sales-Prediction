
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/model.pkl")

st.title("Black Friday Sales Prediction")

st.write("Enter customer details to predict purchase amount")

# Inputs
gender = st.selectbox("Gender", ["M", "F"])
age = st.selectbox(
    "Age",
    ["0-17", "18-25", "26-35", "36-45", "46-50", "51-55", "55+"]
)

occupation = st.number_input("Occupation", min_value=0, max_value=20)
city_category = st.selectbox("City Category", ["A", "B", "C"])
stay_years = st.selectbox(
    "Stay In Current City Years",
    ["0", "1", "2", "3", "4+"]
)

marital_status = st.selectbox(
    "Marital Status",
    [0, 1]
)

product_category_1 = st.number_input(
    "Product Category 1",
    min_value=1
)

product_category_2 = st.number_input(
    "Product Category 2",
    min_value=0
)

product_category_3 = st.number_input(
    "Product Category 3",
    min_value=0
)


if st.button("Predict Purchase"):

    input_data = pd.DataFrame({
        "Gender": [gender],
        "Age": [age],
        "Occupation": [occupation],
        "Stay_In_Current_City_Years": [stay_years],
        "Marital_Status": [marital_status],
        "Product_Category_1": [product_category_1],
        "Product_Category_2": [product_category_2],
        "Product_Category_3": [product_category_3],
        "City_Category_B": [1 if city_category == "B" else 0],
        "City_Category_C": [1 if city_category == "C" else 0]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Purchase Amount: ₹{prediction[0]:.2f}")
