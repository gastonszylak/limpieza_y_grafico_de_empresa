import pandas as pd
import numpy as np

data = {
    'ID': range(1, 21),
    'Fecha': pd.date_range(start='2026-01-01', periods=20, freq='D'),
    'Tipo_Servicio': ['Interior', 'Exterior', 'Impermeabilización', 'Reparación'] * 5,
    'Pintor': ['Juan', 'Pedro', 'Ana', 'Luis'] * 5,
    'Monto_Cobrado': [150000, 250000, np.nan, 80000, 300000, 120000, 450000, 200000, np.nan, 90000,
                      160000, 280000, 320000, 75000, 500000, 130000, 400000, 220000, 110000, 95000],
    'Satisfaccion_Cliente': [4, 5, 3, 2, 5, 4, 5, 4, 3, 2, 4, 5, 5, 1, 5, 4, 4, 3, 4, 2],
    'Region': ['San Rafael', 'Mendoza', 'General Alvear', 'San Rafael'] * 5
}

df = pd.DataFrame(data)
# Aplicamos los "errores" para practicar
df.loc[2, 'Monto_Cobrado'] = np.nan
df.loc[13, 'Satisfaccion_Cliente'] = 10
df.loc[5, 'Tipo_Servicio'] = ' interior '
df.to_csv('ventas_empresa_completo.csv', index=False)
print("Archivo 'ventas_empresa_completo.csv' creado exitosamente.")