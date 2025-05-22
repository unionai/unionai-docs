---
title: Apache Airflow
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Apache Airflow
  title_expanded: Flytekit Airflow Plugin
  name: flytekitplugins-airflow
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: This package holds the Airflow plugins for flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.airflow
  install_requires:
  - apache-airflow
  - apache-airflow-providers-google<12.0.0
  - flytekit>1.10.7
  - flyteidl>1.10.7
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Programming Language :: Python :: 3.11'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  entry_points:
    flytekit.plugins:
    - airflow=flytekitplugins.airflow
  folder: flytekit-airflow
---

Airflow plugin allows you to seamlessly run Airflow tasks in the Flyte workflow without changing any code.

- Compile Airflow tasks to Flyte tasks
- Use Airflow sensors/operators in Flyte workflows
- Add support running Airflow tasks locally without running a cluster

## Example
```python
from airflow.sensors.filesystem import FileSensor
from flytekit import task, workflow

@task()
def t1():
    print("flyte")


@workflow
def wf():
    sensor = FileSensor(task_id="id", filepath="/tmp/1234")
    sensor >> t1()


if __name__ == '__main__':
    wf()
```


To install the plugin, run the following command:

```bash
pip install flytekitplugins-airflow
```
