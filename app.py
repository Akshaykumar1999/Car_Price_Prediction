import streamlit as st
import pickle
import numpy as np
from sklearn.tree import DecisionTreeRegressor

DecisionTreeRegressor.monotonic_cst = None

# Load Models
lr = pickle.load(open("Linear_reg model.pkl", "rb"))
rid = pickle.load(open("Ridge_reg model.pkl", "rb"))
las = pickle.load(open("Lasso_reg model.pkl", "rb"))
rf = pickle.load(open("RandomForest_reg model.pkl", "rb"))
bag = pickle.load(open("Bagging_reg model.pkl", "rb"))


st.set_page_config(page_title="Car Price Prediction App", page_icon="🚗", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🚗 Car Selling Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #7D3C98;'>Select Model ➡ Fill Details ➡ Predict Price</h4>", unsafe_allow_html=True)
st.markdown("---")

# -------------------- Sidebar -------------------- #
st.sidebar.title("🔍 Model Selection")
model_choice = st.sidebar.selectbox("Choose Machine Learning Model", 
                                    ["Linear Regression", "Ridge Regression", "Lasso Regression", "Random Forest", "Bagging Regressor"])

model_map = {
    "Linear Regression": lr,
    "Ridge Regression": rid,
    "Lasso Regression": las,
    "Random Forest": rf,
    "Bagging Regressor": bag
}

# -------------------- Input Form -------------------- #
with st.form("prediction_form"):
    st.subheader("📝 Car Details")

    col1, col2 = st.columns(2)

    with col1:
        year = st.slider('Manufacturing Year', 2000, 2020, 2015)
        km_driven = st.slider('KM Driven', 1, 200000, 50000)
        name = st.selectbox('Car Name', [
            'Ambassador Classic 2000 Dsz',
            'Ambassador Grand 1800 ISZ MPFI PW CL',
            'Audi A4 1.8 TFSI',
            'Audi A4 2.0 TDI',
            'Audi A4 2.0 TDI 177 Bhp Premium Plus',
            'Audi A4 3.0 TDI Quattro',
            'Audi A4 30 TFSI Technology'
        ])

    with col2:
        fuel = st.selectbox('Fuel Type', ['Electric', 'LPG', 'Petrol'])
        seller_type = st.selectbox('Seller Type', ['Individual', 'Trustmark Dealer'])
        transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
        owner = st.selectbox('Owner Type', ['Fourth & Above Owner', 'Second Owner', 'Test Drive Car', 'Third Owner'])

    submitted = st.form_submit_button("💰 Predict Selling Price")

# -------------------- Prediction Logic -------------------- #
if submitted:
    name_map = {
        'Ambassador Classic 2000 Dsz': [1,0,0,0,0,0,0],
        'Ambassador Grand 1800 ISZ MPFI PW CL': [0,1,0,0,0,0,0],
        'Audi A4 1.8 TFSI': [0,0,1,0,0,0,0],
        'Audi A4 2.0 TDI': [0,0,0,1,0,0,0],
        'Audi A4 2.0 TDI 177 Bhp Premium Plus': [0,0,0,0,1,0,0],
        'Audi A4 3.0 TDI Quattro': [0,0,0,0,0,1,0],
        'Audi A4 30 TFSI Technology': [0,0,0,0,0,0,1]
    }

    fuel_map = {'Electric': [1,0,0], 'LPG': [0,1,0], 'Petrol': [0,0,1]}
    seller_map = {'Individual': [1,0], 'Trustmark Dealer': [0,1]}
    trans_map = {'Manual': 1, 'Automatic': 0}
    owner_map = {
        'Fourth & Above Owner': [1,0,0,0],
        'Second Owner': [0,1,0,0],
        'Test Drive Car': [0,0,1,0],
        'Third Owner': [0,0,0,1]
    }

    input_features = [year, km_driven] + \
                     name_map[name] + \
                     fuel_map[fuel] + \
                     seller_map[seller_type] + \
                     [trans_map[transmission]] + \
                     owner_map[owner] + \
                     [0]*1484

    test_array = np.array(input_features).reshape(1, -1)

    selected_model = model_map[model_choice]
    prediction = selected_model.predict(test_array)[0]

    st.markdown("---")
    st.success(f"💵 Estimated Selling Price: ₹ {round(prediction, 2)} Lakhs", icon="✅")

    st.markdown("<h4 style='text-align: center; color: #117A65;'>Thank you for using the prediction app!</h4>", unsafe_allow_html=True)
