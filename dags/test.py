import time
import json
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.python import BranchPythonOperator

import pandas as pd
import numpy as np
import os


def get_data():
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    api_key = 'H9BZCXCEOBDGG625'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=' + api_key
    r = requests.get(url)
    try:
        data = r.json()

        with open("IBM_" + str(time.time())+".txt", "w") as outfile:
            json.dump(data, outfile)
            print("done!")
    except:
        pass

def newPrint():
    print("TEST!")


default_dag_args = {
    'start_date': datetime(2023, 2, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1

}

with DAG("market_data_alphavantage_dag", schedule_interval='@daily', catchup=False, default_args=default_dag_args) as dag_python:
    task_0 = PythonOperator(task_id='first_python_dag', python_callable=get_data)

