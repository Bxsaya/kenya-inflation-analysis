# ARIMA Configuration
ARIMA_ORDER = (0, 1, 2)  # (p, d, q)

# Prophet Configuration
PROPHET_PARAMS = {
    'yearly_seasonality': False,
    'changepoint_prior_scale': 0.1
}

# General Settings
FORECAST_YEARS = 5