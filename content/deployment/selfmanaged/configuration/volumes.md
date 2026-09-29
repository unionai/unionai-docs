---
title: Volumes
description: Configure the durable, versioned file systems tasks mount and read and write.
icon: hdd
weight: 9
variants: -flyte +union
---

# Volumes

[Volumes](../../../user-guide/tasks/task-programming/volumes) give tasks a durable,
versioned file system that they mount and read and write like a local directory.
A Volume is served **inside the task pod** by
[FUSE](https://www.kernel.org/doc/html/latest/filesystems/fuse.html), so on a
self-managed cluster the data plane must give task pods a way to get a FUSE
mount. By default it gives them none, and you enable one of two DaemonSets per
cluster:

| | **Mount broker** (recommended) | **FUSE device plugin** (legacy) |
|---|---|---|
| Chart value | `uvolMountBroker.enabled` | `fuseDevicePlugin.enabled` |
| Task pod privileges | **None** | `CAP_SYS_ADMIN` + the `smarter-devices/fuse` device |
| Who calls `mount(2)` | The broker, on the node | The task pod itself |
| Task image needs `fuse3` | No | Yes |
| Task code | `allow_volumes()` | `flyte.PodTemplate().allow_fuse()` |

Prefer the **mount broker**: it is the only option that leaves the task pod
completely unprivileged, so Volumes work under restricted Pod Security
Standards. The device plugin remains supported for clusters already using it,
and the two can be enabled together during a migration. Each task pod picks its
path from its own pod template, so existing `allow_fuse()` workloads keep
running unchanged.

## Enable the mount broker

The broker is a **CSI node driver** that runs as its own DaemonSet. It premounts
a FUSE channel inside the kubelet publish target for each volume-using pod and
hands that open file descriptor to the pod's in-process client over a unix
socket. The pod adopts the descriptor instead of mounting, so it performs no
`mount(2)` and needs **no `CAP_SYS_ADMIN`, no `/dev/fuse`, and no `hostPath`**.
Privilege is confined to the DaemonSet; the workloads it serves stay fully
unprivileged. The broker holds no object-storage credentials: the data plane
authenticates in-pod under the pod's own identity.

It is **disabled by default**. Enable it in your data plane values:

```yaml
uvolMountBroker:
  enabled: true
```

```bash
helm upgrade <release> <chart> -n <namespace> \
  -f values.yaml \
  --set uvolMountBroker.enabled=true
```

> [!WARNING]
> The broker's default `nodeSelector` is `flyte.org/node-role: worker`, and it
> **must cover every node a volume-using task pod can land on**. A pod that
> lands on a node without the broker fails to start with
> `driver volumes.union.ai not found` (or whatever `driverName` you set). If your task pods are not confined to
> nodes carrying that label, widen the selector or remove it:
>
> ```yaml
> uvolMountBroker:
>   enabled: true
>   nodeSelector: null   # run on every node
> ```
>
> Use `null`, not `{}`. Helm merges your values over the chart's, and an empty
> map contributes nothing to that merge, so `nodeSelector: {}` leaves the
> default `flyte.org/node-role: worker` in place. Only an explicit `null`
> removes the key. This one fails quietly: the DaemonSet stays pinned to the
> labeled nodes while you believe it is running everywhere, which is the
> failure this warning is about.

### Verify the broker

Confirm the DaemonSet is rolled out on every eligible node:

```bash
kubectl get daemonset union-uvol-broker -n <namespace>
```

Readiness means kubelet has actually registered the CSI driver, not merely that
the process started, so a ready pod is a node that can serve a mount. Confirm
the driver is registered cluster-wide, using whatever you set
`uvolMountBroker.driverName` to (the default is `volumes.union.ai`):

```bash
kubectl get csidriver volumes.union.ai
```

Once both look healthy, tasks using `allow_volumes()` can mount Volumes.

### Broker configuration reference

| Key | Default | Description |
|---|---|---|
| `uvolMountBroker.enabled` | `false` | Enable the mount-broker DaemonSet and its `CSIDriver`. |
| `uvolMountBroker.driverName` | `volumes.union.ai` | CSI driver name. Task pods reference it; change it only if it collides. |
| `uvolMountBroker.nodeSelector` | `{"flyte.org/node-role": "worker"}` | Nodes to run on. Must cover every node a volume task pod can schedule to. Set it to `null` (not `{}`) to run on every node. |
| `uvolMountBroker.tolerations` | `[{ effect: NoSchedule, operator: Exists }]` | Tolerate `NoSchedule` taints so it reaches tainted worker nodes. |
| `uvolMountBroker.kubeletDir` | `/var/lib/kubelet` | Kubelet root. Change it if your kubelet uses a non-standard directory. |
| `uvolMountBroker.socketDir` | `/run/uvol` | Host directory for the per-volume unix sockets. |
| `uvolMountBroker.stateDir` | `/var/lib/uvol/state` | Host directory for the broker's state journal (lets channels survive a broker restart). |
| `uvolMountBroker.profilerPort` | `10254` | Port serving `/metrics`, `/healthcheck` and the `/readyz` readiness endpoint. |
| `uvolMountBroker.metricsScope` | `uvol_broker` | Prefix for the metrics the broker emits. |
| `uvolMountBroker.priorityClassName` | `system-node-critical` | Priority class for the DaemonSet pods. |
| `uvolMountBroker.resources` | `requests: cpu 500m, memory 32Mi`; `limits: memory 256Mi` | The broker sits on the task's `open()` hot path, so the CPU request is a scheduling-latency knob rather than a utilization estimate. There is deliberately no CPU limit. |

> [!NOTE]
> The broker is safe to upgrade in place: existing kernel mounts and the file
> descriptors held by running pods survive a restart, and the state journal plus
> client re-registration resume the rest.

## The FUSE device plugin (legacy path)

Use this only on clusters that cannot run the mount broker. Task pods take the
mount themselves, so they need `CAP_SYS_ADMIN` and their images need `fuse3`.

### Why a device plugin is required

Mounting a FUSE file system requires the pod to open the host `/dev/fuse`
character device. Simply exposing `/dev/fuse` through a `hostPath` is **not**
enough: the kernel's devices cgroup denies the `open()` with `EPERM`, because a
`hostPath` surfaces the device node but cannot add it to the pod's
devices-cgroup allowlist. The only thing that adds a device to that allowlist is
kubelet, and kubelet only does so when the pod **requests the device as a
device-plugin resource**.

The dataplane chart ships an opt-in **FUSE device-plugin DaemonSet** that
advertises the host `/dev/fuse` device as the Kubernetes extended resource
`smarter-devices/fuse`. When it is enabled, a task pod that requests
`smarter-devices/fuse` gets `/dev/fuse` injected into its devices-cgroup
allowlist and can complete the mount with only the `CAP_SYS_ADMIN` capability:
**no privileged container and no `/dev/fuse` hostPath**.

{{< variant union >}}
{{< markdown >}}

> [!NOTE]
> Union.ai adds the `smarter-devices/fuse` request and the
> `CAP_SYS_ADMIN` capability to volume-mounting task pods automatically. You only
> need to enable the device plugin; your users do not change their task code.
> Privilege is confined to the DaemonSet; the workloads it serves stay
> unprivileged.

{{< /markdown >}}
{{< /variant >}}

### Enable the FUSE device plugin

The DaemonSet is **disabled by default**. Enable it in your data plane values:

```yaml
fuseDevicePlugin:
  enabled: true
```

Apply the change with a Helm upgrade, layering it onto your existing platform
values:

```bash
helm upgrade <release> <chart> -n <namespace> \
  -f values.yaml \
  --set fuseDevicePlugin.enabled=true
```

Enabling it is the only required step. Because the chart renders nothing for this
feature when it is off, turning it on does not affect any other workloads.

### Restrict the plugin to specific nodes (optional)

By default the DaemonSet runs on **every** node (it tolerates all taints). To run
it only where unprivileged FUSE is wanted, label those nodes and set a
`nodeSelector`:

```bash
kubectl label node <node-name> union.ai/fuse=true
```

```yaml
fuseDevicePlugin:
  enabled: true
  nodeSelector:
    union.ai/fuse: "true"
```

> [!WARNING]
> A volume-mounting task scheduled onto a node where the plugin is **not** running
> cannot mount its Volume and the task will fail. If you restrict the plugin with
> a `nodeSelector`, make sure volume workloads are scheduled onto the labeled
> nodes (for example with matching task resources or node selectors), or omit the
> `nodeSelector` so the resource is advertised on all nodes.

### Verify the device plugin

After the upgrade, confirm the DaemonSet is rolled out:

```bash
kubectl get daemonset -n <namespace> -l app.kubernetes.io/name=fuse-device-plugin
```

Then confirm a node advertises the extended resource:

```bash
kubectl get node <node-name> -o jsonpath='{.status.allocatable.smarter-devices/fuse}{"\n"}'
# 1000
```

A non-zero value means pods on that node can request `smarter-devices/fuse` and
mount Volumes.

### Device-plugin configuration reference

The `fuseDevicePlugin` values block in the dataplane chart:

| Key | Default | Description |
|---|---|---|
| `fuseDevicePlugin.enabled` | `false` | Enable the FUSE device-plugin DaemonSet. |
| `fuseDevicePlugin.devices` | `[{ devicematch: ^fuse$, nummaxdevices: 1000 }]` | Devices the plugin advertises. `nummaxdevices` is the per-node claim count. |
| `fuseDevicePlugin.nodeSelector` | `{}` | Restrict the DaemonSet to selected nodes; empty means all nodes. |
| `fuseDevicePlugin.tolerations` | `[{ operator: Exists }]` | Tolerate everything so it lands on every selected node, including tainted ones. |
| `fuseDevicePlugin.securityContext` | drops `ALL`, adds `SYS_ADMIN` | The plugin needs `SYS_ADMIN` to read host devices and register with kubelet; the workloads it serves stay unprivileged. |
| `fuseDevicePlugin.priorityClassName` | `""` | Override the priority class (defaults to `operator.priorityClassName`). |
| `fuseDevicePlugin.resources` | `cpu: 10m–100m`, `memory: 15Mi` | Resource requests and limits for the plugin pod. |

## Using Volumes

Once one of the two DaemonSets is enabled, no further cluster setup is needed.
Users create and mount Volumes directly from their task code, with
`allow_volumes()` on the broker, or `flyte.PodTemplate().allow_fuse()` on the
device plugin. See the
[Volumes user guide](../../../user-guide/tasks/task-programming/volumes) for the
programming model.
