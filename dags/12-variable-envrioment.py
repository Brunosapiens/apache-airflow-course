from airflow import DAG
from airflow.models import Variable
from airflow.hooks.base import BaseHook
from airflow.operators.python import PythonOperator
import datetime

def get_env():
    env_var_test = Variable.get("NOME_DA_VARIAVEL")
    env_json = Variable.get("JSON")
    print(f"ENV: {env_var_test}")
    print(f"ENV: {env_json}")

def get_conn():
    airflow_conn = BaseHook.get_connection("MY_PROD_DATABASE")
    airflow_conn_pass = airflow_conn.password
    print(f"type(CONN): {type(airflow_conn)}")
    print(f"CONN: {airflow_conn}")
    print(f"password: {airflow_conn_pass}")

with DAG(
    dag_id="12-variavel-enviroment",
    start_date=datetime.datetime(2025, 7, 8),
    schedule=None
):
    test_task = PythonOperator(
        task_id='test_task',
        python_callable=get_env
    )
    test_task2 = PythonOperator(
        task_id='test_task2',
        python_callable=get_conn
    )