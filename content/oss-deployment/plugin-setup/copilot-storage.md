---
title: Flyte copilot storage configuration
variants: +flyte -union
weight: 1
---

# Flyte copilot storage configuration

**Flyte copilot** containers move task inputs and outputs between your object store
and the task pod. They run alongside every container task that declares inputs or
outputs, as an init container that downloads inputs and a sidecar that uploads outputs,
so they need their own credentials for the object store.

The chart gives copilot those credentials through a Kubernetes Secret, which the
plugin projects into the copilot containers as a file. The alternative, used when no
Secret is configured, is to pass the storage configuration on the copilot command
line, where the credentials land in the pod spec of every task and are readable by
anyone who can read pods in the task namespace.

## The Secret the chart creates

With the default `values.yaml` the chart renders the Secret for you and points copilot
at it. Nothing is required to enable this.

| | |
|---|---|
| Secret name | `<release>-flyte-binary-copilot-storage-config-secret` |
| Namespace | The task-pod namespace, `flyte-core-components.actions.kubernetes.namespace` (default `flyte`) |
| Key | `copilot-storage-config.yaml` |
| Config key that names it | `plugins.k8s.co-pilot.storage-config-secret-name` |
| Mount path in the copilot containers | `/etc/flyte/copilot` |

The configuration key is spelled `co-pilot`, with the hyphen, even though everything
else drops it. That is the plugin's key in the Flyte configuration, so copy it exactly.

The Secret is created in the **task-pod** namespace rather than the release namespace,
because a pod can only project Secrets from its own namespace. If you set the task-pod
namespace to something other than the namespace you install into, create that namespace
before running `helm install`.

The key holds the same `storage` block the deployment itself uses, with the credentials
inline:

```yaml
storage:
  type: stow
  stow:
    kind: s3
    config:
      region: us-east-1
      disable_ssl: false
      v2_signing: false
      auth_type: accesskey
      access_key_id: "<access-key-id>"
      secret_key: "<secret-key>"
  container: <your-bucket>
```

{{< note >}}
Copilot reads the whole stow configuration from this one file or not at all, so the
file has to be complete. A partial file leaves copilot with no credentials rather than
falling back to the rest.
{{< /note >}}

Storage settings you add through `configuration.inline` are merged into this Secret as
well, so copilot and the Flyte binary always talk to the same object store. This
matters for settings that have no dedicated value in `configuration.storage`, a session
token for example:

```yaml
configuration:
  inline:
    storage:
      stow:
        config:
          session_token: "<session-token>"
```

## When the chart does not create it

The Secret exists to keep credentials out of task pod specs, so the chart renders it
only when your storage configuration actually carries one:

| Storage configuration | Where copilot reads its configuration |
|---|---|
| `s3` with `authType: accesskey` and `secretKey` | The Secret the chart creates |
| `azure` with a `key` | The Secret the chart creates |
| Anything under `configuration.inline.storage` | The Secret the chart creates |
| `s3` with `authType: iam` | Its command line |
| `gcs` | Its command line |
| `azure` without a `key` | Its command line |
| `s3` with `authType: accesskey` and only `secretKeyPath` | Its command line |
| `configuration.storage.copilotStorageSecretRef` set | The Secret you name |
| `configuration.externalConfigMap` or `configuration.externalSecretRef` set | Whatever your own configuration says |

The command-line rows are not an exposure. Ambient authentication puts nothing secret
on the command line: `authType: iam` resolves credentials from the pod's IAM role, GCS
uses workload identity, and Azure without a `key` uses a managed identity. What travels
is a region, a bucket, and possibly an endpoint.

`configuration.inline.storage` always gets the Secret, whatever it holds, because the
chart cannot tell whether you put a session token or a service-account key in there.

The one credential that stays on the command line is `secretKeyPath`. It points at a
file inside the Flyte container, which a task pod has no copy of, so the chart cannot
read it to build a Secret. To close that exposure, supply your own Secret as shown
below.

## Supplying your own Secret

Create a Secret in the task-pod namespace holding your complete storage configuration,
then name it in `values.yaml`:

```bash
kubectl create secret generic my-copilot-storage \
  --namespace flyte \
  --from-file=copilot-storage-config.yaml=./copilot-storage-config.yaml
```

```yaml
configuration:
  storage:
    copilotStorageSecretRef: my-copilot-storage
```

The whole Secret is mounted and every `.yaml` key in it is read, so it must hold
nothing but copilot's configuration. You can split that configuration across several
keys if you prefer, for example `003-storage.yaml` and `013-storage-secrets.yaml`, and
they are merged in name order. Keys that do not end in `.yaml` are mounted but ignored.

## With external configuration

Setting `configuration.externalConfigMap` or `configuration.externalSecretRef` tells
the chart that you manage the Flyte configuration yourself. The chart then renders
neither the ConfigMap nor the Secret, which means it also does not render the copilot
Secret or the configuration key that names it.

{{< warning >}}
`configuration.storage.copilotStorageSecretRef` cannot be used here. The key it feeds
lives in the chart-rendered ConfigMap, which external configuration replaces, so the
chart fails the install rather than accepting a value it would ignore. Set the
configuration key yourself as shown below.
{{< /warning >}}

Two steps are needed.

**1. Create the Secret** in the task-pod namespace. Write copilot's storage
configuration to a file, using the same `storage` block your deployment uses and
including the credentials:

```yaml
# copilot-storage-config.yaml
storage:
  type: stow
  stow:
    kind: s3
    config:
      region: <region>
      auth_type: accesskey
      access_key_id: "<access-key-id>"
      secret_key: "<secret-key>"
  container: <your-bucket>
```

```bash
kubectl create secret generic my-copilot-storage \
  --namespace flyte \
  --from-file=copilot-storage-config.yaml=./copilot-storage-config.yaml
```

**2. Name it in your own configuration.** Add the key to the ConfigMap or Secret you
point `externalConfigMap` or `externalSecretRef` at:

```yaml
plugins:
  k8s:
    co-pilot:
      storage-config-secret-name: my-copilot-storage
```

Restart the Flyte deployment so it picks up the change, then run a task with inputs or
outputs to confirm.

## Verify

Check that a task pod projects the Secret and that no credentials appear in its spec:

```bash
# The copilot containers should mount the config, the primary container should not
kubectl get pod <task-pod> -n flyte \
  -o jsonpath='{range .spec.initContainers[*]}{.name}{"\t"}{.volumeMounts[*].mountPath}{"\n"}{end}'

# Should return nothing
kubectl get pod <task-pod> -n flyte -o yaml | grep -i secret_key
```

## Troubleshooting

- **Task pods stay in `ContainerCreating` with a `FailedMount` event.** The Secret named
  by `storage-config-secret-name` does not exist in the task-pod namespace. Confirm the
  namespace: the Secret has to live where the task pods run, not where Flyte runs.
- **Copilot containers exit at startup with a permissions error on the config file.**
  Your task pods run as a non-root user without an `fsGroup`. Flyte projects the file
  world-readable to cover this, so check that your deployment is new enough to include
  that fix.
- **Copilot fails to authenticate to the object store.** The mounted file is
  incomplete. Copilot takes the stow configuration all-or-nothing, so the file needs
  the endpoint and credentials, not just some of them.
- **Copilot reaches a different object store than the rest of Flyte.** You are supplying
  your own Secret, and it has drifted from the deployment's storage settings. Settings
  from `configuration.storage` and `configuration.inline` are merged only into the
  Secret the chart renders itself.
- **Storage credentials still appear in task pod specs.** No Secret is configured, so
  copilot is using the command-line fallback. With external configuration, check that
  you set `plugins.k8s.co-pilot.storage-config-secret-name` yourself.
- **`helm install` fails saying `copilotStorageSecretRef` has no effect.** You set it
  alongside `externalConfigMap` or `externalSecretRef`. Remove it and name your Secret
  through the configuration key instead, as described above.
- **Copilot refuses to start after you point it at your own Secret.** The Secret holds
  a `.yaml` key that is not copilot configuration. Every `.yaml` key is read, and
  copilot rejects configuration sections it does not recognize.
