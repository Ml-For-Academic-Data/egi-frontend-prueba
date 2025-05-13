# etl.py
import pandas as pd
import os

def load_and_clean_data(input_path="data/student_data.csv", output_path="data/cleaned_data.csv"):
    print(f"[ETL] Cargando datos desde {input_path}")
    df = pd.read_csv(input_path)

    print("[ETL] Limpiando datos...")
    # Eliminar duplicados
    df.drop_duplicates(inplace=True)

    # Rellenar valores faltantes (si los hubiera)
    df.fillna({
        "promedio": df["promedio"].mean(),
        "asistencia": df["asistencia"].median()
    }, inplace=True)

    print(f"[ETL] Guardando datos limpios en {output_path}")
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    load_and_clean_data()