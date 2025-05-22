from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator

def build_cleaning_group(dag):

    with TaskGroup("cleaning_pipeline", tooltip="Pipeline de limpieza de datos") as group:

        task_1 = PythonOperator(
            task_id="handle_missing_values",
            python_callable=handle_missing_values,
            provide_context=True,
            dag=dag
        )

        task_2 = PythonOperator(
            task_id="remove_duplicate_rows",
            python_callable=remove_duplicate_rows,
            provide_context=True,
            dag=dag
        )

        task_3 = PythonOperator(
            task_id="filter_numeric_outliers",
            python_callable=filter_numeric_outliers,
            provide_context=True,
            dag=dag
        )

        task_4 = PythonOperator(
            task_id="create_derived_features",
            python_callable=create_derived_features,
            provide_context=True,
            dag=dag
        )

        task_1 >> task_2 >> task_3 >> task_4

    return group