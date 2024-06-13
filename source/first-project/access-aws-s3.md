# Access AWS S3 buckets

Here we will take a look at how to access data on AWS S3 Buckets from Union.
As a prerequisite, we assume that our AWS S3 bucket is accessible with API keys: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

## Creating secrets on Union

First, we create secrets on Union by running the following command:

```{code-block} shell
unionai create secret AWS_ACCESS_KEY_ID
```

This will open a prompt where we paste in our AWS credentials:

```{code-block} shell
Enter secret value: 🗝️
```

Repeat this process for all other AWS credentials, such as `AWS_SECRET_ACCESS_KEY`.

## Using secrets in a task

Next, we can use the secrets directly in a task! With AWS CLI, we create a small text file and move it to a AWS bucket

```{code-block} shell
aws s3 mb s3://test_bucket
echo "Hello Union" > my_file.txt
aws s3 cp my_file.txt s3://test_bucket/my_file.txt
```

Next, we give a task access to our AWS secrets by supplying them through `secret_requests`. For this guide, save the following snippet as `aws-s3-access.py` and run:

```{code-block} python
from flytekit import task, current_context, Secret, workflow

@task(
    secret_requests=[
        Secret(key="AWS_ACCESS_KEY_ID"),
        Secret(key="AWS_SECRET_ACCESS_KEY"),
    ],
)
def read_s3_data() -> str:
    import s3fs
    secrets = current_context().secrets

    s3 = s3fs.S3FileSystem(
        secret=secrets.get("AWS_SECRET_ACCESS_KEY"),
        key=secrets.get("AWS_ACCESS_KEY_ID"),
    )

    with s3.open("test_bucket/my_file.txt") as f:
        content = f.read().decode("utf-8")
    return content

@workflow
def main():
    read_s3_data()
```

Within the task, the secrets are available through `current_context().secrets` and passed to `s3fs`. Running the following command to execute the workflow:

```{code-block} shell
unionai run --remote aws-s3-access.py main
```

## Conclusion

You can easily access your AWS S3 buckets by running union create secret and configuring your tasks to access the secrets!
