from airflow.sdk import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.python import PythonOperator
from common.commom_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 11, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    regist_t1 = PythonOperator(
        task_id='regist_t1',
        python_callable=regist,
        op_args=['yang','man','kr','seoul']
    )
    
    regist_t1