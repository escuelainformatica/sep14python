import pandas as pd

df = pd.read_csv('archivos/meses.csv',sep=';',decimal=",")

# print(df)
# operar filas a filas
df["total"]=df["Enero"]+df["Febrero"]+df["Marzo"]+df["Abril"]+df["Mayo"]

enero=df["Enero"].sum()

print(df)

print(f"Enero: {enero}")