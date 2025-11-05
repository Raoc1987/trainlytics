# src/workout_insights/clean.py
import pandas as pd

def clean_workout_data(df):
    """Limpa e padroniza o DataFrame de treino."""
    # Exemplo: remover nulos, padronizar tipos
    df = df.dropna()
    df['date'] = pd.to_datetime(df['date'])
    return df
