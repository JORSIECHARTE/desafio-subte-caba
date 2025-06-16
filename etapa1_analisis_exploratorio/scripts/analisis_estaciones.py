# analisis_estaciones.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text

# --- Cargar archivo de estaciones ---
df_estaciones = pd.read_excel("Datos/estaciones-de-subte.xlsx")

# --- Crear gráfico base ---
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=df_estaciones,
    x="long",
    y="lat",
    hue="linea",
    palette="tab10",
    s=80,
    edgecolor="black"
)

# --- Título y etiquetas ---
plt.title("Mapa de Estaciones de Subte por Línea")
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.legend(title="Línea", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# --- Añadir nombres de estaciones sin solapamientos ---
textos = [
    plt.text(row["long"] + 0.0005, row["lat"], row["estacion"], fontsize=7)
    for _, row in df_estaciones.iterrows()
]
adjust_text(textos, arrowprops=dict(arrowstyle="-", color='gray', lw=0.5))

plt.tight_layout()

# --- Guardar gráfico ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/mapa_estaciones_por_linea.png", dpi=300)


plt.show()
