---
title: Secrets
description: How Union Secrets are stored as Kubernetes secrets, and what to configure.
icon: safe
weight: 6
variants: -flyte +union
---

# Secrets

[Union Secrets](../../../user-guide/tasks/task-configuration/secrets) are managed secrets. With the `K8s` secret manager type, they are stored as native Kubernetes secrets.

Configure secret management under `proxy.secretManager` in the values file used by the helm chart:

- `enabled`: turns secret management on or off.
- `type`: the secret manager to use. This page covers `K8s`, the Kubernetes secret manager.
- `namespace`: with `type: K8s`, the namespace where Kubernetes secrets are stored. If this is not set, the release namespace is used.

Example:

```yaml
proxy:
  secretManager:
    enabled: true
    type: K8s
    # -- Set the namespace for union managed secrets created through the native Kubernetes secret manager. If the namespace is not set,
    # the release namespace will be used.
    namespace: "secret"
```
