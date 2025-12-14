import pandas as pd
import streamlit as st
import joblib

# Load model
model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Prediction")

st.title(" House Price Prediction")
st.write("Enter the details below to predict house price")

# Correct feature names
inputs = [
    'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
    'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea',
    'Fireplaces', 'BsmtFinSF1', 'LotFrontage',
    'WoodDeckSF', 'OpenPorchSF', 'LotArea', 'CentralAir'
]

input_data = {}

for feature in inputs:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(
            "Central Air",
            options=["Yes", "No"]
        )
    else:
        input_data[feature] = st.number_input(
            feature,
            value=0.0
        )

# Convert CentralAir
if st.button("Predict Price"):
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == "Yes" else 0

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted House Price: ₹ {prediction:,.2f}")