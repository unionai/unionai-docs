---
title: Node groups
description: Inspect and update the node groups a cluster declares, the node shapes it can schedule onto.
icon: server
weight: 5
variants: -flyte +union
---

# Node groups

> [!NOTE] Requires the `flyteplugins-union` plugin
> The `flyte get node-groups` and `flyte update node-groups` commands are
> provided by `flyteplugins-union` 0.19.0 or later. Reading and writing the
> `limits` and `max_pods` fields needs `flyteplugins-union` 0.20.0 or later and
> a control plane that supports them. Install it with
> `pip install flyteplugins-union`.

A cluster's **node groups** are the node shapes it can schedule onto: for each
group, the instance types, the node count range, the allocatable CPU and memory
of one node, the pod slots per node, accelerators, architecture, capacity
types, weight, limits, labels, and taints. Use `flyte get node-groups` to see
what a [cluster](./clusters) declares. On a cluster you manage, and on a
control plane that accepts node group writes, use `flyte update node-groups`
to change it (see [Who can write node groups](#who-can-write-node-groups)).

## Inspect node groups

```bash
# Show the node groups as a table
flyte get node-groups my-cluster

# Show them as JSON
flyte -of json get node-groups my-cluster

# Save them as YAML, in the format `flyte update node-groups -f` reads
flyte get node-groups my-cluster --export > node-groups.yaml
```

The output shows the node groups as stored, including every label and taint.
The table has one row per group, with the columns **Name**, **Instance types**,
**Nodes**, **Limits**, **Cpu**, **Memory**, **Accelerators**, **Arch**,
**Capacity**, **Weight**, **Spot**, **Labels**, and **Taints**. **Nodes** shows
`min-max`, or, with `flyteplugins-union` 0.20.0 or later, `min+ (no node limit)`
when `max_nodes` is `0`. **Limits** (0.20.0 or later) shows the group's limits,
for example `cpu=20000, nvidia.com/gpu=2`.

The exported YAML lists every editable field of each group, using the field
names of the `NodeGroup` message:

```yaml
node_groups:
- name: cpu
  min_nodes: 0
  max_nodes: 10
  node_disk_size_gbs: 0
  node_instance_types:
  - m5.xlarge
  spot_instances: false
  allocatable_resources: []
  labels: {}
  taints: []
  accelerators: []
  architecture: NODE_ARCHITECTURE_UNSPECIFIED
  capacity_types: []
  max_pods: 0
  limits: {}
```

`weight` is optional and appears only when a group has one (1 to 100, the
Karpenter NodePool weight). `capacity_types` takes `CAPACITY_TYPE_ON_DEMAND`,
`CAPACITY_TYPE_SPOT`, and `CAPACITY_TYPE_RESERVED`.

`max_pods` and `limits` appear with `flyteplugins-union` 0.20.0 or later. On a
control plane that supports them:

- `max_nodes: 0` means the group has no node-count bound. Only `limits`, if
  set, caps it.
- `limits` is the Karpenter NodePool `spec.limits`: totals the group may not
  exceed across all its nodes, as a Kubernetes resource name and a quoted
  quantity, for example `cpu: '20000'`. The command rejects a bare number
  before it writes anything, and the control plane rejects a value that isn't a
  non-negative quantity.
- `max_pods` is the number of pod slots on one node of the group. `0` means it
  isn't recorded.

## Update node groups

```bash
# Edit the node groups in your $EDITOR
flyte update node-groups my-cluster

# Apply node groups from a YAML file
flyte update node-groups my-cluster -f node-groups.yaml
```

An update **replaces the cluster's complete set** of node groups. A group you
leave out of the edited YAML or the file is removed from the cluster. To change
one group with `-f`, export the current set, edit it, and apply the whole file.
A provisioning run that writes the cluster's spec also replaces its node groups
with the set that spec declares.

Before it writes, the command prints which groups are added, removed, or
changed, by name. If any group would be removed, it asks you to confirm. Pass
`--yes` to skip the prompt. If you decline, nothing is written. If the prompt
gets no answer (end of input or Ctrl-C), the command fails with
`removal of node groups not confirmed; pass --yes to apply non-interactively`.

The command refuses these inputs before it writes anything:

- **A document that declares nothing.** An empty file, a file with only
  comments, or `{}` is rejected. To remove every node group, write
  `node_groups: []`.
- **Duplicate names.** Each node group needs a unique name.
- **Fields your plugin doesn't know.** If the control plane returns node group
  fields that your version of `flyteplugins-union` can't represent, writing
  would drop them, so `update` refuses and tells you to upgrade
  `flyteplugins-union`. `get --export` prints a warning to stderr and leaves
  those fields out of the YAML.

In the editor, a validation error asks whether to edit again, save the YAML to
a file you can apply with `--file`, or abort. Errors that editing can't fix,
such as a permission or conflict error, end the command instead.

### Concurrent edits

When the control plane reports a generation for the node groups, the editor
path sends the generation it read with the write. If the node groups changed in
between, the write is refused with
`node groups changed since they were read`. Re-run the command to edit the
current set.

If the control plane reports generation `0` (it doesn't track one, or the node
groups have never been written), the editor sends no generation and prints a
notice that the last write wins. `-f` never sends a generation:
the file always replaces whatever is stored.

### Who can write node groups

The control plane decides whether you may write a cluster's node groups. Node
groups of a cluster that {{< key product_name >}} provisions (BYOC) are managed
by provisioning, so a write to one is refused, and the CLI shows the control
plane's error. A cluster with no recorded type is refused the same way.

If your control plane doesn't accept node group writes, every update fails
with `this control plane does not accept node group writes yet`.
