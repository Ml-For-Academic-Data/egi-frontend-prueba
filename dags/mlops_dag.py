from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

sys.path.append(os.path.abspath("/opt/airflow/src"))

from etl import run_etl
from ml import train_model

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="mlops_dropout_prediction",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    ml_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model
    )

    etl_task >> ml_task