from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extract step")

def transform():
    print("Transform step")

def load():
    print("Load step")

with DAG(
    dag_id="toy_etl_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callable=transform,
    )

    t3 = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    t1 >> t2 >> t3
