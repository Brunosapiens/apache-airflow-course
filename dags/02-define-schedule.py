from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator

# Formas de definir agendamento em DAGs
# 1. usando os presets (@daily, @monthly)
with DAG(dag_id='02-define-a-sheduler-with-presets',
    start_date=datetime(2025, 7, 3),
    schedule="@daily",
    end_date=datetime(2030, 7, 3)) as dag1:
    
    task1 = EmptyOperator(task_id='extract')
    task2 = EmptyOperator(task_id='transform')
    task3 = EmptyOperator(task_id='load')

    task1 >> task2 >> task3

# 2. usando expressões CRONTAB https://crontab.guru/
with DAG(dag_id='02-define-a-sheduler-with-crontab-expression',
    start_date=datetime(2025, 7, 3),
    end_date=datetime(2030, 9, 6),
    schedule="0 0 * * *") as dag2:
    
    task1 = EmptyOperator(task_id='extract')
    task2 = EmptyOperator(task_id='transform')
    task3 = EmptyOperator(task_id='load')

    task1 >> task2 >> task3