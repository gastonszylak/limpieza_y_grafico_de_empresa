import pandas as pd
ruta_archivo = "C:\\Program Files\\anaul.csv"
df = pd.read_csv(ruta_archivo)
print(df.head(9))

