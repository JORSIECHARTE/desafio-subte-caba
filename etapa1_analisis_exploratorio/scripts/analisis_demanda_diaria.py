# analisis_demanda_diaria.py

import pandas as pd
import matplotlib.pyplot as plt
from etapa1_analisis_exploratorio.scripts.preparacion_datos import df_subte_con_datos

# --- Agrupar por fecha y sumar pasajeros ---
viajes_por_dia = df_subte_con_datos.groupby("FECHA")["CANTIDAD"].sum()

# --- Visualización ---
plt.figure(figsize=(12, 6))
viajes_por_dia.plot(kind="line", marker="o")
plt.title("Cantidad de pasajeros por día - SUBTE")
plt.xlabel("Fecha")
plt.ylabel("Cantidad de pasajeros")
plt.grid(True)
plt.tight_layout()

# --- Guardar el gráfico  ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/demanda_diaria_subte.png", dpi=300)

plt.show()
