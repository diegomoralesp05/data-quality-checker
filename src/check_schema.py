import pandas as pd
import logging

# Lista de columnas que deben estar presentes
COLUMNS_REQUIRED = ["id", "nombre", "edad", "email", "fecha_registro"]

def validate_schema(df: pd.DataFrame) -> bool:
    """
    Verifica que el DataFrame tenga todas las columnas requeridas.

    Parámetros:
        df (pd.DataFrame): El DataFrame cargado desde el archivo CSV

    Retorna:
        bool: True si el esquema es válido, False si faltan columnas
    """
    columnas_actuales = df.columns.tolist()
    faltantes = [col for col in COLUMNS_REQUIRED if col not in columnas_actuales]

    if faltantes:
        logging.error(f"❌ Faltan las siguientes columnas requeridas: {faltantes}")
        return False
    else:
        logging.info("✅ Esquema validado correctamente.")
        return True
