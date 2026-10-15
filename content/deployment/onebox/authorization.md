---
title: Authorization
description: Turn on role-based access control in onebox, choose who gets which role, and keep the in-cluster task port private.
icon: person-check
weight: 6
variants: -flyte +union
---

# Authorization

Onebox can enforce role-based access control. It is **off by default**: every request is allowed, whoever sends it. Turn it on when more than one person uses onebox, after you put an [authenticating proxy](./authentication) in front of it.

```yaml
authz:
  enabled: true
  adminUsers: [<subject>]   # as your proxy reports them
  defaultRole: viewer       # admin, contributor or viewer
```

```shell
helm upgrade onebox unionai/onebox -n union -f values.yaml
```

## How roles are assigned

- Every user listed in `adminUsers` is an admin. Onebox applies the list when it starts, so adding a user and upgrading makes them an admin, also if they have signed in before.
- Every other user gets `defaultRole` the first time they make a request. Changing `defaultRole` later applies to users onebox hasn't seen yet.
- A request without identity headers is refused with `401 Unauthenticated`.

| Role | Can |
|---|---|
| `admin` | Everything, including creating projects. |
| `contributor` | Launch, abort, and follow runs, and read and write their data, in every project. |
| `viewer` | Read runs, actions, logs, and data. |

Users are identified by the **subject** your proxy reports, which isn't always their email. To find a user's subject, have them open `https://<onebox host>/me` in the browser while signed in:

```text
{"subject": "00u1a2b3c4d5", "email": "alice@example.com", "name": "Alice", ...}
```

## Tasks

Tasks call back to onebox to launch and follow their child actions. They do this on an in-cluster port, `8082`, where every request acts as a built-in application with role `authz.tasksRole` (default `contributor`). No credentials are placed in task pods.

Whatever can reach port `8082` gets that role, so keep it private with a network policy.

## Network policy

With `authz.enabled`, the chart also creates a NetworkPolicy that:

- lets only pods in onebox's namespace reach the task ports (`8082` and `15606`);
- lets only your proxy reach the API port (`80`), when you name it in `networkPolicy.proxyFrom`.

```yaml
networkPolicy:
  proxyFrom:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: auth
      podSelector:
        matchLabels:
          app.kubernetes.io/name: oauth2-proxy
```

A NetworkPolicy only takes effect if your cluster's network plugin enforces it, as Calico, Cilium, and the AWS VPC CNI with network policy enabled do. Without that, any pod in the cluster can reach port `8082` and act with `authz.tasksRole`.

Set `networkPolicy.enabled: false` only if you enforce the same rules another way; the chart prints a warning when you do.

## Gotchas

| Symptom | Cause and fix |
|---|---|
| Every request returns `401` after turning authorization on | Requests reach onebox without identity headers. Check that they go through the proxy, and that `identity.subjectHeaders` names the header your proxy sets. |
| A user listed in `adminUsers` isn't an admin | The entry doesn't match their subject. Compare it with `subject` from `/me`. |
| Child actions fail with `PermissionDenied` | `authz.tasksRole` is `viewer`. Tasks need `contributor` to launch child actions. |
