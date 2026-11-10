---
title: Enabling Google Secret Manager
description: Flyte 2 tasks can't read secrets created directly in Google Secret Manager. Use Union.ai secrets, which a GCP data plane stores in your own Secret Manager.
icon: safe
weight: 3
variants: -flyte +union
---

# Enabling Google Secret Manager

Flyte 2 tasks can't request a secret that you create directly in Google Secret Manager.
The data plane fetches such a secret only when the request names both the secret and a secret version, and `flyte.Secret` has no field for a secret version.

Use [Union.ai secrets](../../../user-guide/tasks/task-configuration/secrets) instead.
On a GCP data plane, Union.ai secrets are stored in Google Secret Manager, in your data plane's GCP project.
Create them with `flyte create secret` or in the UI, and read them in a task with `flyte.Secret`.
The values stay in your own Secret Manager and never pass through the {{< key product_name >}} control plane.
See [Secrets management](../../../security/data-protection/secrets).

> [!NOTE]
> AWS Secrets Manager and Azure Key Vault work differently.
> A Flyte 2 task can read a secret that already exists in either of them.
> See [Enabling AWS Secrets Manager](../enabling-aws-resources/enabling-aws-secrets-manager) and [Enabling Azure Key Vault](../enabling-azure-resources/enabling-azure-key-vault).
