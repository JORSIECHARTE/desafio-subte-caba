# 🛠️ Desafío Subte CABA Etapa 1 Analisis Exploratorio

Análisis de datos de pasajeros del subte de la Ciudad de Buenos Aires. Se trabaja sobre datos públicos para visualizar el comportamiento de la demanda, accesibilidad, uso por línea, día y mes, entre otros factores.

---

## 📁 Estructura del proyecto

Subte-analisis/
├── etapa1_analisis_exploratorio/
│   ├── scripts/
│   │   ├── preparacion_datos.py
│   │   ├── analisis_demanda_diaria.py
│   │   ├── analisis_dias_laborales_vs_finde.py
│   │   ├── analisis_estaciones.py
│   │   ├── analisis_estaciones_accesibles.py
│   │   ├── analisis_evolucion_lineas.py
│   │   ├── analisis_frecuencia.py
│   │   ├── analisis_lineas_mas_usadas.py
│   │   ├── analisis_relacion_estaciones_linea.py
│   │   ├── analisis_uso_por_mes.py
│   │   
│   ├── visualizaciones/
│   │   └── *.png
│   └── informe/
│       └── informe_etapa1.md
├── Datos/
│   ├── dataset_viajes_sube.csv
│   ├── estaciones-de-subte.xlsx
│   └── viajes_anual.xlsx

---

📊 Análisis incluidos:

preparacion_datos.py: filtra y prepara el dataset para análisis.

analisis_demanda_diaria.py: pasajeros por día.

analisis_dias_laborales_vs_finde.py: días hábiles vs. fines de semana.

analisis_estaciones.py: mapa de estaciones por línea.

analisis_estaciones_accesibles.py: estaciones accesibles por línea.

analisis_evolucion_lineas.py: evolución anual por línea.

analisis_frecuencia.py: promedio de pasajeros por día de la semana.

analisis_lineas_mas_usadas.py: líneas más utilizadas.

analisis_relacion_estaciones_linea.py: relación entre estaciones y pasajeros.

analisis_uso_por_mes.py: uso mensual por año.

---

✅ Requisitos

Python 3.10+

Pandas

Matplotlib

Seaborn

openpyxl

adjustText

---

✍️ Autor
Proyecto desarrollado por Joaquín Orsi Echarte como parte del desafío de análisis de transporte subterráneo en la Ciudad de Buenos Aires.