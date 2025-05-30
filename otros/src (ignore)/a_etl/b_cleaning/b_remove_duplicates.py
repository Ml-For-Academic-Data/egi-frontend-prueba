# Elimina duplicados
import pandas as pd

def remove_duplicate_rows(df):
    """
    Elimina filas duplicadas basándose en todas las columnas.
    """
    print("Eliminando filas duplicadas...")
    initial_rows = len(df)
    df = df.drop_duplicates()
    final_rows = len(df)
    print(f"Filas eliminadas: {initial_rows - final_rows}")
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/student_data.csv")
    df_cleaned = remove_duplicate_rows(df)
    df_cleaned.to_csv("../processed/no_duplicates.csv", index=False)