from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id='05_xcom_fixed',
    start_date=datetime(2025, 7, 7),
    schedule=None,
    catchup=False
)
def xcom_example():
    
    @task
    def extract():
        return {"primeiro_valor": 10, "segundo_valor": 20}
    
    @task
    def transform(valores: dict):
        print(f"Valores: {valores['primeiro_valor']}, {valores['segundo_valor']}")
    
    transform(extract())

dag = xcom_example()