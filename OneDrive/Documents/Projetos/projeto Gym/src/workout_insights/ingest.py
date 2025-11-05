# src/workout_insights/ingest.py
import pandas as pd

def load_workout_csv(path):
    """Carrega um CSV de logs de treino."""
    return pd.read_csv(path)
