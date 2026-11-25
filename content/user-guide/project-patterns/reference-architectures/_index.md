---
title: Reference architectures
description: End-to-end designs for training and serving, batch inference, and an agent platform, showing which constructs to combine and how data moves between them.
icon: diagram-3
weight: 7
variants: +flyte +union
---

# Reference architectures

A reference architecture is a complete design for one kind of workload. It names the tasks, apps, and triggers involved, the hardware each one runs on, and how data moves between them. Each page here starts with a diagram, then maps every box to the construct that implements it and the page that documents it.

Use these pages to choose a starting design. The linked pages carry the details and the tested examples.

## Building blocks

Every architecture in this section is built from the same parts:

| Part | Construct | Use it for |
|---|---|---|
| Task environment | `flyte.TaskEnvironment` | A unit of batch work with its own image, resources, secrets, and cache. See [Tasks](../../tasks/_index). |
| Driver task | A task whose environment lists the others in `depends_on` | Calling other tasks in plain Python: loops, branches, and fan-out. See [Multiple environments](../../tasks/task-configuration/multiple-environments). |
| App | `flyte.app.AppEnvironment` and its subclasses | A long-running service that answers HTTP requests. See [Apps](../../apps/_index). |
| Trigger | `flyte.Trigger` | Starting a task on a schedule or on demand with saved inputs. See [Triggers](../../triggers/_index). |
| Data passing | `flyte.io.File`, `flyte.io.Dir`, and `flyte.io.DataFrame` | Moving datasets and weights between steps by reference to object storage. See [Files and directories](../../tasks/task-programming/files-and-directories). |

{{< variant union >}}
{{< markdown >}}

On {{< key product_name >}}, two more parts connect these architectures to each other:

| Part | Construct | Use it for |
|---|---|---|
| Artifact | `flyte.artifacts.new()` | Naming and versioning a task's output so tasks, triggers, and apps can refer to it by name. See [Artifacts](../../artifacts/_index). |
| Artifact trigger | `flyte.Trigger` with `flyte.OnArtifact` | Running a task when a new version of an artifact lands. See [Trigger on new artifact versions](../../triggers/artifact-triggers). |

{{< /markdown >}}
{{< /variant >}}

## Architectures

{{< grid >}}

{{< link-card target="training-and-serving" icon="gpu-card" title="Training and serving" >}}
Prepare data, train on GPUs, evaluate, and serve the trained model behind an endpoint.
{{< /link-card >}}

{{< link-card target="batch-inference" icon="stack" title="Batch inference" >}}
Run a model over a large dataset on a schedule, with the model loaded once and the GPU kept busy.
{{< /link-card >}}

{{< link-card target="agent-platform" icon="robot" title="Agent platform" >}}
Run durable agents that call models, tools, MCP servers, and sandboxes, started on demand, on a schedule, or from a webhook.
{{< /link-card >}}

{{< /grid >}}
