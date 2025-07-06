from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def primeira_funcao(valor: int):
    print(f'Minha primeira função Python com {valor}')
    
    def segunda_funcao(par: str, par2: str):
        print(f'Minha segunda função Python com {par} e {par2}')

with DAG(dag_id='03-python-operator-example',
    start_date=datetime(2025, 7, 3),
    schedule=None) as dag:  # só pode ser executado manualmente

    task1 = PythonOperator(
        task_id='primeira_funcao',
        python_callable=primeira_funcao,
        op_args=[10])

    task2 = PythonOperator(
        task_id='segunda_funcao',
        python_callable=segunda_funcao,
        op_kwargs={
            'par': 10,
            'par2': 15
        }
    )