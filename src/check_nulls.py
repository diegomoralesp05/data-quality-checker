import pandas as pd
import logging

# Columnas donde no se permiten valores nulos
COLUMNS_NOT_NULL = ["id", "nombre", "email", "fecha_registro"]

def validate_nulls(df: pd.DataFrame) -> bool:
    """
    Verifica que no haya nulos en las columnas obligatorias.

    Parámetros:
        df (pd.DataFrame): El DataFrame a validar

    Retorna:
        bool: True si no hay nulos en las columnas clave, False si se encuentran
    """
    errores = False

    for col in COLUMNS_NOT_NULL:
        nulos = df[col].isnull().sum()

        if nulos > 0:
            logging.error(f"❌ Columna '{col}' contiene {nulos} valores nulos.")
            errores = True

    if errores:
        logging.warning("⚠️ Validación de nulos fallida.")
        return False
    else:
        logging.info("✅ Validación de nulos superada.")
        return True
