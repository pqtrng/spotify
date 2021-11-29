from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import datetime
import os, sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

# Local
from app.etl import etl

args = {
    "owner": "pqtrng",
    "depends_on_past": False,
    "start_date": datetime.datetime(2021, 11, 28, 0, 0),
    "retries": 1,
    "retry_delay": datetime.timedelta(minutes=30),
}

dag = DAG(
    dag_id="spotify_dag",
    default_args=args,
    description="DAG with Spotify ETL!",
    schedule_interval=datetime.timedelta(days=1),
)

run_etl = PythonOperator(task_id="spotify_etl", python_callable=etl, dag=dag)

run_etl
