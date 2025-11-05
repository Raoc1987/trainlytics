# src/trainlytics/clean.py
import pandas as pd

def clean_workout_data(df):
    """Clean and standardize the workout DataFrame."""
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    return df
