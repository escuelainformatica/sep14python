import pandas as pd

datos={
    "col1":[1,2,3],
    "col2":[4,5,6],
    "col3":[7,8,9]
}

df=pd.DataFrame(datos)  # dataframe

print(df)

series2=pd.Series([10,20,30])

print(df["col1"]) # series
print(series2)
print(df["col1"]*series2)