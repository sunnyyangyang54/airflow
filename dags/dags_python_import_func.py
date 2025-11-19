from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
import pendulum
import datetime
from common.commom_func import get_sftp

with DAG(
    dag_id="dags_python_import_func",
    schedule="0 0 * * 5",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    task_get_sftp = PythonOperator(
        task_id = 'task_get_sftp',
        python_callable=get_sftp,
    )
