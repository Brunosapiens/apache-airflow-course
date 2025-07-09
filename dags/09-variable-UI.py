from airflow.models import Variable
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

def minha_funcao():
    # Obter variáveis dentro da função (melhor prática)
    MINHA_VARIAVEL = Variable.get('minha_variavel')
    PASSWORD_DB = Variable.get('DB_PASSWORD_TEST')
    
    print(f'Definindo minha primeira variável como {MINHA_VARIAVEL}')
    print(f'DB_PASSWORD_TEST = {PASSWORD_DB}')

with DAG(dag_id='09-variable-IU',
    start_date=datetime(2025, 7, 8),  # Data atualizada para 8 de julho de 2025
    schedule=None):
    task1 = PythonOperator(task_id='task-01', python_callable=minha_funcao)
    task2 = PythonOperator(task_id='task-02', python_callable=minha_funcao)
    task3 = PythonOperator(task_id='task-03', python_callable=minha_funcao)