# src/workout_insights/features.py

def compute_metrics(df):
    """Calcula métricas de treino: volume, frequência, intensidade."""
    # Exemplo: volume = sets * reps * weight
    df['volume'] = df['sets'] * df['reps'] * df['weight']
    return df
