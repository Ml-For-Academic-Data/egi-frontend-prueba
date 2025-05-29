# Crea nuevas columnas derivadas

import pandas as pd

def create_derived_features(df):
    """
    Crea nuevas características útiles a partir de datos existentes.
    """
    print("Creando nuevas características...")

    # Tasa de aprobación en el primer semestre
    df['tasa_aprobacion_1er_sem'] = df['Unidades curriculares 1st sem (aprobado)'] / df['Unidades curriculares 1st sem (inscritas)']
    df['tasa_aprobacion_1er_sem'] = df['tasa_aprobacion_1er_sem'].fillna(0)

    # Unidades no aprobadas
    df['unidades_no_aprobadas_1er_sem'] = df['Unidades curriculares 1st sem (inscritas)'] - df['Unidades curriculares 1st sem (aprobado)']

    # Edad categorizada
    df['edad_categoria'] = pd.cut(
        df['Edad en la inscripción'],
        bins=[0, 18, 22, 26, 30, 100],
        labels=['Menor de 18', '19-22', '23-26', '27-30', 'Mayor de 30']
    )

    print("Nuevas características creadas.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/student_data.csv")
    df_with_features = create_derived_features(df)
    df_with_features.to_csv("../processed/with_features.csv", index=False)