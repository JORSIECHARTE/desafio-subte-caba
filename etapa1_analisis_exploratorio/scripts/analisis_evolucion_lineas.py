# analisis_evolucion_lineas.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Cargar archivo de viajes anuales por línea ---
df_viajes = pd.read_excel("Datos/viajes_anual.xlsx")

# --- Asegurar tipos correctos ---
df_viajes["linea"] = df_viajes["linea"].astype(str)
df_viajes["year"] = df_viajes["year"].astype(int)
df_viajes["total"] = df_viajes["total"].astype(int)

# --- Crear gráfico de evolución ---
plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df_viajes,
    x="year",
    y="total",
    hue="linea",
    marker="o",
    palette="tab10"
)

plt.title("Evolución de pasajeros por línea de subte (por año)")
plt.xlabel("Año")
plt.ylabel("Cantidad de pasajeros")
plt.grid(True)
plt.tight_layout()

# --- Guardar gráfico  ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/evolucion_pasajeros_por_linea.png", dpi=300)

plt.show()
