from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

def extract_data():
    # extract data from source
    pass

def transform_data():
    # transform extracted data
    pass

def load_data():
    # load transformed data into Postgres
    pass

dag = DAG(
    "etl_pipeline",
    schedule_interval="0 0 * * *",
    start_date=datetime(2022, 1, 1),
    end_date=datetime(2022, 12, 31),
)

extract_task = PythonOperator(
    task_id="extract_task",
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id="transform_task",
    python_callable=transform_data,
    dag=dag,
)

load_task = PostgresOperator(
    task_id="load_task",
    sql="INSERT INTO table VALUES (1, 2, 3)",
    dag=dag,
)

extract_task >> transform_task >> load_task
