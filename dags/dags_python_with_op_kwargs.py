fromfrom airflow.sdk import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.python import PythonOperator
from common.commom_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2025, 11, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    regist_t2 = PythonOperator(
        task_id = regist_t2
        python_callable=regist_t2
        op_kwargs=['kim','man','kim@gmail.com','111.1111.1111']
    )

    regist_t2