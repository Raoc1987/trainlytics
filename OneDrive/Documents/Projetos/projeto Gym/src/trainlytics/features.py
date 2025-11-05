# src/trainlytics/features.py
def compute_metrics(df):
    """Compute workout metrics: volume, frequency, intensity."""
    df['volume'] = df['sets'] * df['reps'] * df['weight']
    return df
