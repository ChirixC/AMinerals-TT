import pandas as pd

def clean_data(df):
    """
    Limpia un DataFrame eliminando duplicados.
    
    Parameters:
    - df: DataFrame que contiene los datos a limpiar.
    
    Returns:
    - DataFrame limpio sin duplicados.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El parámetro debe ser un DataFrame de pandas.")
    
    # Elimina filas duplicadas
    df_cleaned = df.drop_duplicates()
    
    return df_cleaned