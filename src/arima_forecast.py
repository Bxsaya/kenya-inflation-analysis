# src/arima_forecast.py (updated)
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(df):
    model = ARIMA(df['Inflation Rate'], order=(0,1,2))
    results = model.fit()
    forecast = results.get_forecast(steps=5)
    forecast_df = pd.DataFrame({
        'Year': pd.date_range(start=df['Year'].max(), periods=6, freq='YS')[1:].year,
        'Forecast': forecast.predicted_mean,
        'Lower_CI': forecast.conf_int().iloc[:, 0],
        'Upper_CI': forecast.conf_int().iloc[:, 1]
    })
    return forecast_df