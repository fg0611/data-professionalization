from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def salute(ti):
    name = ti.xcom_pull(task_ids='get_name', key='name')
    lastname = ti.xcom_pull(task_ids='get_name', key='lastname')
    country = ti.xcom_pull(task_ids='get_country', key='country')
    print(f"Hello {name} {lastname}, from {country}!")

def get_name(ti):
    ti.xcom_push(key='name', value="francisco")
    ti.xcom_push(key='lastname', value="garrido")

def get_country(ti):
    ti.xcom_push(key='country', value="argentina")

default_args = {
    'owner': 'fran',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='pyop_xcoms',
    default_args=default_args,
    description='dag with py ops & xcoms',
    start_date=datetime(2022, 12, 5, 3),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='salute',
        python_callable=salute,
        op_kwargs={"country": "argentina"}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
        op_kwargs={"name": "fran"}
    )
    
    task3 = PythonOperator(
        task_id='get_country',
        python_callable=get_country,
        op_kwargs={"country": "argentina"}
    )
    
    [task2, task3] >> task1