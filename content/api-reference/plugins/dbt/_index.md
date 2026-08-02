---
title: DBT
version: 1.16.26
variants: +flyte +union
layout: py_api
---

# DBT



## Directory

### Classes

| Class | Description |
|-|-|
| [`flytekitplugins.dbt.error.DBTHandledError`](flytekitplugins.dbt.error#flytekitpluginsdbterrordbthandlederror) | DBTHandledError wraps error logs and message from command execution that returns ``exit code 1``. |
| [`flytekitplugins.dbt.error.DBTUnhandledError`](flytekitplugins.dbt.error#flytekitpluginsdbterrordbtunhandlederror) | DBTUnhandledError wraps error logs and message from command execution that returns ``exit code 2``. |
| [`flytekitplugins.dbt.schema.BaseDBTInput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemabasedbtinput) | Base class for DBT Task Input. |
| [`flytekitplugins.dbt.schema.BaseDBTOutput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemabasedbtoutput) | Base class for output of DBT task. |
| [`flytekitplugins.dbt.schema.DBTFreshnessInput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtfreshnessinput) | Input to DBT Freshness task. |
| [`flytekitplugins.dbt.schema.DBTFreshnessOutput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtfreshnessoutput) | Output of DBT Freshness task. |
| [`flytekitplugins.dbt.schema.DBTRunInput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtruninput) | Input to DBT Run task. |
| [`flytekitplugins.dbt.schema.DBTRunOutput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtrunoutput) | Output of DBT run task. |
| [`flytekitplugins.dbt.schema.DBTTestInput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbttestinput) | Input to DBT Test task. |
| [`flytekitplugins.dbt.schema.DBTTestOutput`](flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbttestoutput) | Output of DBT test task. |
| [`flytekitplugins.dbt.task.DBTFreshness`](flytekitplugins.dbt.task#flytekitpluginsdbttaskdbtfreshness) | Execute DBT Freshness CLI command. |
| [`flytekitplugins.dbt.task.DBTRun`](flytekitplugins.dbt.task#flytekitpluginsdbttaskdbtrun) | Execute DBT Run CLI command. |
| [`flytekitplugins.dbt.task.DBTTest`](flytekitplugins.dbt.task#flytekitpluginsdbttaskdbttest) | Execute DBT Test CLI command. |

### Functions

| Function | Description |
|-|-|
| [`flytekitplugins.dbt.util.run_cli()`](flytekitplugins.dbt.util#run_cli) | Execute a CLI command in a subprocess. |

### Packages

| Package | Description |
|-|-|
| [`flytekitplugins.dbt.error`](flytekitplugins.dbt.error) |  |
| [`flytekitplugins.dbt.schema`](flytekitplugins.dbt.schema) |  |
| [`flytekitplugins.dbt.task`](flytekitplugins.dbt.task) |  |
| [`flytekitplugins.dbt.util`](flytekitplugins.dbt.util) |  |

