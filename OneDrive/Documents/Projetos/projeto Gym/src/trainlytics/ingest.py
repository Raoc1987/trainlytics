# src/trainlytics/ingest.py
import pandas as pd

def load_workout_csv(path):
    """Load a CSV file with workout logs."""
    return pd.read_csv(path)
