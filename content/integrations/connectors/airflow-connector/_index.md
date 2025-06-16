---
title: Airflow connector
weight: 1
variants: +flyte -serverless +byoc +selfmanaged
sidebar_expanded: false
---

# Airflow connector

[Apache Airflow](https://airflow.apache.org) is a widely used open source platform for managing workflows with a robust ecosystem. {{< key product_name >}} provides an Airflow plugin that allows you to run Airflow tasks as {{< key product_name >}} tasks.
This allows you to use the Airflow plugin ecosystem in conjunction with {{< key product_name >}}'s powerful task execution and orchestration capabilities.

> [!NOTE]
> The Airflow connector does not support all [Airflow operators](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html).
> We have tested many, but if you run into issues,
> please [file a bug report](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=bug%2Cuntriaged&projects=&template=bug_report.yaml&title=%5BBUG%5D+).

## Installation

To install the plugin, run the following command:

`pip install flytekitplugins-airflow`

This plugin has two components:
* **Airflow compiler:** This component compiles Airflow tasks to {{< key product_name >}} tasks, so Airflow tasks can be directly used inside the {{< key product_name >}} workflow.
* **Airflow connector:** This component allows you to execute Airflow tasks either locally or on a {{< key product_name >}} cluster.

> [!NOTE]
> You don't need an Airflow cluster to run Airflow tasks, since flytekit will
> automatically compile Airflow tasks to {{< key product_name >}} tasks and execute them on the Airflow connector.

## Example usage

{{< variant flyte >}}
{{< markdown >}}

For an example query, see [Airflow connector example usage](./airflow-connector-example-usage)

{{< /markdown >}}
{{< /variant >}}
{{< variant byoc selfmanaged >}}
{{< markdown >}}

For an example query, see [Airflow connector example usage](./airflow-connector-example-usage-union)

{{< /markdown >}}
{{< /variant >}}

## Local testing

Airflow doesn't support local execution natively. However, {{< key product_name >}} compiles Airflow tasks to {{< key product_name >}} tasks,
which enables you to test Airflow tasks locally in flytekit's local execution mode.

> [!NOTE]
> In some cases, you will need to store credentials in your local environment when testing locally.

{{< variant flyte >}}
{{< markdown >}}

## Flyte deployment configuration

To enable the Airflow connector in your Flyte deployment, see the [Airflow connector deployment guide](../../../deployment/flyte-connectors/airflow).

{{< /markdown >}}
{{< /variant >}}

