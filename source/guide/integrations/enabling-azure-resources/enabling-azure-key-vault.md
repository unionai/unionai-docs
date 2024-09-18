# Enabling Azure Key Vault

```{note}
This documentation exists for customers who must use Azure Key Vault for organizational reasons. For everyone else, we strongly recommend using the [Union secrets manager](../../development-cycle/managing-secrets) to manage secrets rather than Azure Key Vault.
```

The Union-managed `userflyterole` identity must be granted permission to access [Azure Key Vault secrets](https://learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets).

:::{admonition} Managing Azure Key Vault secrets

Refer to [Azure official documentation](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal) for details on  creating and managing secrets.

:::

## Providing permissions to Azure Key Vault

Union data plane tasks employ Azure Workload Identity Federation to access Azure resources using an Azure user-assigned identity. Access to Azure Key Vault containers requires updating permissions to permit this Union-managed user-assigned identity.

[Create a role assignment]((https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal)) assigning the `Key Vault Secrets User` role to the `userflyterole` user-assigned identity. Make sure it is scoped to the Azure Key Vault Secret.

:::{admonition} Union managed user-assigned identities

Refer to [Azure portal's user assigned managed identitites](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities) if assistance is required identifying the `userflyterole` user-assigned identity within the Union data plane resource group.

:::

## Accessing the secret within Union

* Define a `Secret` object where
  * `Secret.group` is the a HTTP URI of the format `https://<KEY_VAULT_NAME>.vault.azure.net/secrets/<SECRET_NAME>`
  * `Secret.group_version` can be omitted to retrieve the latest version or set to an explicit secret version
  * `Secret.mount_requirement` is `Secret.MountType.FILE`
* Pass that `Secret` object in the `secret_requests` parameter of the `@task` decorator.
* Inside the task code, retrieve the value of the secret with:
  * `flytekit.current_context().secrets.get(<SECRET_NAME>)` if `Secret.group_version` was omitted.
  * `flytekit.current_context().secrets.get(<SECRET_NAME>, group_version=SECRET_GROUP_VERSION)`  if `Secret.group_version` was specified.

Here are examples:

```{code-block} python
import flytekit
from flytekit import task, workflow, Secret

VAULT_NAME = "examplevault"
SECRET_NAME = "example-secret"

SECRET_GROUP = f"https://{VAULT_NAME}.vault.azure.net/secrets/{SECRET_NAME}"
SECRET_GROUP_VERSION = "12345"

SECRET_REQUEST_WITH_VERSION = Secret(
  group=SECRET_GROUP,
  group_version=SECRET_GROUP_VERSION,
  mount_requirement=Secret.MountType.FILE
)

@task(secret_requests=[SECRET_REQUEST_WITH_VERSION])
def task_with_versioned_secret():
    secret_val = flytekit.current_context().secrets.get(
        SECRET_NAME,
        group_version=SECRET_GROUP_VERSION
    )

SECRET_REQUEST_FOR_LATEST = Secret(
  group=SECRET_GROUP,
  mount_requirement=Secret.MountType.FILE
)

@task(secret_requests=[SECRET_REQUEST_FOR_LATEST])
def task_with_latest_secret():
    secret_val = flytekit.current_context().secrets.get(
        SECRET_NAME
    )
```
