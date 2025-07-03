# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 11:07:06 2025

@author: admin
"""

import pickle
import streamlit as st
import numpy as np

wea=pickle.load(open('weather.sav','rb'))

def weather_pre(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=wea.predict(input_data_reshaped)
    
    if (prediction[0]==0):
      print('The weather is cloudy')
    elif(prediction[0]==1):
      print('The weather is rainy')
    elif (prediction[0]==2):
      print('The weather is snowy ')
    else:
      print('The weather is sunny')
      
def main():
    st.title('🌥️ Weather Prediction Web App')
    
    col1,col2,col3=st.columns(3)
    # Input fields
    with col1:
        Temperature = st.text_input('🌡️ Temperature')
    with col2:
        Humidity = st.text_input('💧 Humidity')
    with col3:
        Wind_Speed = st.text_input('🌪️ Wind Speed')
    with col1:
        Preciptitation = st.text_input('🌧️ Preciptitation (%)')
    with col2:
        Cloud_Cover = st.text_input('☁️ Cloud Cover')
    with col3:
        Atmospheric_Pressure= st.text_input('💨 Atmospheric Pressure')
    with col1:
        UV_Index = st.text_input('☀️ UV Index')
    with col2:
        Season = st.text_input('🌞 Season')
    with col3:
        Visibility = st.text_input('🌫️ Visibility (km)')
    with col1:
        Location = st.text_input('📍 Location')

    diagnosis = ''

    # Button for prediction
    if st.button('Weather Type Result'):
        try:
            # Convert inputs and predict
            input_list = [float(Temperature), float(Humidity), float(Wind_Speed),
                          float(Preciptitation), float(Cloud_Cover), float(Atmospheric_Pressure),
                          float(UV_Index), float(Season),float(Visibility),float(Location)]
            diagnosis = weather_pre(input_list)
            
            
        except ValueError:
            diagnosis = "Please enter valid numeric values in all fields."

    st.success(diagnosis)
main()
