from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'test',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='first_dag',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2022, 12, 5, 2),
    schedule_interval='@daily'
) as dag:
    task_1 = BashOperator(
        task_id='first_task',
        bash_command="echo TASK 1 DONE!"
    )
    
    task_1