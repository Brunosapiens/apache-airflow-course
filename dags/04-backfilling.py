from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

# Formas de definir agendamento em DAGs
# 1. usando os presets (@daily, @monthly)
with DAG(dag_id='04-backfilling',
    start_date=datetime(2025, 7, 7),  # Data atualizada para hoje
    schedule="@daily",
    catchup=True  # Executa todas as execuções desde a start_date até hoje
    ) as dag:

    task1 = EmptyOperator(task_id='extract')
    task2 = EmptyOperator(task_id='transform')
    task3 = EmptyOperator(task_id='load')

    task1 >>[ task2, task3]
