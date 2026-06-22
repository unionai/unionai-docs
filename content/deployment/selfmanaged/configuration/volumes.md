---
title: Volumes
weight: 9
variants: -flyte +union
---

# Volumes

[Volumes](../../../user-guide/task-programming/volumes) give tasks a durable,
versioned file system that they mount and read and write like a local directory.
A Volume is mounted **inside the task pod** with [FUSE](https://www.kernel.org/doc/html/latest/filesystems/fuse.html)
(JuiceFS), so on a self-managed cluster the data plane must allow task pods to
perform a FUSE mount. By default it does not — you enable it per cluster by
turning on the **FUSE device-plugin DaemonSet** described below.

## Why a device plugin is required

Mounting a FUSE file system requires the pod to open the host `/dev/fuse`
character device. Simply exposing `/dev/fuse` through a `hostPath` is **not**
enough: the kernel's devices cgroup denies the `open()` with `EPERM`, because a
`hostPath` surfaces the device node but cannot add it to the pod's
devices-cgroup allowlist. The only thing that adds a device to that allowlist is
kubelet, and kubelet only does so when the pod **requests the device as a
device-plugin resource**.

The dataplane chart ships an opt-in [`smarter-device-manager`](https://gitlab.com/arm-research/smarter/smarter-device-manager)
DaemonSet that advertises the host `/dev/fuse` device as the Kubernetes extended
resource `smarter-devices/fuse`. When it is enabled, a task pod that requests
`smarter-devices/fuse` gets `/dev/fuse` injected into its devices-cgroup
allowlist and can complete the mount with only the `CAP_SYS_ADMIN` capability —
**no privileged container and no `/dev/fuse` hostPath**.

{{< variant union >}}
{{< markdown >}}

> [!NOTE]
> {{< key product_name >}} adds the `smarter-devices/fuse` request and the
> `CAP_SYS_ADMIN` capability to volume-mounting task pods automatically. You only
> need to enable the device plugin — your users do not change their task code.
> Privilege is confined to the DaemonSet; the workloads it serves stay
> unprivileged.

{{< /markdown >}}
{{< /variant >}}

## Enable the FUSE device plugin

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

## Restrict the plugin to specific nodes (optional)

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

## Verify

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

## Configuration reference

The `fuseDevicePlugin` values block in the dataplane chart:

| Key | Default | Description |
|---|---|---|
| `fuseDevicePlugin.enabled` | `false` | Enable the FUSE device-plugin DaemonSet. |
| `fuseDevicePlugin.image.repository` | `registry.gitlab.com/arm-research/smarter/smarter-device-manager` | Device-manager image. |
| `fuseDevicePlugin.image.tag` | `v1.20.11` | Image tag. |
| `fuseDevicePlugin.devices` | `[{ devicematch: ^fuse$, nummaxdevices: 1000 }]` | Devices advertised, in `smarter-device-manager` `conf.yaml` format. `nummaxdevices` is the per-node claim count. |
| `fuseDevicePlugin.nodeSelector` | `{}` | Restrict the DaemonSet to selected nodes; empty means all nodes. |
| `fuseDevicePlugin.tolerations` | `[{ operator: Exists }]` | Tolerate everything so it lands on every selected node, including tainted ones. |
| `fuseDevicePlugin.securityContext` | drops `ALL`, adds `SYS_ADMIN` | The plugin needs `SYS_ADMIN` to read host devices and register with kubelet; the workloads it serves stay unprivileged. |
| `fuseDevicePlugin.priorityClassName` | `""` | Override the priority class (defaults to `operator.priorityClassName`). |
| `fuseDevicePlugin.resources` | `cpu: 10m–100m`, `memory: 15Mi` | Resource requests and limits for the plugin pod. |

## Using Volumes

Once the device plugin is enabled, no further setup is needed — users create and
mount Volumes directly from their task code. See the
[Volumes user guide](../../../user-guide/task-programming/volumes) for the
programming model.
