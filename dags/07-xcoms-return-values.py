from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id='07_return_values_fixed',
    start_date=datetime(2025, 7, 7),
    schedule=None,  # Mudança crucial: schedule_interval → schedule
    catchup=False
)
def return_example():
    
    @task
    def extract():
        return {'primeiro_valor': 100, 'segundo_valor': 400}
    
    @task
    def transform(resultado: dict):
        print(f"Valores: {resultado['primeiro_valor']}, {resultado['segundo_valor']}")
        return resultado
    
    transform(extract())

dag = return_example()

