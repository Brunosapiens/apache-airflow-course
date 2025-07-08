from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id='06_kwargs_fixed',
    start_date=datetime(2025, 7, 7),
    schedule=None
)
def xcom_kwargs_example():
    
    @task
    def extract(**context):
        context["ti"].xcom_push(key="dados", value={"val1": 100, "val2": 200})
    
    @task
    def transform(**context):
        dados = context["ti"].xcom_pull(task_ids="extract", key="dados")
        print(f"Dados: {dados['val1']}, {dados['val2']}")
    
    transform() << extract()

dag = xcom_kwargs_example()