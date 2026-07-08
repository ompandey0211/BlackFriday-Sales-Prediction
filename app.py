import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Black Friday Sales Prediction",
    page_icon="🛍️",
    layout="wide"
)

# Locate the model file
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.pkl"

# Load the model
model = joblib.load(MODEL_PATH)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#334155);
    color:white;
}

h1,h2,h3,label{
    color:white!important;
}

div[data-baseweb="select"]{
    color:black;
}

div[data-testid="stNumberInput"] input{
    color:black;
}

.stButton>button{
    background:#ff4b4b;
    color:white;
    border-radius:12px;
    height:55px;
    width:100%;
    font-size:20px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#ff7b00;
    transform:scale(1.03);
}

.block-container{
    padding-top:2rem;
}

.card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    box-shadow:0px 0px 25px rgba(255,255,255,0.15);
}

</style>
""", unsafe_allow_html=True)

st.title("🛍️ Black Friday Sales Prediction")

st.write("Enter customer details to predict purchase amount.")

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

    gender_map = {
        "F": 0,
        "M": 1
    }

    age_map = {
        "0-17": 0,
        "18-25": 1,
        "26-35": 2,
        "36-45": 3,
        "46-50": 4,
        "51-55": 5,
        "55+": 6
    }

    stay_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4+": 4
    }

    input_data = pd.DataFrame({
        "Gender": [gender_map[gender]],
        "Age": [age_map[age]],
        "Occupation": [occupation],
        "Stay_In_Current_City_Years": [stay_map[stay_years]],
        "Marital_Status": [marital_status],
        "Product_Category_1": [product_category_1],
        "Product_Category_2": [product_category_2],
        "Product_Category_3": [product_category_3],
        "City_Category_B": [1 if city_category == "B" else 0],
        "City_Category_C": [1 if city_category == "C" else 0]
    })

   

    prediction = model.predict(input_data)

    st.success(f"Predicted Purchase Amount: ₹{prediction[0]:.2f}")
