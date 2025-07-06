from airflow.providers.standard.operators.empty import EmptyOperator
from airflow import DAG
from airflow.decorators import dag, task
from datetime import datetime

##@dag(start_date=datetime(2025, 1, 1), schedule='@once', catchup=False)
## DAG com Orientado a ObjetO
##dag = DAG(dag_id='01-primeira-dag', start_date=datetime(2025, 7, 2) )
# task1 = EmptyOperator(task_id='extract', dag=dag)
# task2 = EmptyOperator(task_id='transform', dag=dag)
# task3 = EmptyOperator(task_id='load', dag=dag)
# task1 >> task2 >> task3

## usar com with
# with DAG(dag_id='01-primeira-dag', start_date=datetime(2025, 7, 2) ) as dag2:
#     task1 = EmptyOperator(task_id='extract')
#     task2 = EmptyOperator(task_id='transform')
#     task3 = EmptyOperator(task_id='load')
#     task1 >> task2 >> task3

   #Dag com decorator
@dag(dag_id='01-primeira-dag-decorator', start_date=datetime(2025, 7, 3),
         schedule=None,
         catchup=False,
          tags=['etl']) 
def etl():
        task1 = EmptyOperator(task_id='extract')
        task2 = EmptyOperator(task_id='transform')
        task3 = EmptyOperator(task_id='load')
        task1 >> task2 >> task3

dag_instance = etl()