---
title: Apache Airflow agent
weight: 1
variants: +flyte -serverless +byoc +byok
---

# Apache Airflow agent

[Apache Airflow](https://airflow.apache.org) is a widely used open source platform for managing workflows with a robust ecosystem. Flyte provides an Airflow plugin that allows you to run Airflow tasks as Flyte tasks.
This allows you to use the Airflow plugin ecosystem in conjunction with Flyte's powerful task execution and orchestration capabilities.

> [!NOTE]
> The Airflow agent does not support all [Airflow operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html). We have tested many, but if you run into issues, please [file a bug report](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=bug%2Cuntriaged&projects=&template=bug_report.yaml&title=%5BBUG%5D+) or reach out to the Union team.

## Installation

To install the Airflow agent, run the following command:

```
pip install flytekitplugins-airflow
```

This integration has two components:
* **Airflow compiler:** This component compiles Airflow tasks to Flyte tasks, so Airflow tasks can be directly used inside the Flyte workflow.
* **Airflow agent:** This component allows you to execute Airflow tasks either locally or on a Flyte cluster.

## Example usage

> [!NOTE]
> You don't need an Airflow cluster to run Airflow tasks, since Flytekit will
> automatically compile Airflow tasks to Flyte tasks and execute them on the Airflow agent.

For a usage example, see [Airflow agent example](./airflow-agent-example.md).

## Local testing

Airflow doesn't support local execution natively. However, Flyte compiles Airflow tasks to Flyte tasks,
which enables you to test Airflow tasks locally in Flytekit's local execution mode.

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant byoc >}}
{{< markdown >}}

## Union cluster deployment

After you have finished testing the agent locally, contact the Union team to enable it in your cluster.

{{< /markdown >}}
{{< /variant >}}
