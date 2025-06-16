# analisis_dias_laborales_vs_finde.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from etapa1_analisis_exploratorio.scripts.preparacion_datos import df_subte_con_datos

# --- Asignar tipo de día ---
df_subte_con_datos["FRANJA"] = df_subte_con_datos["PARCIAL"].map({
    True: "Día Laboral",
    False: "Fin de Semana / No Laboral"
})

# --- Agrupar por tipo de día ---
viajes_por_franja = df_subte_con_datos.groupby("FRANJA")["CANTIDAD"].sum().sort_values(ascending=False)

# --- Mostrar resultados en consola ---
print("Cantidad total de pasajeros por tipo de día:")
print(viajes_por_franja)

# --- Visualización ---
plt.figure(figsize=(8, 5))
sns.barplot(x=viajes_por_franja.index, y=viajes_por_franja.values, palette="pastel")
plt.title("Cantidad total de pasajeros por tipo de día")
plt.xlabel("Tipo de día")
plt.ylabel("Total de pasajeros")
plt.tight_layout()

# --- Guardar gráfico ---
plt.savefig("etapa1_analisis_exploratorio/visualizaciones/pasajeros_por_tipo_de_dia.png", dpi=300)

plt.show()
