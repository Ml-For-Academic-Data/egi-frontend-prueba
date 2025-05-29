# /opt/airflow/src/utils/processing.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def handle_missing_values(**kwargs):
    input_path = kwargs['input_path']
    output_path = kwargs['output_path']

    print(f"Leyendo archivo: {input_path}")
    df = pd.read_csv(input_path)

    print("Manejando valores faltantes...")
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(df[col].median())

    print(f"Guardando archivo: {output_path}")
    df.to_csv(output_path, index=False)

def encode_categoricals(**kwargs):
    input_path = kwargs['input_path']
    output_path = kwargs['output_path']

    print(f"Leyendo archivo: {input_path}")
    df = pd.read_csv(input_path)

    print("Codificando variables categóricas...")
    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    print(f"Guardando archivo: {output_path}")
    df.to_csv(output_path, index=False)

def split_train_test(**kwargs):
    input_path = kwargs['input_path']
    train_output = kwargs['train_output']
    test_output = kwargs['test_output']

    print(f"Leyendo archivo: {input_path}")
    df = pd.read_csv(input_path)

    print("Dividiendo en train y test...")
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    print(f"Guardando archivos:")
    train_df.to_csv(train_output, index=False)
    test_df.to_csv(test_output, index=False)

def train_and_predict(**kwargs):
    train_path = kwargs['train_path']
    test_path = kwargs['test_path']
    output_path = kwargs['output_path']

    print(f"Leyendo train: {train_path}")
    print(f"Leyendo test: {test_path}")
    X_train = pd.read_csv(train_path)
    X_test = pd.read_csv(test_path)

    y_train = X_train.pop('target')  # Asegúrate de tener una columna 'target'
    y_test = X_test.pop('target')

    print("Entrenando modelo...")
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)

    print("Prediciendo...")
    predictions = model.predict(X_test)

    result = pd.DataFrame({'prediction': predictions})
    print(f"Guardando predicciones en: {output_path}")
    result.to_csv(output_path, index=False)