from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'test',
    'retries': 1,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='pg_dag',
    default_args=default_args,
    description='postgres dag',
    start_date=datetime(2022, 12, 5, 2),
    schedule_interval='@daily'
) as dag:
    create_data_table = PostgresOperator(
        task_id="create_data_table",
        sql="""
            CREATE TABLE IF NOT EXISTS data (
            data_id SERIAL PRIMARY KEY,
            item VARCHAR NOT NULL,
            type VARCHAR NOT NULL,
            count INT NOT NULL);
          """,

    )

    populate_data_table = PostgresOperator(
        task_id="populate_data_table",
        sql="""
            INSERT INTO data (item, type, count)
            VALUES ( 'Teddy Bear', 'Toy', 1);
            INSERT INTO pet (item, type, count)
            VALUES ( 'Ford Mustang', 'Vehicle', 10);
            INSERT INTO pet (item, type, count)
            VALUES ( 'Truck', 'Vehicle', 4);
            INSERT INTO pet (item, type, count)
            VALUES ( 'Explorer', 'Vehicle Submarine', 1);
            """,
    )

    get_all = PostgresOperator(task_id="get_all", sql="SELECT * FROM data;")


    create_data_table >> populate_data_table >> get_all
