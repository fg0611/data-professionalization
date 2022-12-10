from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'test',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='catchup_backfill_v02',
    default_args=default_args,
    description='dag with catchup and backfill',
    start_date=datetime(2022, 11, 4),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task_1 = BashOperator(
        task_id='first_task',
        bash_command="echo TASK 1 DONE!"
    )

    task_1
