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

## Multiple Dependency DAGs  
- DAGs having a multiple dependency on each other 
- Note : **dependency cannot be circular**

```py
default_args = {
    'owner': 'dinith'
}

with DAG( 
    dag_id='multiple-depdency',
    description='Multi Depedency DAG',
    default_args=default_args,
    start_date= days_ago(1),
    schedule_interval='@once',
    tags=['djtest']
) as dag:

    taskA = BashOperator(task_id='taskA', bash_command='echo "Executed Task A"')
    taskB = BashOperator(task_id='taskB', bash_command='echo "Executed Task B"')
    taskC = BashOperator(task_id='taskC', bash_command='echo "Executed Task C"')
    taskD = BashOperator(task_id='taskD', bash_command='echo "Executed Task D"')

# the execution order is defined as below 
taskA >> [taskB,taskC] >> taskD
```

## Python Operator Based DAGs

- this dag calls a **Python function** as Task 
- arguments can be passed to the function by `op_kwargs`
- `PythonOperator` is imported from the airflow operators.

```py
from airflow.operators.python import PythonOperator # python operator in imported 

default_args = {
    'owner': 'dinith'
}

# this function is called when task executed 
def hello_world():
    print("Hello World from the python function")

# this function is called with arguments when task2 is executed
def hello_world2(name, city):
    print(f"Hello {name} from  {city} the python function ")

with DAG( 
    dag_id='helloworld-python',
    description='Hellow-wrold-python-DAG',
    default_args=default_args,
    start_date= days_ago(1),
    schedule_interval='@daily',
    tags=['djtest']
) as dag:

    task = PythonOperator(task_id='hello_world', python_callable=hello_world, dag=dag)
    
    task2 = PythonOperator( 
                task_id='hello_world2',
                  python_callable=hello_world2, # name of the python function
                  # arguments can be passed to the python function using op_kwargs
                  op_kwargs={'name':'Dinith', 'city':'Colombo'}, 
                  dag=dag)

task >> task2
```
  