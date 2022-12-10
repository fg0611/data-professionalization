from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'test',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='test_dag_v1',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2022, 12, 5, 3),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo TASK 1 DONE!"
    )
    task2 = BashOperator(
        task_id='task2',
        bash_command="echo TASK 2 DONE!"
    )
    task3 = BashOperator(
        task_id='task3',
        bash_command="echo TASK 3 DONE!"
    )

    task1 >> task2
    task1 >> task3