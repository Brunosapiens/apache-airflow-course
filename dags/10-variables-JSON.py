from airflow.models import Variable
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import json

# Obter variável JSON (com tratamento de erro)
try:
    MEU_JSON = Variable.get('meu_json', deserialize_json=True)
except KeyError:
    raise ValueError("Variável 'meu_json' não encontrada no Airflow")

def minha_funcao():
    print(f'Definindo minha primeira variável como {MEU_JSON}')
    # Se quiser acessar campos específicos do JSON:
    # print(f"Campo específico: {MEU_JSON.get('chave')}")

with DAG(dag_id='10-variable-json',
    start_date=datetime(2025, 7, 8),  # Atualizado para a data atual
    schedule=None,
    catchup=False):
    
    task1 = PythonOperator(task_id='task-01', python_callable=minha_funcao)
    task2 = PythonOperator(task_id='task-02', python_callable=minha_funcao)
    task3 = PythonOperator(task_id='task-03', python_callable=minha_funcao)