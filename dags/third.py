import requests
import time
import json
from datetime import timedelta,datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator

import pandas as pd
import numpy as np
import os

"""exercise: write a DAG which is able to request market data for a list of stocks.
this list should be an input of your function. The functions names are left to help you
you DAG should only have one task
"""

def get_data(**kwargs):
	api_key = 'H9BZCXCEOBDGG625'
	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=' + api_key
	r = requests.get(url)

	try:
		data=r.json()
		print("doneeee")
		return data["Meta Data"]


	except:
		pass



default_dag_args = {
	'start_date' : datetime(2023,2,20),
	'email_on_failure' : False,
	'email_on_retry' : False,
	'retries' : 1,
	'retry_delay' : timedelta(minutes = 5),
	'project_id' : 1
}

with DAG('third_dag_market_data', schedule_interval = '@daily' , catchup = False, default_args= default_dag_args ) as dag_python:
	task_0 = PythonOperator(task_id = 'third_dag', python_callable = get_data, op_kwargs = {'tickers' : []})