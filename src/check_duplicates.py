import pandas as pd
import logging

# Columnas que deberían ser únicas por fila
KEY_COLUMNS = ["email"]

def validate_duplicates(df: pd.DataFrame) -> bool:
    """
    Verifica que no haya duplicados en las columnas clave.

    Parámetros:
        df (pd.DataFrame): El DataFrame a validar

    Retorna:
        bool: True si no hay duplicados, False si se detectan
    """
    duplicados = df.duplicated(subset=KEY_COLUMNS).sum()

    if duplicados > 0:
        logging.error(f"❌ Se encontraron {duplicados} registros duplicados en columnas: {KEY_COLUMNS}")
        return False
    else:
        logging.info("✅ No se encontraron registros duplicados.")
        return True
