# src/preprocess.py (updated)
import pandas as pd

def preprocess_data(df):
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    df['Inflation Rate'] = pd.to_numeric(df['Inflation Rate'], errors='coerce')
    df = df.dropna()
    return df