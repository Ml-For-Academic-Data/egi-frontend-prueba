# Filtra o corrige outliers

import pandas as pd
import numpy as np

def filter_numeric_outliers(df):
    """
    Detecta y elimina outliers usando el método IQR en columnas numéricas.
    """
    print("Filtrando outliers...")
    numeric_cols = df.select_dtypes(include=['number']).columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

    print("Outliers filtrados.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/student_data.csv")
    df_cleaned = filter_numeric_outliers(df)
    df_cleaned.to_csv("../processed/no_outliers.csv", index=False)