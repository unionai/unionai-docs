---
title: Enabling Azure Key Vault
description: Grant the userflyterole identity permission to read Key Vault secrets.
icon: safe
weight: 3
variants: -flyte +union
---

# Enabling Azure Key Vault

> [!NOTE]
> This documentation exists for customers who must use Azure Key Vault for organizational reasons. For everyone else, we strongly recommend using the
> [{{< key product_name >}} secrets manager](../../../user-guide/tasks/task-configuration/secrets) to manage secrets rather than Azure Key Vault.

The {{< key product_name >}}-managed `userflyterole` identity must be granted permission to access [Azure Key Vault secrets](https://learn.microsoft.com/en-us/azure/key-vault/secrets/about-secrets).

> [!NOTE] Managing Azure Key Vault secrets
> Refer to [Azure official documentation](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal) for details on creating and managing secrets.

## Providing permissions to Azure Key Vault

{{< key product_name >}} data plane tasks employ Azure Workload Identity Federation to access Azure resources using an Azure user-assigned identity. Access to Azure Key Vault containers requires updating permissions to permit this {{< key product_name >}}-managed user-assigned identity.

[Create a role assignment](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal) assigning the `Key Vault Secrets User` role to the `userflyterole` user-assigned identity. Make sure it is scoped to the Azure Key Vault Secret.

> [!NOTE] {{< key product_name >}} managed user-assigned identities
> Refer to [Azure portal's user assigned managed identitites](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.ManagedIdentity%2FuserAssignedIdentities) if assistance is required identifying the `userflyterole` user-assigned identity within the {{< key product_name >}} data plane resource group.

## Accessing the secret within {{% key product_name %}}

* Declare a `flyte.Secret` in the `secrets` of your `TaskEnvironment`, where
  * `group` is the HTTP URI of the secret, in the format `https://<KEY_VAULT_NAME>.vault.azure.net/secrets/<SECRET_NAME>`
  * `key` is the secret name, `<SECRET_NAME>`
  * `mount` is `"/etc/flyte/secrets"`. Azure Key Vault secrets can only be delivered as files.
* Inside the task, read the secret from the file `/etc/flyte/secrets/<SECRET_NAME>`, with the name in lower case.

The latest version of the secret is always retrieved: `flyte.Secret` has no parameter for a secret version.

Here is an example:

```python
import pathlib

import flyte

VAULT_NAME = "examplevault"
SECRET_NAME = "example-secret"
SECRET_GROUP = f"https://{VAULT_NAME}.vault.azure.net/secrets/{SECRET_NAME}"

env = flyte.TaskEnvironment(
    name="azure-key-vault",
    secrets=[flyte.Secret(key=SECRET_NAME, group=SECRET_GROUP, mount="/etc/flyte/secrets")],
)

@env.task
def task_with_secret():
    secret_val = (pathlib.Path("/etc/flyte/secrets") / SECRET_NAME.lower()).read_text()
    # do something with the secret. For example, communication with an external API.
    ...
```
