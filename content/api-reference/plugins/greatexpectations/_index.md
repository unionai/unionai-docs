---
title: Great Expectations
layout: plugin
variants: +flyte -byoc -selfmanaged -serverless
metadata:
  title: Great Expectations
  title_expanded: Flytekit Great Expectations Plugin
  name: flytekitplugins-great_expectations
  version: 0.0.0+develop
  author: flyteorg
  author_email: admin@flyte.org
  description: Great Expectations Plugin for Flytekit
  namespace_packages:
  - flytekitplugins
  packages:
  - flytekitplugins.great_expectations
  install_requires:
  - flytekit>=1.5.0
  - great-expectations>=0.13.30,<1.0.0
  - sqlalchemy>=1.4.23
  - pyspark==3.3.2
  - s3fs<2023.6.0
  license: apache2
  python_requires: '>=3.9'
  classifiers:
  - 'Intended Audience :: Science/Research'
  - 'Intended Audience :: Developers'
  - 'License :: OSI Approved :: Apache Software License'
  - 'Programming Language :: Python :: 3.9'
  - 'Programming Language :: Python :: 3.10'
  - 'Topic :: Scientific/Engineering'
  - 'Topic :: Scientific/Engineering :: Artificial Intelligence'
  - 'Topic :: Software Development'
  - 'Topic :: Software Development :: Libraries'
  - 'Topic :: Software Development :: Libraries :: Python Modules'
  folder: flytekit-greatexpectations
---


Great Expectations helps enforce data quality. The plugin supports the usage of Great Expectations as task and type.

To install the plugin, run the following command:

```bash
pip install flytekitplugins-great-expectations
```

## Task Example
```python
import os

import pandas as pd
from flytekit import Resources, kwtypes, task, workflow
from flytekitplugins.great_expectations import BatchRequestConfig, GreatExpectationsTask

simple_task_object = GreatExpectationsTask(
    name="great_expectations_task_simple",
    datasource_name="data",
    inputs=kwtypes(dataset=str),
    expectation_suite_name="test.demo",
    data_connector_name="data_example_data_connector",
    context_root_dir="great_expectations",
)

@task(limits=Resources(mem="500Mi"))
def simple_task(csv_file: str) -> int:
    result = simple_task_object(dataset=csv_file)
    df = pd.read_csv(os.path.join("greatexpectations", "data", csv_file))
    return df.shape[0]

@workflow
def simple_wf(dataset: str = "yellow_tripdata_sample_2019-01.csv") -> int:
    return simple_task(csv_file=dataset)
```

## Type Example
```python
from flytekit import workflow
from flytekitplugins.great_expectations import (
    BatchRequestConfig,
    GreatExpectationsFlyteConfig,
    GreatExpectationsType,
)

def simple_task(
    directory: GreatExpectationsType[
        str,
        GreatExpectationsFlyteConfig(
            datasource_name="data",
            expectation_suite_name="test.demo",
            data_connector_name="my_data_connector",
            batch_request_config=BatchRequestConfig(
                data_connector_query={
                    "batch_filter_parameters": {
                        "year": "2019",
                        "month": "01",
                    },
                    "limit": 10,
                },
            ),
            context_root_dir="great_expectations",
        ),
    ]
) -> str:
    return f"Validation works for {directory}!"


@workflow
def simple_wf(directory: str = "my_assets") -> str:
    return simple_task(directory=directory)
```

[More examples](https://docs.flyte.org/en/latest/flytesnacks/examples/greatexpectations_plugin/index.html) can be found in the documentation.
