# preparacion_datos.py

import pandas as pd
from datetime import datetime

# --- Función auxiliar para limpiar fechas ---
def limpiar_fecha(fecha_str):
    """Convierte fecha en formato 'ddMMMyyyy...' a datetime."""
    return datetime.strptime(fecha_str[:9], "%d%b%Y")

# --- Cargar y preparar datos SUBTE ---
ruta_archivo = "Datos/dataset_viajes_sube.csv"
df = pd.read_csv(ruta_archivo)
df["TIPO_TRANSPORTE"] = df["TIPO_TRANSPORTE"].str.upper()

# Filtrar solo registros de SUBTE con datos válidos
df_subte = df[(df["TIPO_TRANSPORTE"] == "SUBTE") & (df["CANTIDAD"].notnull())]
df_subte.loc[:, "FECHA"] = df_subte["DIA"].apply(limpiar_fecha)

# Exportar DataFrame para otros módulos
df_subte_con_datos = df_subte

# --- Test local (solo si se ejecuta directamente) ---
if __name__ == "__main__":
    print(df_subte_con_datos.head())

