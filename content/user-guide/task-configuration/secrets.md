---
title: Secrets
weight: 170
variants: +flyte +serverless +byoc +selfmanaged
---

# Secrets

Flyte secrets enable you to securely store and manage sensitive information, such as API keys, passwords, and other credentials.
Secrets reside in a secret store on the data plane of your Union/Flyte backend.
You can create, list, and delete secrets in the store using the Flyte CLI or SDK.
Secrets in the store can be accessed and used within your workflow tasks, without exposing any cleartext values in your code.

Flyte supports two types of secrets:
- **String secrets**: Simple text values that are injected as environment variables
- **File secrets**: Binary or text files that are mounted as files in the task container

## Creating a string secret

You can create a secret using the [`flyte create secret`](../../api-reference/flyte-cli#flyte-create-secret) command like this:

```shell
flyte create secret MY_SECRET_KEY my_secret_value
```

This will create a secret called `MY_SECRET_KEY` with the value `my_secret_value`.
This secret will be scoped to your entire organization.
It will be available across all projects and domains in your organization.
See the [scoping secrets](#scoping-secrets) section below for more details.

## Creating a file secret

You can also create a secret with a file as the value:

```shell
flyte create secret MY_SECRET_KEY --from-file /path/to/my_secret_file
```

In this case, when accessing the secret in your task code, you will need to [mount it as a file](#using-a-file-secret).

### Secret types

You can specify the type of secret when creating it using the `--type` flag. The available types are:

- `regular` (default): Standard secrets for API keys, passwords, etc.
- `image_pull`: Secrets specifically for authenticating with container registries

```shell
# Create a regular secret (default)
flyte create secret MY_API_KEY --value my_api_value

# Create an image pull secret for container registry authentication
flyte create secret MY_REGISTRY_SECRET --type image_pull --from-file /path/to/docker/config.json
```

## Scoping secrets

When you create a secret without specifying a project or domain, the secret is scoped to the organization level.
This means that the secret will be available across all projects and domains in the organization.

You can optionally specify either or both of the `--project` and `--domain` flags to restrict the scope of the secret to:
* A specific project (across all domains)
* A specific domain (across all projects)
* A specific project and a specific domain.

For example, to create a string secret that is only available in `my_project/development`, you would execute:

```shell
flyte create secret --project my_project --domain development MY_SECRET_KEY my_secret_value
```

The same scoping applies to file secrets:

```shell
flyte create secret --project my_project --domain development MY_FILE_SECRET --from-file /path/to/secret_file
```

## Listing secrets

You can list existing secrets with the [`flyte get secret`](../../api-reference/flyte-cli#flyte-get-secret) command.
For example, the following command will list all secrets in the organization:

```shell
$ flyte get secret
```

Specifying either or both of the `--project` and `--domain` flags will list the secrets that are **only** available in that project and/or domain.

For example, to list the secrets that are only available in `my_project` and domain `development`, you would run:

```shell
flyte get secret --project my_project --domain development
```

## Deleting secrets

To delete a secret, use the [`flyte delete secret`](../../api-reference/flyte-cli#flyte-delete-secret) command:

```shell
flyte delete secret MY_SECRET_KEY
```

## Using a string secret

To use a string secret, specify it in the `TaskEnvironment` along with the name of the environment variable into which it will be injected.
You can then access it using `os.getenv()` in your task code.

### Using explicit environment variable names

```python
import os

env = flyte.TaskEnvironment(
    name="my_task_env",
    secrets=[
        flyte.Secret(key="MY_SECRET_KEY", as_env_var="MY_SECRET_ENV_VAR"),
    ]
)


@env.task
def t1():
    my_secret_value = os.getenv("MY_SECRET_ENV_VAR")
    # Do something with the secret
    ...
```

### Using automatic environment variable names

If you don't specify an environment variable name, Flyte will automatically create one by converting the secret key to uppercase and replacing hyphens with underscores:

```python
import os

env = flyte.TaskEnvironment(
    name="my_task_env",
    secrets=[
        flyte.Secret(key="my-secret-key"),  # Will be available as MY_SECRET_KEY
    ]
)


@env.task
def t1():
    my_secret_value = os.getenv("MY_SECRET_KEY")
    # Do something with the secret
    ...
```

## Using a file secret

To use a file secret, specify it in the `TaskEnvironment` along with the path to which the file will be mounted.
You can then access it as a local file within your task code.

```python
import pathlib

env = flyte.TaskEnvironment(
    name="my_task_env",
    secrets=[
        flyte.Secret(key="MY_SECRET_KEY", mount=pathlib.Path("/tmp/my_secret_file")),
    ]
)


@env.task
def t1():
    with open("/tmp/my_secret_file", "r") as f:
        my_secret_value = f.read()
    # Do something with the secret
    ...
```

> [!NOTE]
> File secrets are mounted read-only in the task container. Choose mount paths that your task has permission to read, such as `/tmp/` or your application's working directory.

> [!NOTE]
> A `TaskEnvironment` can only access a secret if the scope of the secret includes the project and domain where the `TaskEnvironment` is deployed.

> [!WARNING]
> Do not return secret values from tasks, as this will expose secrets to the control plane.
