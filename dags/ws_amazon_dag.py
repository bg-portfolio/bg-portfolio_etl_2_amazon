from datetime import timedelta, datetime
import sys
sys.path.append('/opt/airflow/dags/programs/ws_amazon')
from ws_amazon import amazon_scrapper
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 8, 5),
    'schedule_interval': '@daily',
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    'Amazon_ETL',
    catchup=False,
    default_args=default_args,
    description='Amazon web scrapper DAG',
    schedule_interval=timedelta(days=1),
    tags=["amazon"]) as dag:

    run_etl = PythonOperator(
        task_id='extract_transform_load',
        python_callable=amazon_scrapper,
        dag=dag,
    )

    run_etl