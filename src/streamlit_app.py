import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from preprocess import preprocess_data
from arima_forecast import arima_forecast
from prophet_forecast import prophet_forecast


st.set_page_config(page_title="Kenya Inflation Dashboard")

def main():
    st.title("Kenya Inflation Forecast")
    
    # Upload CSV
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file:
        raw_df = pd.read_csv(uploaded_file)
        cleaned_df = preprocess_data(raw_df)
        
        # Generate forecasts
        arima_results = arima_forecast(cleaned_df)
        prophet_results = prophet_forecast(cleaned_df)
        
        # Plotting
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(cleaned_df['Year'], cleaned_df['Inflation Rate'], label='Historical', marker='o')
        ax.plot(arima_results['Year'], arima_results['Forecast'], label='ARIMA Forecast', linestyle='--')
        ax.plot(prophet_results['ds'].dt.year, prophet_results['yhat'], label='Prophet Forecast', linestyle='--')
        ax.legend()
        st.pyplot(fig)
        
        # Show data
        st.subheader("Forecast Data")
        st.write("### ARIMA Forecast")
        st.dataframe(arima_results)
        st.write("### Prophet Forecast")
        st.dataframe(prophet_results)

if __name__ == "__main__":
    main()
