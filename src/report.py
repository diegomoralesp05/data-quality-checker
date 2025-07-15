import logging
import os
from datetime import datetime

def configurar_logging():
    """
    Configura logging para guardar registros en output/reporte_calidad.log
    """
    os.makedirs("output", exist_ok=True)

    logging.basicConfig(
        filename="output/reporte_calidad.log",
        level=logging.INFO,
        filemode="w",  # sobrescribe si ya existe
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def generar_resumen(final_status: bool):
    """
    Agrega un resumen final al log.

    Parámetros:
        final_status (bool): True si todo está OK, False si hubo errores.
    """
    logging.info("-" * 50)
    if final_status:
        logging.info("✅ TODOS LOS CHEQUEOS SUPERADOS. Calidad de datos: APROBADA.")
    else:
        logging.warning("❌ Algunos chequeos fallaron. Calidad de datos: RECHAZADA.")
    logging.info("-" * 50)
