import pandas as pd

def analyze(df: pd.DataFrame):
    required = {'provincia', 'comune', 'popolazione', 'superficie_km2'}
    if not required.issubset(df.columns):
        raise ValueError('Colonne mancanti')
    x = df.copy()
    if x[list(required)].isna().any().any():
        raise ValueError('Valori mancanti')
    for col in ['popolazione', 'superficie_km2']:
        x[col] = pd.to_numeric(x[col], errors='raise')
        if not x[col].map(__import__('math').isfinite).all():
            raise ValueError('Valori non finiti')
    if (x['popolazione'] < 0).any() or (x['superficie_km2'] <= 0).any():
        raise ValueError('Valori non validi')
    x['densita'] = x['popolazione'] / x['superficie_km2']
    agg = x.groupby('provincia', as_index=False).agg(popolazione=('popolazione', 'sum'), superficie_km2=('superficie_km2', 'sum'))
    agg['densita'] = agg['popolazione'] / agg['superficie_km2']
    return (x, agg)
