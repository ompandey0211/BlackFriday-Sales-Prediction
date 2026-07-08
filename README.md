# 🛍️ Black Friday Sales Prediction

## 📌 Project Overview

This project focuses on predicting customer purchase amounts during Black Friday sales using Machine Learning techniques.

The goal is to analyze customer purchasing behavior and build a regression model that can predict the expected purchase value based on customer demographics and product-related information.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA) to understand customer behavior.
- Clean and preprocess the dataset.
- Perform feature engineering and convert categorical data into numerical format.
- Train machine learning regression models.
- Evaluate model performance.
- Build a Streamlit web application for real-time prediction.

---

## 📂 Dataset Information

The dataset contains customer purchase records from Black Friday sales.

### Features:

| Feature | Description |
|---------|-------------|
| User_ID | Unique customer ID |
| Product_ID | Unique product ID |
| Gender | Customer gender |
| Age | Customer age group |
| Occupation | Occupation code |
| City_Category | Customer city category |
| Stay_In_Current_City_Years | Years stayed in current city |
| Marital_Status | Customer marital status |
| Product_Category_1 | Main product category |
| Product_Category_2 | Secondary product category |
| Product_Category_3 | Third product category |
| Purchase | Purchase amount (Target variable) |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle
- Git & GitHub

---

## 🔍 Exploratory Data Analysis

Performed analysis:

- Dataset structure and statistics
- Missing value analysis
- Duplicate value checking
- Gender distribution
- Age group analysis
- Occupation analysis
- City category analysis
- Product category analysis
- Purchase distribution
- Customer purchase behavior analysis
- Correlation analysis

---

## ⚙️ Data Preprocessing

Steps performed:

- Removed unnecessary columns (`User_ID`, `Product_ID`)
- Handled missing values
- Converted categorical variables into numerical format
- Encoded:
  - Gender
  - Age
  - City Category
  - Stay duration
- Prepared data for machine learning models

---

## 🤖 Machine Learning Models

Models trained:

1. Linear Regression
2. Random Forest Regression
3. XGBoost Regression

---

## 📊 Model Evaluation

Evaluation metrics used:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## 🌐 Streamlit Application

A web application was developed using Streamlit where users can enter:

- Gender
- Age
- Occupation
- City Category
- Stay in Current City Years
- Marital Status
- Product Categories

The application predicts the expected Black Friday purchase amount.

---

## 📁 Project Structure
