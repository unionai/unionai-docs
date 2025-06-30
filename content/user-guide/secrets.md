---
title: Secrets
weight: 85
variants: +flyte +serverless +byoc +selfmanaged
---

# Secrets

Flyte secrets enable you to securely store and manage sensitive information, such as API keys, passwords, and other credentials.
Secrets reside in a secret store on the data plane of your Flyte/Union backend.
You can create, list, and delete secrets in the store using the Flyte CLI or SDK.
Secrets in the store can be accessed and used within your workflow tasks, without exposing any cleartext values in your code.

<!-- TODO: add back when file secrets are supported
## Creating a literal string secret
-->

## Creating a secret

You can create a secret using the [`flyte create secret`](../api-reference/flyte-cli#flyte-create-secret) command like this:

```shell
flyte create secret MY_SECRET_KEY my_secret_value
```

This will create a secret called `MY_SECRET_KEY` with the value `my_secret_value`.
This secret will be scoped to your entire organization.
It will be available across all projects and domains in your organization.
See the [scoping secrets](#scoping-secrets) section below for more details.

<!-- TODO: add back when file secrets are supported
## Creating a file secret

You can also create a secret with a file as the value

```shell
flyte create secret MY_SECRET_KEY --from-file /path/to/my_secret_file
```

In this case, when accessing the secret in your task code, you will need to [mount it as a file](#using-a-secret-created-from-a-file).
-->

## Scoping secrets

When you create a secret without specifying a project or domain, as we did above, the secret is scoped to the organization level.
This means that the secret will be available across all projects and domains in the organization.

You can optionally specify either or both of the `--project` and `--domain` flags to restrict the scope of the secret to:
* A specific project (across all domains)
* A specific domain (across all project)
* A specific project and a specific domain.

For example, to create a secret that it is only available in `my_project/development`, you would execute the following command:

```shell
flyte create secret  --project my_project --domain development MY_SECRET_KEY my_secret_value
```

## Listing secrets

You can list existing secrets with the [`flyte get secret`](../api-reference/flyte-cli#flyte-get-secret) command.
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

To delete a secret, use the [`flyte delete secret`](../api-reference/flyte-cli#flyte-delete-secret) command:

```shell
flyte delete secret MY_SECRET_KEY
```

<!-- TODO: add back when file secrets are supported
## Using a literal string secret
-->

## Using a secret

To use a secret, specify it in the `TaskEnvironment` along with the name of the environment variable into which it will be injected.
You can then access it using `os.getenv()` in your task code.
For example:

```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    secrets=[
        flyte.Secret(key="MY_SECRET_KEY", as_env_var="MY_SECRET_ENV_VAR"),
    ]
)


@env.task
def t1():
    my_secret = os.getenv("MY_SECRET_ENV_VAR")
    # Do something with the secret
    ...
```

<!-- TODO: add back when file secrets are supported

## Using a file secret

To use a file secret, specify it in the `TaskEnvironment` along with the path to which the file will be mounted.
You can then access it as a local file within your task code.

```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    secrets=[
        flyte.Secret(key="MY_SECRET_KEY", mount="/root/my_secret_file"),
    ]
)


@env.task
def t1():
    with open("/root/my_secret_file", "r") as f:
        secret_value = f.read()
    # Do something with the secret
    ...
```
-->

> [!NOTE]
> A `TaskEnvironment` can only access a secret if the scope of the secret includes the project and domain where the `TaskEnvironment` is deployed.

> [!WARNING]
> Do not return secret values from tasks, as this will expose secrets to the control plane.
