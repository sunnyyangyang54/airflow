from airflow.sdk import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator2",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 11, 18, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo aa",
    )    

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo bb",
    )    
    
    bash_t1 >> bash_t2