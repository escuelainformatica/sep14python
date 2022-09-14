import pandas as pd
import numpy as np



datos={
    "col1":[1,2,3],
    "col2":[4,5,6],
    "col3":[7,8,9]
}

df=pd.DataFrame(datos)  # dataframe
print(df)

arreglo=np.array(df)   # nd-array (arreglo de numpy)
print(arreglo)

