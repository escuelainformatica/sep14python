import pandas as pd

datos={
    "nombre":["cocacola","fanta","sprite"],
    "precio":[2000,500,100],
    "cantidad":[3,4,2]
}

df=pd.DataFrame(datos)
print(df)
print("primera fila:")
print(df.iloc[0])
print("precio x cantidad:")

multiplicacion=df["precio"]*df["canLibro5.csvtidad"]  # Series

print(multiplicacion.sum())


