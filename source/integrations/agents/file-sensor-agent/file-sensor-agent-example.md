# File sensor agent example

This example shows how to use the `FileSensor` to detect files appearing in your local or remote filesystem.

First, import the required libraries.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/sensor/sensor/file_sensor_example.py
:language: python
:lines: 9-10
```

Next, create a FileSensor task.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/sensor/sensor/file_sensor_example.py
:language: python
:lines: 16
```

To use the FileSensor created in the previous step, you must specify the `path` parameter. In the sandbox, you can use the S3 path.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/7a300ac43f3da41a4e01bd4dae9d45e8c0094ce3/examples/sensor/sensor/file_sensor_example.py
:language: python
:lines: 23-34
```

You can also use the S3 or GCS file system. We have already set the minio credentials in the agent by default. If you test the sandbox example locally, you will need to set the AWS credentials in your environment variables.

```{prompt} bash
export FLYTE_AWS_ENDPOINT="http://localhost:30002"
export FLYTE_AWS_ACCESS_KEY_ID="minio"
export FLYTE_AWS_SECRET_ACCESS_KEY="miniostorage"
```
