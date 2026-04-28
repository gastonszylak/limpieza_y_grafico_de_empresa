import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#CARGA DE ARCHIVO
df=pd.read_csv("ventas_empresa_completo.csv")

#INSPECCION RAPIDA
print(df.info())
print(df.head())

#LIMPIAMOS DATOS
df["Tipo_Servicio"] = df["Tipo_Servicio"].str.strip().str.capitalize()
df["Monto_Cobrado"] = df["Monto_Cobrado"].fillna(
    df.groupby("Tipo_Servicio")["Monto_Cobrado"].transform("median")
)
df["Satisfaccion_Cliente"] = df["Satisfaccion_Cliente"].clip(upper=5)

#UTILIZAR GRAFICOS
plt.figure(figsize=(5,6))
sns.barplot(data=df, x="Tipo_Servicio" , y="Monto_Cobrado" , estimator="mean")
plt.title("Promedio de monto cobrado por servicio")
plt.show()