from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id='03_python_operator_fixed',
    start_date=datetime(2025, 7, 7),
    schedule=None
)
def python_operator_example():
    
    @task
    def primeira_funcao():
        print("Executando a primeira tarefa!")
    
    primeira_funcao()

dag = python_operator_example()