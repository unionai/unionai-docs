---
title: From Airflow to Flyte
weight: 2
variants: +flyte +union
---

# From Airflow to Flyte

A staged guide to migrating Airflow DAGs to Flyte 2.

The migration is split by operator family. Each section maps an Airflow construct to its Flyte 2 equivalent and links to a runnable example pair (an Airflow DAG and its Flyte port) in the [`unionai/airflow-examples`](https://github.com/unionai/airflow-examples/tree/main/guide/examples) repo.

{{< grid >}}

{{< link-card target="part-1-vanilla-operators" title="Part 1 — vanilla operators" >}}
PythonOperator, TaskFlow, BashOperator, KubernetesPodOperator, plus DAG schedules, the driver task model, and orchestration patterns (parallelism, conditionals, error handling).
{{< /link-card >}}

{{< /grid >}}

> [!NOTE]
> **Part 2** (later) covers provider operators: Beam, Dataproc, BigQuery, Databricks, Spark, and sensors.
