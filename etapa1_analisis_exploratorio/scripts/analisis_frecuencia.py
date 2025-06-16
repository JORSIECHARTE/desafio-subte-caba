# analisis_frecuencia.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# --- Cargar y preparar datos ---
df = pd.read_csv("Datos/dataset_viajes_sube.csv")
df["TIPO_TRANSPORTE"] = df["TIPO_TRANSPORTE"].str.upper()

# Filtrar solo SUBTE con datos válidos
df_subte = df[df["TIPO_TRANSPORTE"] == "SUBTE"]
df_subte_con_datos = df_subte[df_subte["CANTIDAD"].notnull()]

# Convertir columna 'DIA' a formato fecha
def limpiar_fecha(fecha_str):
    return datetime.strptime(fecha_str[:9], "%d%b%Y")

df_subte_con_datos["FECHA"] = df_subte_con_datos["DIA"].apply(limpiar_fecha)

# Obtener nombre del día de la semana
df_subte_con_datos["DIA_SEMANA"] = df_subte_con_datos["FECHA"].dt.day_name()

# Calcular promedio de pasajeros por día
frecuencia_por_dia = df_subte_con_datos.groupby("DIA_SEMANA")["CANTIDAD"].mean().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])

# --- Visualización ---
plt.figure(figsize=(10, 6))
sns.barplot(x=frecuencia_por_dia.index, y=frecuencia_por_dia.values, palette="pastel")

plt.title("Promedio de pasajeros por día de la semana (SUBTE)")
plt.xlabel("Día de la semana")
plt.ylabel("Pasajeros promedio")
plt.grid(True)
plt.tight_layout()

# --- Guardar gráfico ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/promedio_pasajeros_por_dia_semana.png", dpi=300)

plt.show()
