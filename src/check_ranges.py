import pandas as pd
import logging

# Rango válido para cada columna
RANGE_RULES = {
    "edad": {"min": 0, "max": 120}
}

def validate_ranges(df: pd.DataFrame) -> bool:
    """
    Verifica que los valores estén dentro de los rangos definidos.

    Retorna:
        bool: True si todo está dentro de los rangos, False si hay violaciones
    """
    errores = False

    for columna, regla in RANGE_RULES.items():
        if columna in df.columns:
            fuera_de_rango = df[
                (df[columna] < regla["min"]) | (df[columna] > regla["max"])
            ]

            if not fuera_de_rango.empty:
                logging.error(
                    f"❌ Columna '{columna}' tiene {len(fuera_de_rango)} valores fuera del rango {regla}"
                )
                errores = True

    if errores:
        logging.warning("⚠️ Validación de rangos fallida.")
        return False
    else:
        logging.info("✅ Validación de rangos superada.")
        return True
