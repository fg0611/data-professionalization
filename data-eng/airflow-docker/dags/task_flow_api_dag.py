from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'fran',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}


@dag(
    dag_id='taskflow_dag_v02',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2022, 12, 5),
    schedule_interval='@daily'
)
def test_etl():

    @task(multiple_outputs=True)
    def get_info():
        return {"name": "Fran", "country": "AR"}

    @task()
    def get_age():
        return 34

    @task()
    def show_data(info: dict, age):
        name = info["name"]
        country = info["country"]
        print(f"{name} {age} {country}")

    info = get_info()
    age = get_age()
    show_data(info, age)


result = test_etl()
