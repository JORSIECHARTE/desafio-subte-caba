# analisis_estaciones_accesibles.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Cargar archivo de estaciones accesibles ---
df_accesibles = pd.read_excel("Datos/estaciones-accesibles.xlsx")

# --- Agrupar por línea y contar accesibles ---
conteo_lineas = df_accesibles.groupby("linea")["estacion"].count().sort_values(ascending=False)

# --- Mostrar resultados en consola ---
print("Cantidad de estaciones accesibles por línea:")
print(conteo_lineas)

# --- Visualización ---
plt.figure(figsize=(8, 5))
sns.barplot(x=conteo_lineas.index, y=conteo_lineas.values, hue=conteo_lineas.index, palette="Set2", legend=False)
plt.title("Estaciones accesibles por línea de subte")
plt.xlabel("Línea")
plt.ylabel("Cantidad de estaciones accesibles")
plt.tight_layout()

# --- Guardar gráfico  ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/estaciones_accesibles_por_linea.png", dpi=300)


plt.show()
