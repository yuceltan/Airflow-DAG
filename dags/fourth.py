import os
import json
import time
import requests
import numpy as np
import pandas as pd
from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import timedelta, datetime
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.postgres import PostgresOperator

default_args = { 'owner': 'airflow',
'retries': 1, 'retry_delay': timedelta(minutes=5), }

#CREATE NEW TABLE IN POSTGRES
create_query = """ CREATE TABLE employee (
id int PRIMARY KEY AUTO INCREMENT,
name varchar(50) UNIQUE NOT NULL,
age int UNIQUE NOT NULL

)"""


insert_data_query = """ INSERT INTO employee (id,name,age)
                        VALUES(0,"YUCELTAN",22),
                        (1,"JAKUB",29),
                        (2,"Anastasiaa",20)"""

calculating_averag_age = """ SELECT AVG(age) FROM employee"""

dag_postgres = DAG(dag_id = "postgres_dag_connection", default_args = default_args, schedule_interval = None, start_date = days_ago(1))

create_table = PostgresOperator(task_id = "creation_of_table", sql = create_query, dag = dag_postgres, postgres_conn_id = "postgres_pedro_local")

insert_data = PostgresOperator(task_id = "insertion_of_data", sql = insert_data_query, dag = dag_postgres, postgres_conn_id = "postgres_pedro_local")

group_data = PostgresOperator(task_id = "calculating_averag_age", sql = calculating_averag_age, dag = dag_postgres, postgres_conn_id = "postgres_pedro_local")

create_table >> insert_data >> group_data