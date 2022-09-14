import pandas as pd
import numpy as np


datos={
    "col1":[1,2.3,3],
    "col2":[4,5,6],
    "col3":[7,8,9]
}
print("dataframe:")
df=pd.DataFrame(datos)  # dataframe
print(df)
print("series:")
col1=df["col1"]  # series
print(col1)
print("nd-array:")
arreglo=np.array(df)   # nd-array (arreglo de numpy)
print(arreglo)

