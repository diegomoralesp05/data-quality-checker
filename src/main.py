import pandas as pd
import logging

from src.check_schema import validate_schema
from src.check_nulls import validate_nulls
from src.check_duplicates import validate_duplicates
from src.check_ranges import validate_ranges
from src.report import configurar_logging, generar_resumen

def main():
    configurar_logging()
    logging.info("🚀 Iniciando validación de calidad de datos...")

    try:
        # 1. Cargar datos
        df = pd.read_csv("data/clientes.csv")
        logging.info(f"📄 Archivo cargado con {len(df)} registros.")

        # 2. Validaciones
        validaciones = {
            "Esquema": validate_schema(df),
            "Nulos": validate_nulls(df),
            "Duplicados": validate_duplicates(df),
            "Rangos": validate_ranges(df)
        }

        # 3. Resultado final
        resultado_final = all(validaciones.values())
        generar_resumen(resultado_final)

    except Exception as e:
        logging.exception(f"❌ Error crítico durante la ejecución: {e}")
        generar_resumen(False)

if __name__ == "__main__":
    main()
