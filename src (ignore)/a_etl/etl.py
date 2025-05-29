import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def run_etl():
    print("Ejecutando ETL...")
    
    # Cargar datos
    df = pd.read_csv("./data/student_data.csv")

    # Simular limpieza o transformaciones
    df['promedio_categoria'] = pd.cut(df['promedio'], bins=[0,3,4,5], labels=['Bajo','Medio','Alto'])

    # --- Nueva parte: Codificación de variables NO NUMÉRICAS ---
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns.tolist()

    if non_numeric_cols:
        print(f"Columnas no numéricas detectadas: {non_numeric_cols}")
    else:
        print("No se encontraron columnas no numéricas.")

    for col in non_numeric_cols:
        unique_values = df[col].nunique()
        if unique_values < 5:
            print(f"  → Aplicando One-Hot Encoding a '{col}' ({unique_values} valores únicos)")
            encoder = OneHotEncoder(sparse_output=False, drop='first')
            encoded = encoder.fit_transform(df[[col]])
            encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([col]))
            df = pd.concat([df.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)
            df.drop(col, axis=1, inplace=True)
        else:
            print(f"  → Aplicando Label Encoding a '{col}' ({unique_values} valores únicos)")
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])

    # --- Fin de codificación ---

    # Guardar datos procesados
    os.makedirs("./data/processed", exist_ok=True)
    df.to_csv("./data/processed/cleaned_data.csv", index=False)
    print("ETL completado. Datos guardados en ./data/processed/cleaned_data.csv")
    return df

if __name__ == "__main__":
    run_etl()