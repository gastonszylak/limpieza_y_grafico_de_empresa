import pandas as pd
import numpy as np

df=pd.read_csv("anaul.csv")
print(df.info(6))
print(df.head(12))

# Convertir a string, quitar comas, y forzar a número
df['Value'] = df['Value'].astype(str).str.replace(',', '', regex=False)
df['Value'] = pd.to_numeric(df['Value'], errors='coerce') # Los errores se vuelven NaN

# Sumar el total de ingresos por tipo de industria
resumen = df.groupby('Industry_name_NZSIOC')['Value'].sum()

# Ordenar de mayor a menor y mostrar los 5 principales
print(resumen.sort_values(ascending=False).head(5))



