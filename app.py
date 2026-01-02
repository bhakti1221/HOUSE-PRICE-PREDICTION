import pandas as pd
import streamlit as st
import joblib
import matplotlib.pyplot as plt

model = joblib.load("house_price_model.pkl")

st.set_page_config(page_title="House Price Prediction")
st.title(" House Price Prediction")

FEATURE_ORDER = [
    'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
    'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea',
    'Fireplaces', 'BsmtFinSF1', 'LotFrontage',
    'WoodDeckSF', 'OpenPorchSF', 'LotArea', 'CentralAir'
]

input_data = {}

for feature in FEATURE_ORDER:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox("Central Air", ["Yes", "No"])
    else:
        input_data[feature] = st.number_input(feature, min_value=0.0)

if st.button("Predict Price"):
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == "Yes" else 0

    input_df = pd.DataFrame(
        [[input_data[col] for col in FEATURE_ORDER]],
        columns=FEATURE_ORDER
    )

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted House Price: ₹ {prediction:,.2f}")

    fig, ax = plt.subplots()
    ax.bar(["Predicted Price"], [prediction])
    st.pyplot(fig)