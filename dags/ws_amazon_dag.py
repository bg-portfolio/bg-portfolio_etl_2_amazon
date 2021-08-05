from datetime import timedelta
import sys
sys.path.append('/opt/airflow/dags/programs/ws_amazon')
from ws_amazon/ws_amazon import amazon_scrapper
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 7, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'spotify_dag',
    default_args=default_args,
    description='Amazon web scrapper DAG',
    schedule_interval=timedelta(days=1),
)

def just_a_function():
    print("I'm going to show you something :)")

run_etl = PythonOperator(
    task_id='amazon_scrapper',
    python_callable=amazon_scrapper,
    dag=dag,
)

run_etl