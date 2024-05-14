# Apache Airflow agent example

```{code-block} python
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from flytekit import task, workflow


@task()
def t1():
    print("success")

# Use the Airflow FileSensor to wait for a file to appear before running the task.
@workflow
def file_sensor():
    sensor = FileSensor(task_id="id", filepath="/tmp/1234")
    sensor >> t1()

# Use the Airflow BashOperator to run a bash command.
@workflow
def bash_sensor():
    op = BashOperator(task_id="airflow_bash_operator", bash_command="echo hello")
    op >> t1()
```