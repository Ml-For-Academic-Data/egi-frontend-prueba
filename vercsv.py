#Ver dataset en carpeta raiz

import pandas as pd
import os

df = pd.read_csv("./dataset.csv")

# print(df.columns)

#imprimir tipo de dato de cada columna
print(df.dtypes)
