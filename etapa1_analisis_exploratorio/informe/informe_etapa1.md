# 📊 Informe Etapa 1 - Análisis Exploratorio

**Proyecto:** Análisis de datos de viajes en Subte CABA  
**Autor:** Joaquín Orsi Echarte  
**Fecha:** Junio 2025

---

## 🎯 Objetivos de la Etapa

- Realizar un análisis exploratorio inicial sobre el uso del subte.
- Identificar patrones generales de movilidad: días, líneas, meses.
- Crear visualizaciones representativas que faciliten la comprensión de los datos.
- Establecer las bases para las siguientes etapas de limpieza y modelado.

---

## 🗃️ Datos Utilizados

Se utilizó el archivo `dataset_viajes_sube.csv`, ubicado en la carpeta raíz del proyecto dentro de `datos/`.

Contiene información desagregada por tipo de transporte, cantidad de viajes, día y otras columnas relevantes.

---

## 🧪 Scripts desarrollados

Se trabajó sobre 9 scripts organizados en `etapa1_analisis_exploratorio/scripts/`:

| Archivo                          | Propósito principal                                                                 |
|----------------------------------|--------------------------------------------------------------------------------------|
| `preparacion_datos.py`          | Limpieza inicial y generación del dataset `df_subte_con_datos` para todos los scripts |
| `analisis_demanda_diaria.py`    | Evolución diaria de la demanda de viajes en subte                                    |
| `analisis_dias_laborales_vs_finde.py` | Comparación entre días laborales y fines de semana                               |
| `analisis_frecuencia.py`        | Promedio de uso por día de la semana                                                 |
| `analisis_uso_por_mes.py`       | Evolución mensual de pasajeros                                                       |
| `analisis_evolucion_lineas.py`  | Evolución anual por línea de subte                                                   |
| `analisis_lineas_mas_usadas.py` | Líneas más utilizadas en total acumulado                                             |
| `analisis_estaciones_accesibles.py` | Estaciones accesibles por línea                                                   |
| `analisis_relacion_estaciones_linea.py` | Relación entre cantidad de estaciones y pasajeros por línea                   |
| `analisis_estaciones.py`        | Mapa geográfico de estaciones por línea                                              |

---

## 📈 Visualizaciones generadas

Las visualizaciones se guardaron en la carpeta `visualizaciones/`. Entre las más destacadas se encuentran:

- **demanda_diaria_subte.png:** muestra cómo varía la cantidad de pasajeros por día.
- **pasajeros_por_tipo_de_dia.png:** compara uso laboral vs fines de semana.
- **promedio_pasajeros_por_dia_semana.png:** revela los días con mayor flujo.
- **pasajeros_por_mes.png:** evolución mensual de la demanda.
- **evolucion_pasajeros_por_linea.png:** línea por línea, evolución anual.
- **lineas_mas_utilizadas.png:** suma total por línea.
- **estaciones_accesibles_por_linea.png:** accesibilidad por línea.
- **relacion_estaciones_vs_pasajeros.png:** relación entre estaciones disponibles y cantidad de usuarios.
- **mapa_estaciones_por_linea.png:** visualización geográfica del subte.

---

## 📌 Conclusiones

- Las líneas con mayor uso acumulado fueron la B y la D.
- Se identifican caídas de demanda en ciertos años, posiblemente por pandemia.
- Los días laborales tienen un flujo notablemente más alto que los fines de semana.
- Algunas líneas tienen muchas estaciones, pero no necesariamente mayor demanda.
- La accesibilidad todavía presenta disparidades entre líneas.

Este análisis permitió sentar una base sólida para continuar con la **Etapa 2: Limpieza y Transformación**, asegurando que las decisiones de limpieza estarán bien fundamentadas.

---

## 🗂️ Estructura del Proyecto hasta la Etapa 1

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
│   │   └── analisis_uso_por_mes.py
│   │   
│   ├── visualizaciones/
│   │   └── *.png
│   └── informe/
│       └── informe_etapa1.md
└── Datos/
    ├── dataset_viajes_sube.csv
    ├── estaciones-de-subte.xlsx
    └── viajes_anual.xlsx
