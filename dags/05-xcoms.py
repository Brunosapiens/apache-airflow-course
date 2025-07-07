from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract(ti):
    ti.xcom_push(key="primeiro_valor", value=10)
    ti.xcom_push(key="segundo_valor", value=20)

def transform(ti):
    primeiro_valor = ti.xcom_pull(key="primeiro_valor", task_ids='extract')
    segundo_valor = ti.xcom_pull(key="segundo_valor", task_ids='extract')
    print(f"Valores XCOM: {primeiro_valor} e {segundo_valor}")

with DAG(
    dag_id='xcom_atualizado',
    start_date=datetime(2025, 7, 7),
    schedule_interval=None,
    catchup=False,
    tags=['exemplo_xcom']
) as dag:

    task_extract = PythonOperator(
        task_id='extract_task',
        python_callable=extract
    )

    task_transform = PythonOperator(
        task_id='transform_task',
        python_callable=transform
    )

    task_extract >> task_transform