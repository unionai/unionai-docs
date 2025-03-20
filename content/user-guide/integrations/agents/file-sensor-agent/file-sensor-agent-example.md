---
title: File sensor agent example
weight: 1
variants: +flyte -serverless +byoc +byok
---

# File sensor agent example

```python
# %% [markdown]
# # File Sensor
#
# This example shows how to use the `FileSensor` to detect files appearing in your local or remote filesystem.
#
# First, import the required libraries.

# %%
import {{< key kit_import >}}
from flytekit.sensor.file_sensor import FileSensor

# %% [markdown]
# Next, create a FileSensor task.

# %%
sensor = FileSensor(name="test_file_sensor")

# %% [markdown]
# To use the FileSensor created in the previous step, you must specify the path parameter. In the sandbox, you can use the S3 path.


# %%
@{{< key kit_as >}}.task()
def t1():
    print("SUCCEEDED")


@{{< key kit_as >}}.workflow()
def wf():
    sensor(path="s3://my-s3-bucket/file.txt") >> t1()
```
