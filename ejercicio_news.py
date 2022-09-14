import pandas as pd

df = pd.read_csv('archivos/news_decline.csv', sep=', ', quotechar='"')  # nota el espacio en sep=', '

# print(df)
# print(df["Show"])
df["promedio"] = (df['"2009"'] + df['"2010"'] + df['"2011"']) / 3

print(df)
