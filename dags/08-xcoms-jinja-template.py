from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    return {"primeiro_valor": 100, "segundo_valor": 400}

def transform(JSON, **kwargs):
    print(f"XCOM recebido via Jinja template: {JSON}")
    print(f"Tipo do dado: {type(JSON)}")

with DAG(
    dag_id='08-xcoms-com-jinja-template',
    start_date=datetime(2025, 7, 7),
    schedule_interval=None,
    catchup=False
) as dag:
    
    task1 = PythonOperator(
        task_id='extract_task',
        python_callable=extract
    )
    
    task2 = PythonOperator(
        task_id='transform_task',
        python_callable=transform,
        op_kwargs={
            "JSON": "{{ ti.xcom_pull(task_ids='extract_task') }}"
        }
    )
    
    task1 >> task2
