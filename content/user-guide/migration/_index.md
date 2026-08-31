---
title: Migration
description: Port a Flyte 1 codebase to Flyte 2, or map Airflow concepts to their Flyte 2 equivalents.
icon: arrow-right
weight: 12
variants: +flyte +union
---

# Migration

Guides for migrating to Flyte 2 from other systems.

{{< grid >}}

{{< link-card target="flyte-2" icon="box-seam" title="From Flyte 1 to 2" >}}
What's new in Flyte 2 (pure Python execution, simplified API, fine-grained reproducibility) and how to port a Flyte 1 codebase.
{{< /link-card >}}

{{< link-card target="from-airflow" icon="git" title="From Airflow to Flyte" >}}
Mapping from Airflow concepts (DAGs, operators, schedules, XCom, trigger rules) to their Flyte 2 equivalents.
{{< /link-card >}}

{{< link-card target="from-slurm" icon="cpu" title="From Slurm to Flyte" >}}
Mapping from Slurm concepts (sbatch scripts, modules, job arrays, dependencies, partitions, requeue, multi-node jobs) to their Flyte 2 equivalents.
{{< /link-card >}}

{{< /grid >}}
