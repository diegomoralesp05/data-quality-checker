# ✅ Validador de Calidad de Datos

Este proyecto implementa un validador de calidad de datos en Python, que verifica automáticamente:

- ✅ Esquema (columnas requeridas)
- ✅ Valores nulos en columnas críticas
- ✅ Duplicados en claves únicas
- ✅ Rangos válidos para variables numéricas

## 📁 Estructura

data-quality-checker/
├── data/ # Archivos CSV de entrada
├── output/ # Reporte de calidad generado
├── rules/ # Reglas futuras (en YAML o JSON)
├── src/ # Código fuente modular
├── README.md
└── .gitignore


## 🚀 Cómo ejecutar

1. Clona el repositorio
2. Instala dependencias (solo `pandas`)
3. Ejecuta el validador:

```bash
python -m src.main
