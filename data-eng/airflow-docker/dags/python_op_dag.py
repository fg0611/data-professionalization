from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def salute(country, ti):
    name = ti.xcom_pull(task_ids='task_py_op_2')
    print(f"Hello {name}, from {country}!")

def fetch_name(name):
    return "fran"

default_args = {
    'owner': 'fran',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='py_op_dag_v02',
    default_args=default_args,
    description='test dag with python operator',
    start_date=datetime(2022, 12, 5, 3),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='task_py_op_1',
        python_callable=salute,
        op_kwargs={"country": "argentina"}
    )
    
    task2 = PythonOperator(
        task_id='task_py_op_2',
        python_callable=fetch_name,
        op_kwargs={"name": "fran", "country": "argentina"}
    )
    
    task2 >> task1