---
title: Secrets
description: Store API keys and credentials securely and read them from inside a task.
icon: safe
weight: 3
variants: +flyte +union
---

# Secrets

Flyte secrets enable you to securely store and manage sensitive information, such as API keys, passwords, and other credentials.
Secrets reside in a secret store on the data plane of your Union/Flyte backend.
You can create, list, and delete secrets in the store using the Flyte CLI or SDK.
Secrets in the store can be accessed and used within your workflow tasks, without exposing any cleartext values in your code.

## Creating a literal string secret

You can create a secret using the [`flyte create secret`](../../../api-reference/flyte-cli#flyte-create-secret) command like this:

```bash
flyte create secret MY_SECRET_KEY --value my_secret_value
```

This will create a secret called `MY_SECRET_KEY` with the value `my_secret_value`.
This secret will be scoped to your entire organization.
It will be available across all projects and domains in your organization.
See the [scoping secrets](#scoping-secrets) section below for more details.
See [Using a literal string secret](#using-a-literal-string-secret) for how to access the secret in your task code.

## Creating a file secret

You can also create a secret by specifying a local file:

```bash
flyte create secret MY_SECRET_KEY --from-file /local/path/to/my_secret_file
```

In this case, when accessing the secret in your task code, you will need to [mount it as a file](#using-a-file-secret).

{{< variant union >}}
{{< markdown >}}

## Creating a secret in the UI

You can also create and manage secrets in the {{< key product_name >}} UI:

* **Organization-wide secrets:** open **Settings** and select **Secrets** under **Assets & Configuration**.
* **Project- or domain-scoped secrets:** navigate into a project and domain, then select **Secrets** in the main sidebar.

Secrets created in the UI are the same secrets that the CLI and SDK create, so they can be used from both Flyte 1 and Flyte 2 tasks.

Admins can create, update, and delete any secret.
Contributors can manage secrets within the projects they are assigned to.
See [Role-based access control](../../../security/identity-and-access/rbac).

{{< /markdown >}}
{{< /variant >}}

## Scoping secrets

When you create a secret without specifying a project or domain, as we did above, the secret is scoped to the organization level.
This means that the secret will be available across all projects and domains in the organization.

{{< variant union >}}
{{< markdown >}}
If your organization spans multiple cluster pools, see [Org-wide secrets in a multi-cluster deployment](#org-wide-secrets-in-a-multi-cluster-deployment) below: org-wide secrets are stored per pool.
{{< /markdown >}}
{{< /variant >}}

You can optionally specify `--domain`, or both `--project` and `--domain`, to restrict the scope of the secret to:

* A specific domain (across all projects)
* A specific project and a specific domain.

For example, to create a secret that it is only available in `my_project/development`, you would execute the following command:

```bash
flyte create secret MY_SECRET_KEY --value my_secret_value --project my_project --domain development
```

{{< variant union >}}
{{< markdown >}}

## Org-wide secrets in a multi-cluster deployment

Each [cluster pool](../../cluster-workload-management/cluster-pools) has its own secret store, declared as part of the pool's data plane configuration.
A secret therefore lives in the secret store of one particular pool, not in a single global store.

If your organization has more than one [cluster pool](../../cluster-workload-management/cluster-pools), you must name the pool explicitly with the `--cluster-pool` flag.
All three secret commands accept it:

```bash
# Create an org-wide secret in the `prod` pool's secret store
flyte create secret MY_SECRET_KEY --value my_secret_value --cluster-pool prod

# List the org-wide secrets in that pool
flyte get secret --cluster-pool prod

# Delete an org-wide secret from that pool
flyte delete secret MY_SECRET_KEY --cluster-pool prod
```

Use `flyte get cluster-pool` to list the pool names available in your organization.

To make the same org-wide secret available to workloads in every pool, create it once per pool.

```python
import flyte
import flyte.remote

flyte.init_from_config()

flyte.remote.Secret.create(name="MY_SECRET_KEY", value="my_secret_value", cluster_pool="prod")

for secret in flyte.remote.Secret.listall(cluster_pool="prod"):
    print(secret.name)
```

{{< /markdown >}}
{{< /variant >}}

## Listing secrets

You can list existing secrets with the [`flyte get secret`](../../../api-reference/flyte-cli#flyte-get-secret) command.
For example, the following command will list all secrets in the organization:

```bash
flyte get secret
```

Specifying `--domain`, or both `--project` and `--domain`, will list the secrets that are **only** available in that domain, or in that project and domain.

For example, to list the secrets that are only available in `my_project` and domain `development`, you would run:

```bash
flyte get secret --project my_project --domain development
```

## Deleting secrets

To delete a secret, use the [`flyte delete secret`](../../../api-reference/flyte-cli#flyte-delete-secret) command:

```bash
flyte delete secret MY_SECRET_KEY
```

## Declaring secrets in a task environment

A task can only read a secret that it declares.
Declare secrets with the `secrets` parameter of `flyte.TaskEnvironment`, using one or more `flyte.Secret` objects:

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    secrets=[
        # Injected as the environment variable OPENAI_API_KEY
        flyte.Secret(key="openai-api-key", as_env_var="OPENAI_API_KEY"),
        # Injected as the environment variable MY_DB_PASSWORD (default name derived from the key)
        flyte.Secret(key="my-db-password"),
        # Mounted as the file /etc/flyte/secrets/my_cert
        flyte.Secret(key="my_cert", mount="/etc/flyte/secrets"),
    ],
)
```

`flyte.Secret` takes the following parameters:

| Parameter | Description |
|-----------|-------------|
| `key` | The name of the secret in the secret store, exactly as you created it (for example, with `flyte create secret`). Required. |
| `as_env_var` | The name of the environment variable to inject the secret into. Must be a valid uppercase environment variable name (`^[A-Z_][A-Z0-9_]*$`). |
| `mount` | Set to `"/etc/flyte/secrets"` to mount the secret as a file instead of an environment variable. No other path is supported. |
| `group` | Optional. Used by some secret stores to organize secrets. If set, it is prepended to the default environment variable name. |

Set either `as_env_var` or `mount`, not both.
If you set both, the secret is injected as an environment variable.

If you set neither, the secret is injected as an environment variable whose name is derived from the key: uppercased, with `-` replaced by `_`, and prefixed with the group if one is given.
For example, `flyte.Secret(key="my-db-password")` is injected as `MY_DB_PASSWORD`, and `flyte.Secret(key="password", group="db")` as `DB_PASSWORD`.

As a shorthand, you can pass a key string instead of a `flyte.Secret` object: `secrets="my-db-password"` is equivalent to `secrets=flyte.Secret(key="my-db-password")`.

## Using a literal string secret

To use a literal string secret, specify it in the `TaskEnvironment` along with the name of the environment variable into which it will be injected.
You can then access it using `os.getenv()` in your task code.
For example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/secrets/secrets.py" fragment="literal" lang="python" >}}

## Using a file secret

To use a file secret, specify it in the `TaskEnvironment` along with the `mount="/etc/flyte/secrets"` argument (with that precise value).

The file will be mounted at `/etc/flyte/secrets/<SECRET_KEY>`.

For example:

{{< code file="/unionai-examples/v2/user-guide/task-configuration/secrets/secrets.py" fragment="file" lang="python" >}}

> [!NOTE]
> Currently, to access a file secret you must specify a `mount` parameter value of `"/etc/flyte/secrets"`.
> This fixed path is the directory in which the secret file will be placed.
> The name of the secret file is the key of the secret exactly as you created it, including its case.
> For example, a secret created as `MY_CERT` is mounted at `/etc/flyte/secrets/MY_CERT`.

{{< variant union >}}
{{< markdown >}}
The path above applies to secrets created with `flyte create secret`, the SDK, or the UI.
Secrets read directly from an external store use a different, provider-specific path:
see [AWS Secrets Manager](../../../deployment/byoc/enabling-aws-resources/enabling-aws-secrets-manager),
[Azure Key Vault](../../../deployment/byoc/enabling-azure-resources/enabling-azure-key-vault),
or [Google Secret Manager](../../../deployment/byoc/enabling-gcp-resources/enabling-google-secret-manager).
{{< /markdown >}}
{{< /variant >}}

## Using secrets in local runs

When you run a task locally, for example with `flyte run --local` or by calling the task directly in Python, secrets are **not** fetched from the secret store.
Your code reads secrets from environment variables and files, so you need to provide those yourself in your local environment.

### Environment variable secrets

Export an environment variable with the name that the task reads.
This is the `as_env_var` name, or the [default name derived from the key](#declaring-secrets-in-a-task-environment).
For the literal string secret example above:

```bash
export MY_SECRET_ENV_VAR=my_secret_value
flyte run --local secrets.py task_1
```

### File secrets

A file secret created with `flyte create secret`, the SDK, or the UI is read from `/etc/flyte/secrets/<SECRET_KEY>`.
For a secret from an external store, use that provider's path instead.
To simulate the secret locally, create the file at that path:

```bash
sudo mkdir -p /etc/flyte/secrets
echo -n 'my_secret_value' | sudo tee /etc/flyte/secrets/my_secret > /dev/null
```

Writing to `/etc` usually needs `sudo`.
To avoid that, you can build the path from the `FLYTE_SECRETS_DEFAULT_DIR` environment variable.
It is set to `/etc/flyte/secrets` in the task container when a file secret is mounted, so locally you can point it at any directory you like:

```python
import os

@env_2.task
def task_2():
    secrets_dir = os.getenv("FLYTE_SECRETS_DEFAULT_DIR", "/etc/flyte/secrets")
    with open(os.path.join(secrets_dir, "my_secret")) as f:
        my_secret_file_content = f.read()
```

```bash
mkdir -p ~/.flyte-secrets
echo -n 'my_secret_value' > ~/.flyte-secrets/my_secret
export FLYTE_SECRETS_DEFAULT_DIR=~/.flyte-secrets
flyte run --local secrets.py task_2
```

> [!WARNING]
> Do not commit local secret files or `export` lines containing secret values to source control.

## Overriding secrets at invocation time

The secrets above are declared when the task is defined, on the `TaskEnvironment`.
You can also override which secrets are injected for a **single invocation** of a task using `task.override(secrets=...)` &mdash; useful when the same task needs different credentials depending on how it's called.
See [Overriding secrets](./overrides#overriding-secrets) for details and an example.

> [!NOTE]
> A `TaskEnvironment` can only access a secret if the scope of the secret includes the project and domain where the `TaskEnvironment` is deployed.

> [!WARNING]
> Do not return secret values from tasks. Returned values are stored in plaintext in your data plane's object store and shown in the UI and to downstream tasks, defeating the secret store's protections.
