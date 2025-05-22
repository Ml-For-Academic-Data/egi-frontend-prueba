# Limpieza: valores faltantes

import pandas as pd
import sys
import os

# Añade el directorio raíz del proyecto al path
sys.path.append(os.path.abspath("../../../"))

# # Agrega la carpeta src al path para imports globales
# SRC_PATH = os.path.abspath(os.path.dirname(__file__) + "/../../")
# if SRC_PATH not in sys.path:
#     sys.path.insert(0, SRC_PATH)
    
from utils import save_backup
backup_path = "../../../data/backups/"

def handle_missing_values(df):
    """
    Maneja los valores faltantes del DataFrame:
    - Rellena categóricas con 'Unknown' o el valor más frecuente
    - Rellena numéricas con la mediana
    """
    print("Manejando valores faltantes...")

    save_backup(df, backup_path + "before_cleaning")

    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == "object":
                # Para variables categóricas
                df[col] = df[col].fillna("Unknown")
            else:
                # Para variables numéricas
                df[col] = df[col].fillna(df[col].median())

    print("Valores faltantes tratados.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/student_data.csv")
    df_cleaned = handle_missing_values(df)
    df_cleaned.to_csv("../processed/handled_missing.csv", index=False)