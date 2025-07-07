from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    return {'primeiro_valor': 100, 'segundo_valor': 400}

def transform(ti):
    result = ti.xcom_pull(task_ids='extract')
    primeiro_valor = result['primeiro_valor']
    segundo_valor = result['segundo_valor']
    print(f"XCOM são {primeiro_valor} e {segundo_valor}")

with DAG(
    dag_id='07-xcoms-return-value',
    start_date=datetime(2025, 7, 7),
    schedule_interval=None,
    catchup=False
) as dag:
    
    task1 = PythonOperator(
        task_id='extract',
        python_callable=extract
    )
    
    task2 = PythonOperator(
        task_id='transform',
        python_callable=transform
    )
    
    task1 >> task2