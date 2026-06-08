# 📊 Data Wrangling & Business Analytics: Limpieza y Optimización de Ventas

Este proyecto implementa un flujo completo de **Data Science** (Preprocesamiento y Análisis Exploratorio de Datos - EDA) aplicado a los registros históricos de ventas y operaciones de una empresa de servicios y retail. El objetivo principal es transformar datos crudos inconsistentes en un tablero visual confiable para la toma de decisiones gerenciales.

## 🛠️ Tecnologías y Librerías Utilizadas
* **Lenguaje:** Python
* **Manipulación de Datos:** Pandas, NumPy
* **Visualización Avanzada:** Matplotlib, Seaborn
* **Entorno de Desarrollo:** Visual Studio Code / Jupyter Notebooks

---

## 📂 Desafíos del Dataset y Soluciones Técnicas (Data Wrangling)

El archivo original presentaba los problemas típicos de la recolección de datos en el mundo real. Se aplicó un riguroso proceso de limpieza estructurado en fases:

1. **Identificación y Manejo de Valores Faltantes ($NaN$):** * Se detectaron caracteres espurios (como los signos `?`) y registros nulos en métricas operativas.
   * Se aplicó la técnica de **imputación por media estadística** (`.fillna()`) en variables continuas para preservar la tendencia central de los datos sin alterar las métricas globales.
2. **Corrección de Formato y Tipos de Datos:** * Se limpiaron símbolos monetarios (`$`) y puntos de miles incrustados en las columnas de precios mediante expresiones regulares (`regex=True`).
   * Se transformaron las variables a formatos numéricos nativos (`.astype(float)`) para posibilitar el cálculo de funciones matemáticas.
3. **Ingeniería de Características (Feature Engineering):**
   * **One-Hot Encoding (`pd.get_dummies`):** Se convirtieron las categorías de texto (tipos de materiales/servicios) en variables binarias ($0$ y $1$) para que los datos queden listos y optimizados para futuros modelos de Machine Learning.
   * **Normalización de Escalas (Min-Max Scaling):** Se comprimieron de forma proporcional los valores de facturación a un rango estricto entre $0$ y $1$ para neutralizar el sesgo de magnitud frente a variables de menor escala.
   * **Segmentación por Rangos (Binning):** Se categorizaron los volúmenes continuos empleando `np.linspace` y `pd.cut` para agrupar los registros en categorías lógicas de negocio (*Chica*, *Mediana*, *Grande*).

---

## 📈 Análisis Exploratorio Visual (EDA)

Una vez homogeneizada la estructura, se utilizaron **Seaborn y Matplotlib** para responder preguntas estratégicas de la dirección mediante gráficos profesionales:

### 🎯 Reporte de Facturación y Rendimiento Comercial
Se desarrolló un **Gráfico de Barras** (`sns.barplot`) optimizado para evaluar el flujo de caja e ingresos totales generados. Este gráfico permite identificar de un vistazo el rendimiento comercial segmentado por responsable, detectando quién tracciona el mayor volumen de facturación para la organización.

### 🔍 Análisis de Distribución y Detección de Outliers
Se implementó un **Diagrama de Caja** (*Boxplot*) para evaluar la dispersión de los costos logísticos y los precios cobrados. Esta visualización resulta crítica para:
* Identificar desviaciones estándar anómalas.
* Detectar gráficamente *outliers* o valores atípicos (puntos fuera de los bigotes) que puedan representar errores de carga o contratos excepcionales que distorsionen los promedios.

---

## 🚀 Conclusiones de Negocio (Insights)
* **Optimización Logística:** La segmentación por *Binning* demostró que el mayor porcentaje de las operaciones se concentra en la categoría *Mediana*, permitiendo prever de forma eficiente el stock y la compra anticipada de materiales.
* **Control de Desvíos:** El análisis visual de *outliers* permitió auditar celdas inconsistentes y contratos fuera de banda, asegurando políticas de precios estables y transparentes.

---

## 💻 Cómo Ejecutar el Proyecto

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/gastonszylak/tu-repositorio.git](https://github.com/gastonszylak/tu-repositorio.git)
