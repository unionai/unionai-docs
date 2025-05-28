---
title: Secrets
weight: 6
variants: -flyte -serverless -byoc +selfmanaged
---

# Secrets

[Union Secrets](../user-guide/development-cycle/managing-secrets.md) are enabled by default. Union Secrets are managed secrets created through the native Kubernetes secret manager.

The only configurable option is the namespace where the secret is stored. To override the default behavior, set `proxy.secretManager.namespace` in the values file used by the helm chart. If this is not specified, the `union` namespace will be used by default.

Example:
```yaml
proxy:
  secretManager:
    # -- Set the namespace for union managed secrets created through the native Kubernetes secret manager. If the namespace is not set,
    # the release namespace will be used.
    namespace: "secret"
```
