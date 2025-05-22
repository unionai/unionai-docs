---
title: Dynamic Job Spec
weight: 5
variants: +flyte -serverless -byoc -selfmanaged
---

# Dynamic Job Spec

A dynamic job spec is a subset of the entire workflow spec that defines a set of tasks, workflows, nodes, and output bindings that control how the job should assemble its outputs.

This spec is currently only supported as an intermediate step in running Dynamic Tasks.

```protobuf
message DynamicJobSpec {
repeated Node nodes = 1;
int64 min_successes = 2;
repeated Binding outputs = 3;
     repeated TaskTemplate tasks = 4;
     repeated WorkflowTemplate subworkflows = 5;
}
```
## Tasks
Defines one or more [tasks](../../tasks)  that can then be referenced in the spec.

## Subworkflows
Defines zero or more [workflows](../../workflows) that can then be referenced in the spec.

## Nodes
Defines one or more nodes that can run in parallel to produce the final outputs of the spec.

## Outputs
Defines one or more binding that instructs engine on how to assemble the final outputs.

