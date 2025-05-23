---
title: Enabling Azure Key Vault
weight: 3
variants: -flyte -serverless +byoc -selfmanaged
---

# Enabling Azure Key Vault

> [!NOTE]
> This documentation exists for customers who must use Azure Key Vault for organizational reasons. For everyone else, we strongly recommend using the
> [{{< key product_name >}} secrets manager](../../user-guide/development-cycle/managing-secrets) to manage secrets rather than Azure Key Vault.

The {{< key product_name >}}-managed `userflyterole` identity must be granted permission to access [Azure Key Vault secrets](https://learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets).

> [!NOTE] Managing Azure Key Vault secrets
> Refer to [Azure official documentation](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal) for details on creating and managing secrets.

## Providing permissions to Azure Key Vault

{{< key product_name >}} data plane tasks employ Azure Workload Identity Federation to access Azure resources using an Azure user-assigned identity. Access to Azure Key Vault containers requires updating permissions to permit this {{< key product_name >}}-managed user-assigned identity.

[Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) assigning the `Key Vault Secrets User` role to the `userflyterole` user-assigned identity. Make sure it is scoped to the Azure Key Vault Secret.

> [!NOTE] {{< key product_name >}} managed user-assigned identities
> Refer to [Azure portal's user assigned managed identitites](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities) if assistance is required identifying the `userflyterole` user-assigned identity within the {{< key product_name >}} data plane resource group.

## Accessing the secret within {{< key product_name >}}

* Define a `Secret` object where
  * `Secret.group` is the a HTTP URI of the format `https://<KEY_VAULT_NAME>.vault.azure.net/secrets/<SECRET_NAME>`
  * `Secret.group_version` can be omitted to retrieve the latest version or set to an explicit secret version
  * `Secret.mount_requirement` is `Secret.MountType.FILE`
* Pass that `Secret` object in the `secret_requests` parameter of the `@{{< key kit_as >}}.task` decorator.
* Inside the task code, retrieve the value of the secret with:
  * `{{< key kit_as >}}.current_context().secrets.get(<SECRET_NAME>)` if `Secret.group_version` was omitted.
  * `{{< key kit_as >}}.current_context().secrets.get(<SECRET_NAME>, group_version=SECRET_GROUP_VERSION)` if `Secret.group_version` was specified.

Here are examples:

```python
import {{< key kit_import >}}

VAULT_NAME = "examplevault"
SECRET_NAME = "example-secret"

SECRET_GROUP = f"https://{VAULT_NAME}.vault.azure.net/secrets/{SECRET_NAME}"
SECRET_GROUP_VERSION = "12345"

SECRET_REQUEST_WITH_VERSION = {{< key kit_as >}}.Secret(
  group=SECRET_GROUP,
  group_version=SECRET_GROUP_VERSION,
  mount_requirement={{< key kit_as >}}.Secret.MountType.FILE
)

@{{< key kit_as >}}.task(secret_requests=[SECRET_REQUEST_WITH_VERSION])
def task_with_versioned_secret():
    secret_val = {{< key kit_as >}}.current_context().secrets.get(
        SECRET_NAME,
        group_version=SECRET_GROUP_VERSION
    )

SECRET_REQUEST_FOR_LATEST = union.Secret(
  group=SECRET_GROUP,
  mount_requirement={{< key kit_as >}}.Secret.MountType.FILE
)

@{{< key kit_as >}}.task(secret_requests=[SECRET_REQUEST_FOR_LATEST])
def task_with_latest_secret():
    secret_val = {{< key kit_as >}}.current_context().secrets.get(
        SECRET_NAME
    )
```
