from airflow.sdk import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_shell_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 11, 18, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="/opt/airflow/plugins/shell/test.sh",
    )    
    
    bash_t1