import pandas as pd
import os

def run_etl():
    print("Ejecutando ETL...")
    df = pd.read_csv("../data/student_data.csv")

    # Simular limpieza o transformaciones
    df['promedio_categoria'] = pd.cut(df['promedio'], bins=[0,3,4,5], labels=['Bajo','Medio','Alto'])
    
    os.makedirs("../processed", exist_ok=True)
    df.to_csv("../processed/cleaned_data.csv", index=False)
    print("ETL completado. Datos guardados en ../processed/cleaned_data.csv")

if __name__ == "__main__":
    run_etl()