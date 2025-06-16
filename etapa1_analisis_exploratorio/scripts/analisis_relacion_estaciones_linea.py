# analisis_relacion_estaciones_linea.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Cargar datos de estaciones ---
df_estaciones = pd.read_excel("Datos/estaciones-de-subte.xlsx")
conteo_estaciones = df_estaciones.groupby("linea")["estacion"].count().rename("estaciones")

# --- Cargar datos de viajes ---
df_viajes = pd.read_excel("Datos/viajes_anual.xlsx")
df_viajes["linea"] = df_viajes["linea"].astype(str)
df_viajes["total"] = df_viajes["total"].astype(int)
viajes_por_linea = df_viajes.groupby("linea")["total"].sum().rename("pasajeros")

# --- Unir datasets ---
comparacion = pd.concat([conteo_estaciones, viajes_por_linea], axis=1)
comparacion = comparacion.dropna().sort_values("pasajeros", ascending=False)

# --- Verificación por consola ---
print("\n Estaciones vs. Pasajeros por línea:")
print(comparacion)

# --- Visualización ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=comparacion, x="estaciones", y="pasajeros", hue=comparacion.index, s=100)

plt.title("Relación entre cantidad de estaciones y pasajeros por línea")
plt.xlabel("Cantidad de estaciones")
plt.ylabel("Cantidad total de pasajeros")
plt.grid(True)
plt.tight_layout()

# --- Guardar gráfico  ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/relacion_estaciones_vs_pasajeros.png", dpi=300)

plt.show()
