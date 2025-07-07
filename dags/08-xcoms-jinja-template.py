from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    return {"primeiro_valor": 100, "segundo_valor": 400}

def transform(JSON):
    import json
    dados = json.loads(str(JSON))
    print(f"XCOM são {dados}")
    print(f"Tipo de dado é {type(dados)}")

with DAG(
    dag_id='08-xcoms-com-jinja-template',
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
        python_callable=transform,
        op_kwargs={
            "JSON": "{{ ti.xcom_pull(task_ids='extract') }}"
        }
    )
    
    task1 >> task2