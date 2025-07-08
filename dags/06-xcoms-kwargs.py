from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract(**context):
    ti = context['ti']
    ti.xcom_push(key="primeiro_valor", value='10')
    ti.xcom_push(key="segundo_valor", value='20')

def transform(**context):
    ti = context['ti']
    primeiro_valor = ti.xcom_pull(key='primeiro_valor', task_ids='extract_task')
    segundo_valor = ti.xcom_pull(key='segundo_valor', task_ids='extract_task')
    print(f"XCOM são {primeiro_valor} e {segundo_valor}")

with DAG(
    dag_id='06-xcoms-context',
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
        python_callable=transform
    )
    
    task1 >> task2
