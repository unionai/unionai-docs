---
title: Apache Airflow agent
weight: 1
variants: +flyte -serverless +byoc +byok
sidebar_expanded: true
---

# Apache Airflow agent

[Apache Airflow](https://airflow.apache.org) is a widely used open source platform for managing workflows with a robust ecosystem. {{< key product_name >}} provides an Airflow plugin that allows you to run Airflow tasks as {{< key product_name >}} tasks.
This allows you to use the Airflow plugin ecosystem in conjunction with {{< key product_name >}}'s powerful task execution and orchestration capabilities.

> [!NOTE]
> The Airflow agent does not support all [Airflow operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html). We have tested many, but if you run into issues, please [file a bug report](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=bug%2Cuntriaged&projects=&template=bug_report.yaml&title=%5BBUG%5D+) or reach out to the {{< key product_name >}} team.

## Installation

To install the Airflow agent, run the following command:

```
pip install flytekitplugins-airflow
```

This integration has two components:
* **Airflow compiler:** This component compiles Airflow tasks to {{< key product_name >}} tasks, so Airflow tasks can be directly used inside the {{< key product_name >}} workflow.
* **Airflow agent:** This component allows you to execute Airflow tasks either locally or on a {{< key product_name >}} cluster.

## Example usage

> [!NOTE]
> You don't need an Airflow cluster to run Airflow tasks, since {{< key kit_name >}} will
> automatically compile Airflow tasks to {{< key product_name >}} tasks and execute them on the Airflow agent.

For a usage example, see [Airflow agent example](./airflow-agent-example).

## Local testing

Airflow doesn't support local execution natively. However, {{< key product_name >}} compiles Airflow tasks to {{< key product_name >}} tasks,
which enables you to test Airflow tasks locally in {{< key kit_name >}}'s local execution mode.

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant byoc >}}
{{< markdown >}}

## {{< key product_name >}} cluster deployment

After you have finished testing the agent locally, contact the {{< key product_name >}} team to enable it in your cluster.

{{< /markdown >}}
{{< /variant >}}
