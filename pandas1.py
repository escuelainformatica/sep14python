import pandas as pd   # voy a importar (usar) la libreria de pandas y voy a usar el alias "pd"

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

print(df.sum(axis=0))