---
title: Secrets
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Secrets

Flyte secrets enable you to securely store and manage sensitive information, such as API keys, passwords, and other credentials.
Secrets reside in a secret store on the data plane of your Union/Flyte backend.
You can create, list, and delete secrets in the store using the Flyte CLI or SDK.
Secrets in the store can be accessed and used within your workflow tasks, without exposing any cleartext values in your code.

## Creating a literal string secret

You can create a secret using the [`flyte create secret`](../../api-reference/flyte-cli#flyte-create-secret) command like this:

```shell
flyte create secret MY_SECRET_KEY --value my_secret_value
```

This will create a secret called `MY_SECRET_KEY` with the value `my_secret_value`.
This secret will be scoped to your entire organization.
It will be available across all projects and domains in your organization.
See the [scoping secrets](#scoping-secrets) section below for more details.
See [Using a literal string secret](#using-a-literal-string-secret) for how to access the secret in your task code.


## Creating a file secret

You can also create a secret by specifying a local file:

```shell
flyte create secret MY_SECRET_KEY --from-file /local/path/to/my_secret_file
```

In this case, when accessing the secret in your task code, you will need to [mount it as a file](#using-a-file-secret).

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

## Using a literal string secret

To use a literal string secret, specify it in the `TaskEnvironment` along with the name of the environment variable into which it will be injected.
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
    my_secret_value = os.getenv("MY_SECRET_ENV_VAR")
    # Do something with the secret
    ...
```

## Using a file secret

To use a file secret, specify it in the `TaskEnvironment` along with the `mount="/etc/flyte/secrets"` argument (with that precise value).

The file will be mounted at `/etc/flyte/secrets/<SECRET_KEY>`.

For example:


```python
env = flyte.TaskEnvironment(
    name="my_task_env",
    secrets=[
        flyte.Secret(key="MY_SECRET_KEY", mount="/etc/flyte/secrets"),
    ]
)

@env.task
def t1():
    with open("/etc/flyte/secrets/MY_SECRET_KEY", "r") as f:
        my_secret_file_content = f.read()
        # Do something with the secret file content
    ...
```

> [!NOTE]
> Currently, to access a file secret you must specify a `mount` parameter value of `"/etc/flyte/secrets"`.
> This fixed path is the directory in which the secret file will be placed.
> The name of the secret file will be equal to the key of the secret.

> [!NOTE]
> A `TaskEnvironment` can only access a secret if the scope of the secret includes the project and domain where the `TaskEnvironment` is deployed.

> [!WARNING]
> Do not return secret values from tasks, as this will expose secrets to the control plane.
