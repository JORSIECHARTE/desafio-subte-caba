# analisis_uso_por_mes.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# --- Cargar y preparar datos ---
df = pd.read_csv("Datos/dataset_viajes_sube.csv")
df["TIPO_TRANSPORTE"] = df["TIPO_TRANSPORTE"].str.upper()
df_subte = df[(df["TIPO_TRANSPORTE"] == "SUBTE") & (df["CANTIDAD"].notnull())]

# Convertir columna 'DIA' a fecha
def limpiar_fecha(fecha_str):
    return datetime.strptime(fecha_str[:9], "%d%b%Y")

df_subte["FECHA"] = df_subte["DIA"].apply(limpiar_fecha)

# Extraer mes y año
df_subte["AÑO"] = df_subte["FECHA"].dt.year
df_subte["MES"] = df_subte["FECHA"].dt.month
df_subte["MES_LABEL"] = df_subte["MES"].apply(lambda x: f"{x:02d}")

# Agrupar por año y mes
viajes_por_mes = df_subte.groupby(["AÑO", "MES_LABEL"])["CANTIDAD"].sum().reset_index()

# --- Visualización ---
plt.figure(figsize=(12, 6))
sns.lineplot(data=viajes_por_mes, x="MES_LABEL", y="CANTIDAD", hue="AÑO", marker="o")
plt.title("Cantidad de pasajeros por mes (SUBTE)")
plt.xlabel("Mes")
plt.ylabel("Total de pasajeros")
plt.grid(True)
plt.tight_layout()

# --- Guardar gráfico  ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/pasajeros_por_mes.png", dpi=300)

plt.show()
