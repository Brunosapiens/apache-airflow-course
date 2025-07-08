from airflow.decorators import dag, task
from datetime import datetime
import json

@dag(
    dag_id='08_xcom_jinja_fixed_v2',
    start_date=datetime(2025, 7, 7),
    schedule=None,
    catchup=False,
    tags=['xcom']
)
def xcom_pipeline():
    
    @task
    def extract():
        return {'primeiro_valor': 100, 'segundo_valor': 400}
    
    @task
    def transform(json_str: str):
        data = json.loads(json_str)
        print(f"Valores transformados: {data['primeiro_valor']}, {data['segundo_valor']}")
        return data
    
    transform("{{ ti.xcom_pull(task_ids='extract') | tojson }}") << extract()

dag = xcom_pipeline()