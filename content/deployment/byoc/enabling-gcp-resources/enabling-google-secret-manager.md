---
title: Enabling Google Secret Manager
description: On a GCP data plane, Union.ai secrets are stored in Google Secret Manager in your own GCP project.
icon: safe
weight: 3
variants: -flyte +union
---

# Enabling Google Secret Manager

On a GCP data plane, {{< key product_name >}} secrets are stored in Google Secret Manager in your own GCP project.
Secret values stay in your project and never pass through the {{< key product_name >}} control plane.
See [Secrets management](../../../security/data-protection/secrets).

## Set up Secret Manager

The Union.ai team sets up Secret Manager when they set up your data plane: they enable the Secret Manager API in your GCP project and give the data plane access to it.
There is nothing else to configure.

## Create and use secrets

Manage secrets with `flyte create secret`, `flyte get secret`, and `flyte delete secret`, or in the UI, and request them with `flyte.Secret`:

* In tasks, including reusable environments, declare secrets on the task environment. See [Secrets](../../../user-guide/tasks/task-configuration/secrets).
* In apps, declare secrets on the app environment. See [App environment settings](../../../user-guide/apps/configure-apps/app-environment-settings).

> [!NOTE]
> A task can't request a Secret Manager secret that wasn't created through {{< key product_name >}}.
> To use such a value in a task, create it as a {{< key product_name >}} secret with `flyte create secret` or in the UI.
