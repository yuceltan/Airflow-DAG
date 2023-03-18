from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_dag_args = {
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
}

# let's define our DAG

with DAG("First_DAG", schedule_interval=None, default_args=default_dag_args) as dag:
    task_0 = BashOperator(task_id='bash_task', bash_command="echo \"COMMAND IS EXECUTED\"")
    task_1 = BashOperator(task_id='bash_task_move',bash_command=r"cp \Users\yucel\Data_Center\DATA_LAKE\dataset_raw.txt /Users/yucel/Data_Center/CLEAN_DATA")
    task_2 = BashOperator(task_id='bash_task_move_delete', bash_command=r"rm \Users\yucel\Data_Center\DATA_LAKE\dataset_raw.txt")
    task_0 >> task_1>>task_2
