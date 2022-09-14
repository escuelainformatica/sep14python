import pandas as pd
import numpy as np
import funcion

datos={
    "libro":["libro1","libro2","libro3","libro4"],
    "categoria":["cat1","cat1","cat2","cat1"],
    "precio":[100,200,300,300],
    "cantpaginas":[500,400,600,400],
    "autor":["autor1","autor2","autor3","autor4"]
}

df=pd.DataFrame(datos,["Indice1","Indice2","Indice3","Indice4"])
df.rename_axis(index="Indice")

print(df)

agrupado=df.groupby(['categoria']).count()

print(agrupado)

agrupado_precio=df.groupby(['precio']).count()

print(agrupado_precio)
# filtrado
df_filtado=df[df['categoria']=='cat1']

print(df_filtado)

# modificar
df['libro']=df['libro'].apply(lambda fila: funcion.convertir(fila))  # por cada fila, transformar cada valor en mayuscula

print(df)

