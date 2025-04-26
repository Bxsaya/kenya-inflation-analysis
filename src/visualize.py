import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_report(arima_path, prophet_path, output_dir):
    # Load data
    arima_df = pd.read_csv(arima_path)
    prophet_df = pd.read_csv(prophet_path)
    
    # Create comparison plot
    plt.figure(figsize=(14, 6))
    plt.plot(arima_df['Year'], arima_df['Forecast'], label='ARIMA Forecast')
    plt.plot(prophet_df['ds'].str[:4], prophet_df['yhat'], label='Prophet Forecast')
    plt.xlabel('Year')
    plt.ylabel('Inflation Rate (%)')
    plt.title('ARIMA vs Prophet Forecast Comparison')
    plt.legend()
    plt.savefig(os.path.join(output_dir, "forecast_comparison.png"))
    
    # Generate markdown report
    with open(os.path.join(output_dir, "final_report.md"), 'w') as f:
        f.write("# Kenya Inflation Forecast Report\n")
        f.write("![Historical Trend](eda_plots/historical_trend.png)\n")
        f.write("![Forecast Comparison](forecasts/forecast_comparison.png)\n")

if __name__ == "__main__":
    arima_path = os.path.join("..", "results", "forecasts", "arima_forecast.csv")
    prophet_path = os.path.join("..", "results", "forecasts", "prophet_forecast.csv")
    output_dir = os.path.join("..", "results")
    generate_report(arima_path, prophet_path, output_dir)