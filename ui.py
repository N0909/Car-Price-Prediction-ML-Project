import streamlit as st
import numpy as np 
import pickle

model = pickle.load(open("model.pkl",'rb'))
data = pickle.load(open("Car-Price-Prediction-ML-Project/data.pkl",'rb'))

st.title('Car Price Prediction')

#Make
make = st.selectbox('Make',data['Make'].unique())

#Year
year = st.number_input('Year')

#KM
km = st.number_input('KiloMeter')

#Fuel Type
fueltype = st.selectbox('Fuel Type',data['Fuel Type'].unique())

#Transmission
transmission = st.selectbox('Transmission',data['Transmission'].unique())

#Owner
owner = st.selectbox('Owner',data['Owner'].unique())

#Seller Type
seller_type = st.selectbox('Seller Type',data['Seller Type'].unique())

#Engine CC
engine_cc = st.number_input('Engine(CC)')

#Max power 
power = st.number_input('Max Power (bhp)')

#@powerrpm 
power_rpm = st.number_input('@ RPM')

#Max Torque
torque = st.number_input('Torque (nm)')

#@torquerpm
torque_rpm = st.number_input(' @ RPM')

#Drivetrain
drivetrain = st.selectbox('Drivetrain',data['Drivetrain'].unique())

#Length
length = st.number_input('Length (mm)')

#Width 
width = st.number_input('Width (mm)')

#Height
height = st.number_input('Height (mm)')

#Seating Capacity
seating_capacity = st.selectbox('Seating Capacity',data['Seating Capacity'].unique())

#Fuel Capacity
fuel_cap = st.number_input('Fuel tank Capacity (Litre)')



if st.button('Predict Price'):
    query = np.array([make,year,km,fueltype,transmission,owner,seller_type,engine_cc,power,torque,drivetrain,length,width,height,seating_capacity,fuel_cap,power_rpm,torque_rpm])
    query = query.reshape(1,18)
    price = round(int(np.exp(model.predict(query)[0])))

    st.title(f'Predicted Price:{price}')





