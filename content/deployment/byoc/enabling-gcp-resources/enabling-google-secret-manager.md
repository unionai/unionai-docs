---
title: Enabling Google Secret Manager
description: Use Google Secret Manager secrets in Flyte 2 tasks, through Union.ai secrets stored in your own Secret Manager or by reading Secret Manager from task code.
icon: safe
weight: 3
variants: -flyte +union
---

# Enabling Google Secret Manager

On a GCP data plane, Union.ai secrets are stored in Google Secret Manager, in your data plane's GCP project.
A Flyte 2 task can use a Secret Manager secret in two ways:

* **As a Union.ai secret.** Create it with `flyte create secret`, in the UI, or directly in Secret Manager under the name Union.ai expects. The task reads it with `flyte.Secret`.
* **By calling the Secret Manager API from task code.** Use this for a secret that must keep its own name, for example because other systems already read it.

A task can't request an arbitrary Secret Manager secret by name through `flyte.Secret`.
The data plane fetches such a secret only when the request names a secret version, and `flyte.Secret` has no field for a version.

> [!NOTE]
> AWS Secrets Manager and Azure Key Vault work differently.
> A Flyte 2 task can request a secret that already exists in either of them through `flyte.Secret`.
> See [Enabling AWS Secrets Manager](../enabling-aws-resources/enabling-aws-secrets-manager) and [Enabling Azure Key Vault](../enabling-azure-resources/enabling-azure-key-vault).

## Use Union.ai secrets

Create a secret with `flyte create secret` or in the UI, and read it in a task with `flyte.Secret`, as described in [Secrets](../../../user-guide/tasks/task-configuration/secrets).
The value is stored in Google Secret Manager in your data plane's GCP project, and never passes through the {{< key product_name >}} control plane.
See [Secrets management](../../../security/data-protection/secrets).

### Secret names in Secret Manager

Each Union.ai secret is a Secret Manager secret whose name encodes its scope:

| Scope | Secret Manager name |
|---|---|
| Organization | `u__org__<org>__domain____project____key__<key>` |
| Domain | `u__org__<org>__domain__<domain>__project____key__<key>` |
| Project and domain | `u__org__<org>__domain__<domain>__project__<project>__key__<key>` |

Replace `<org>` with your organization, `<domain>` and `<project>` with the scope, and `<key>` with the secret's key.
The scope fields are empty for a scope the secret doesn't have, which leaves four underscores in a row.

For example, this command in organization `acme`:

```bash
flyte create secret openai-api-key --value <your-api-key> --project ml --domain production
```

creates the Secret Manager secret `u__org__acme__domain__production__project__ml__key__openai-api-key`.

Other systems with access to your Secret Manager can read the secret under that name, so you don't need to store the value twice.

### Add a secret directly in Secret Manager

To make a value from your own tooling available to tasks, create the Secret Manager secret in your data plane's GCP project, under a name from the table above.
It is then a Union.ai secret: it appears in `flyte get secret` and in the UI, and a task reads it with `flyte.Secret(key="<key>")`.

* A task gets the secret's latest version.
* If a key exists at more than one scope, the task gets the most specific one: project and domain, then domain, then organization.

> [!WARNING] Rotating a secret
> The data plane caches secret values for up to 24 hours.
> A new version added directly in Secret Manager can take that long to reach tasks.
> To rotate a secret immediately, update it in the UI, which clears the cache.

## Read Secret Manager from task code

For a secret that keeps its own name, call the Secret Manager API from the task.
Task code runs as the `<UserFlyteGSA>` (see [Enabling GCP resources](./_index)), which can read secrets in your data plane's GCP project by default.

```python
import flyte

env = flyte.TaskEnvironment(
    name="gcp-secret-manager",
    image=flyte.Image.from_debian_base().with_pip_packages("google-cloud-secret-manager"),
)


@env.task
def call_api() -> None:
    from google.cloud import secretmanager

    client = secretmanager.SecretManagerServiceClient()
    name = "projects/<project-id>/secrets/<secret-name>/versions/latest"
    api_key = client.access_secret_version(name=name).payload.data.decode("utf-8")
    # Use api_key to call the external API.
```

Replace `<project-id>` with the GCP project that holds the secret and `<secret-name>` with its name.
The task reads the value when it runs, so a new version takes effect on the next run.

> [!WARNING]
> Do not return secret values from tasks. Returned values are stored in plaintext in your data plane's object store and shown in the UI and to downstream tasks.

### Secrets in another GCP project

To read a secret stored in a GCP project other than your data plane's, grant the `<UserFlyteGSA>` access to it:

1. Find the email address of the `<UserFlyteGSA>` in your data plane's GCP project (see [Enabling GCP resources](./_index)).
2. In the GCP project that holds the secret, go to **Security → Secret Manager**.
3. Select the secret, then select **GRANT ACCESS**.
4. Under **Add principals**, enter the email address of the `<UserFlyteGSA>`.
5. Under **Assign roles**, add **Secret Manager Secret Accessor**.
6. Save the changes.
