# Introduction
- an opensource tool to *schedule* *monitor* workflows. 
- it provides the functionality such as  
  - data processing 
  - sequence management 
  - web ui to configure and manage the data workflow 
- the workflows should be schduled through `DAGS` 

# Key Terms and Concepts 

## Task 
- most basic unit of execution 
- task can be invoke of powershell script or python function. 

### Task Depedencies 
- can specify the order of execution of the taskA 

eg: TaskA should execute first then TaskB

> bitshift operator
- `TaskA > TaskB` 
  
> Setdownstream 
- `TaskA.set_downstream(taskB)`

> setUpstream 
- `TaskB.set_upstream(taskA)`

### Task Instances 
- different stages in the task lifecycle 
- instaces docs : [Task Instaces Docs](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html#task-instances)

## DAG 
- Directed Acyclic Graph is a collection of the tasks together. 
- organized based on their dependencies 
- mentions how each of those should be executed. 

# DAG Interval 
- time range in which the dag operates or data is collected 
- for dag specified as `@daily` it will begin today midnight wait till tomorrow midnight to `execute` 
- the time begin this interval can be set by the value `start_date` 

# Creating a DAG

## Simple Dag 

 - simplest of DAGs which will *print HelloWorld* to the screen. 
```py
# follwoing imports are essential in all DAGs
from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'dinith'
}

with DAG( 
    dag_id='simple-hello-world',
    description='Simple Hello World DAG',
    default_args=default_args, # default arguments to be passed to the DAG
    start_date= days_ago(1),  # date which begins the dag interval
    schedule_interval='@daily', # interval at which the DAG should run
    tags=['djtest']
) as dag:

    # Bash Operator is used to run a bash script or code snippet 
    task = BashOperator(task_id='hello_world', bash_command='echo "Hello World 2nd time"', dag=dag)

task
```

## Multiple Depedency DAGs 

  