from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'test',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='cron_dag_v6',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2022, 12, 7, 0, 11),
    schedule_interval="*/1 * * * *"
) as dag:
    t1 = BashOperator(
        task_id='t1',
        bash_command="echo cron Task DONE!"
    )
    
    t1