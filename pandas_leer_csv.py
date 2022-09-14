import pandas as pd

df = pd.read_csv('archivos/Libro5.csv',sep=';')

print(df)

df["subtotal"]=df["Precio"]*df["Cantidad"]

print(df)

total=df["subtotal"].sum()

print(f"El total es {total}")
