# src/prophet_forecast.py (updated)
from prophet import Prophet

def prophet_forecast(df):
    prophet_df = df.rename(columns={'Year': 'ds', 'Inflation Rate': 'y'})
    model = Prophet(yearly_seasonality=False)
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=5, freq='Y')
    forecast = model.predict(future)
    return forecast.tail(5)