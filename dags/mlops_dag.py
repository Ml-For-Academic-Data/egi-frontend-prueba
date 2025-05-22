# # Tu DAG principal en Airflow
# import sys
# import os
# from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.utils.task_group import TaskGroup
# from airflow.operators.dummy import DummyOperator


# # Añadimos src/ al path para poder importar nuestros módulos
# # SRC_PATH = os.path.abspath("../src/")
# SRC_PATH = "/opt/airflow/src"
# if SRC_PATH not in sys.path:
#     sys.path.insert(0, SRC_PATH)

# # Importa los scripts del pipeline
# from a_etl.b_cleaning.a_handle_missing import handle_missing_values
# from a_etl.b_cleaning.b_remove_duplicates import remove_duplicate_rows
# from a_etl.b_cleaning.c_filter_outliers import filter_numeric_outliers
# from a_etl.b_cleaning.d_create_features import create_derived_features

# default_args = {
#     "owner": "airflow",
#     "start_date": datetime(2025, 1, 1),
# }

# with DAG(
#     dag_id="mlops_dropout_prediction",
#     default_args=default_args,
#     schedule_interval="@daily",
#     catchup=False
# ) as dag:

#     start = DummyOperator(task_id="start")

#     from a_etl.b_cleaning import build_cleaning_group
    
#     cleaning_group = build_cleaning_group(dag)

#     end = DummyOperator(task_id="end")

#     start >> cleaning_group >> end



# DAG con algunas ramas simples
import sys
import os
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
import pandas as pd

# Añadimos src/ al path para poder importar nuestros módulos
SRC_PATH = "/opt/airflow/src"
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

# Importa los scripts del pipeline
from a_etl.b_cleaning.a_handle_missing import handle_missing_values
from a_etl.b_cleaning.b_remove_duplicates import remove_duplicate_rows
from a_etl.b_cleaning.c_filter_outliers import filter_numeric_outliers
from a_etl.b_cleaning.d_create_features import create_derived_features

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
}

# Funciones para las tareas
def load_data_task():
    """Carga los datos iniciales"""
    df = pd.read_csv("/opt/airflow/data/raw/student_data.csv")
    df.to_csv("/opt/airflow/data/temp/step0_raw_data.csv", index=False)
    print(f"Datos cargados: {df.shape}")

def handle_missing_task():
    """Maneja valores faltantes"""
    df = pd.read_csv("/opt/airflow/data/temp/step0_raw_data.csv")
    df_cleaned = handle_missing_values(df)
    df_cleaned.to_csv("/opt/airflow/data/temp/step1_missing_handled.csv", index=False)
    print(f"Valores faltantes manejados: {df_cleaned.shape}")

def remove_duplicates_task():
    """Remueve duplicados"""
    df = pd.read_csv("/opt/airflow/data/temp/step1_missing_handled.csv")
    df_cleaned = remove_duplicate_rows(df)
    df_cleaned.to_csv("/opt/airflow/data/temp/step2_duplicates_removed.csv", index=False)
    print(f"Duplicados removidos: {df_cleaned.shape}")

def filter_outliers_task():
    """Filtra outliers"""
    df = pd.read_csv("/opt/airflow/data/temp/step1_missing_handled.csv")  # También desde step1
    df_cleaned = filter_numeric_outliers(df)
    df_cleaned.to_csv("/opt/airflow/data/temp/step2b_outliers_filtered.csv", index=False)
    print(f"Outliers filtrados: {df_cleaned.shape}")

def create_features_task():
    """Crea features derivadas combinando ambos paths"""
    # Leer ambos archivos procesados
    df1 = pd.read_csv("/opt/airflow/data/temp/step2_duplicates_removed.csv")
    df2 = pd.read_csv("/opt/airflow/data/temp/step2b_outliers_filtered.csv")
    
    # Usar el que tenga más filas (ejemplo de lógica simple)
    df_to_use = df1 if len(df1) > len(df2) else df2
    
    df_final = create_derived_features(df_to_use)
    df_final.to_csv("/opt/airflow/data/processed/cleaned_data.csv", index=False)
    print(f"Features creadas: {df_final.shape}")

def generate_report_task():
    """Genera un reporte simple"""
    df = pd.read_csv("/opt/airflow/data/processed/cleaned_data.csv")
    
    report = f"""
    REPORTE DE LIMPIEZA DE DATOS
    ============================
    Total de filas: {len(df)}
    Total de columnas: {len(df.columns)}
    Valores nulos restantes: {df.isnull().sum().sum()}
    
    Columnas: {', '.join(df.columns.tolist())}
    """
    
    with open("/opt/airflow/data/processed/cleaning_report.txt", "w") as f:
        f.write(report)
    
    print("Reporte generado")

# Definir el DAG
with DAG(
    dag_id="mlops_dropout_prediction",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    # Tareas del pipeline
    start = DummyOperator(task_id="start")
    
    load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_data_task
    )
    
    handle_missing = PythonOperator(
        task_id="handle_missing_values",
        python_callable=handle_missing_task
    )
    
    # Dos ramas paralelas desde handle_missing
    remove_duplicates = PythonOperator(
        task_id="remove_duplicates",
        python_callable=remove_duplicates_task
    )
    
    filter_outliers = PythonOperator(
        task_id="filter_outliers",
        python_callable=filter_outliers_task
    )
    
    # Se unen en create_features
    create_features = PythonOperator(
        task_id="create_features",
        python_callable=create_features_task
    )
    
    # Tarea final de reporte
    generate_report = PythonOperator(
        task_id="generate_report",
        python_callable=generate_report_task
    )
    
    end = DummyOperator(task_id="end")

    # Definir el flujo con ramas
    start >> load_data >> handle_missing
    
    # Dos caminos paralelos
    handle_missing >> remove_duplicates >> create_features
    handle_missing >> filter_outliers >> create_features
    
    # Final
    create_features >> generate_report >> end