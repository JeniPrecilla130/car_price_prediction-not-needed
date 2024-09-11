import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('car_price_prediction_model.pkl')

# List of selected features (these should match the features used in your model)
selected_features = ['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage(Kmpl)', 'engine(cc)', 'max_power(bhp)', 'torque(rpm)', 'seats']

# Define a function for predicting car price
def predict_car_price(user_input):
    # Convert user input into a DataFrame
    user_data = pd.DataFrame([user_input], columns=selected_features)
    
    # Predict the car price based on user input
    prediction = model.predict(user_data)
    
    return prediction[0]

# Set the page icon and title
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")  # You can use an emoji like 🚗 or upload your own icon.

# Custom CSS for background image and blur effect
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://th.bing.com/th/id/OIP.qUTpyFjNX1V-7AbIllH8WQAAAA?rs=1&pid=ImgDetMain'); /* Replace with the URL of your image */
        background-size: cover;
        background-position: center;
        filter: blur(8px);  /* Blurring the background */
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
    .block-container {
        background: rgba(255, 255, 255, 0.8);  /* Transparent white background for the form content */
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Create a Streamlit app
st.title("Car Price Prediction")

st.write("""
### Please provide the car details below:
""")

# Move inputs to the main page
# year
year = st.number_input('Year of the car:', min_value=1990, max_value=2024, step=1)

# km_driven
km_driven = st.number_input('Kilometers driven by the car:', min_value=0, step=500)

# Dropdown menus for categorical features
fuel = st.selectbox('Select Fuel Type:', ('Diesel', 'Petrol', 'CNG', 'LPG'))
fuel = {'Diesel': 0, 'Petrol': 1, 'CNG': 2, 'LPG': 3}[fuel]

seller_type = st.selectbox('Select Seller Type:', ('Individual', 'Dealer', 'Trustmark Dealer'))
seller_type = {'Individual': 0, 'Dealer': 1, 'Trustmark Dealer': 2}[seller_type]

transmission = st.selectbox('Select Transmission Type:', ('Manual', 'Automatic'))
transmission = {'Manual': 0, 'Automatic': 1}[transmission]

owner = st.selectbox('Select Owner Type:', ('First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'))
owner = {'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2, 'Fourth & Above Owner': 3, 'Test Drive Car': 4}[owner]

# mileage
mileage = st.number_input('Mileage (in Kmpl):', min_value=0.0, max_value=50.0, step=0.1)

# engine
engine = st.number_input('Engine Size (in cc):', min_value=500, max_value=5000, step=50)

# max_power
max_power = st.number_input('Max Power (in bhp):', min_value=30.0, max_value=500.0, step=1.0)

# torque
torque = st.number_input('Torque (in rpm):', min_value=10, max_value=10000, step=100)

# seats
seats = st.number_input('Number of Seats:', min_value=2, max_value=10, step=1)

# Gather user input into a dictionary
user_input = {
    'year': year,
    'km_driven': km_driven,
    'fuel': fuel,
    'seller_type': seller_type,
    'transmission': transmission,
    'owner': owner,
    'mileage(Kmpl)': mileage,
    'engine(cc)': engine,
    'max_power(bhp)': max_power,
    'torque(rpm)': torque,
    'seats': seats
}

# Prediction button on the main page
if st.button('Predict Price'):
    predicted_price = predict_car_price(user_input)
    st.success(f"The predicted car price is: ₹{predicted_price:.2f}")
