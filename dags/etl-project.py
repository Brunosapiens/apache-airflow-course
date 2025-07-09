from airflow.decorators import dag, task
import json
from datetime import datetime

@dag(
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    doc_md=__doc__,
    default_args={"owner": "Astro", "retries": 3},
    tags=["example"],
)
def etl_dag():
    @task()
    def extract():
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'
        order_data_dict = json.loads(data_string)
        return order_data_dict

    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        total_order_value = 0
        for value in order_data_dict.values():
            total_order_value += value
        return {"total_order_value": total_order_value}

    @task
    def load(total_order_value: float):
        print(f"Total order value is: {total_order_value}")

    # Task dependencies
    order_data = extract()
    order_summary = transform(order_data)
    task_load = load(order_summary['total_order_value'])
    
    order_data >> order_summary >> task_load

etl_dag = etl_dag()