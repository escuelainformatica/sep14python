import pandas as pd

datos={
    "Enero":[10,20],   # Enero, febrero, marzo son las columnas
    "Febrero":[12,33], # [12,33] son los valores para cada column
    "Marzo":[33,44]
}
df=pd.DataFrame(datos)
print(df)

print(df.iloc[0])  # primera fila

# Crear un dataframe, y usando CocaCola, Fanta como indices
df=pd.DataFrame(datos,["Cocacola","Fanta"])

print(df)

print(df.loc["Cocacola"])  # primera fila

