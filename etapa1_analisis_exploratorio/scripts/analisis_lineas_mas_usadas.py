# analisis_lineas_mas_usadas.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Cargar y preparar datos ---
df_viajes = pd.read_excel("Datos/viajes_anual.xlsx")
df_viajes["linea"] = df_viajes["linea"].astype(str)
df_viajes["total"] = df_viajes["total"].astype(int)

# Agrupar por línea y calcular total acumulado
viajes_por_linea = df_viajes.groupby("linea")["total"].sum().sort_values(ascending=False)

# Mostrar tabla en consola
print("Total de pasajeros por línea (acumulado):")
print(viajes_por_linea)

# --- Visualización ---
plt.figure(figsize=(10, 6))
sns.barplot(x=viajes_por_linea.index, y=viajes_por_linea.values, palette="Set1")

plt.title("Total de pasajeros por línea de subte (acumulado)")
plt.xlabel("Línea")
plt.ylabel("Cantidad de pasajeros")
plt.grid(True)
plt.tight_layout()

# --- Guardar gráfico  ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/lineas_mas_utilizadas.png", dpi=300)

plt.show()
