---
title: Classes
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`flytekitplugins.dbt.error.DBTHandledError`](../packages/flytekitplugins.dbt.error#flytekitpluginsdbterrordbthandlederror) |DBTHandledError wraps error logs and message from command execution that returns ``exit code 1``. |
| [`flytekitplugins.dbt.error.DBTUnhandledError`](../packages/flytekitplugins.dbt.error#flytekitpluginsdbterrordbtunhandlederror) |DBTUnhandledError wraps error logs and message from command execution that returns ``exit code 2``. |
| [`flytekitplugins.dbt.schema.BaseDBTInput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemabasedbtinput) |Base class for DBT Task Input. |
| [`flytekitplugins.dbt.schema.BaseDBTOutput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemabasedbtoutput) |Base class for output of DBT task. |
| [`flytekitplugins.dbt.schema.DBTFreshnessInput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtfreshnessinput) |Input to DBT Freshness task. |
| [`flytekitplugins.dbt.schema.DBTFreshnessOutput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtfreshnessoutput) |Output of DBT Freshness task. |
| [`flytekitplugins.dbt.schema.DBTRunInput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtruninput) |Input to DBT Run task. |
| [`flytekitplugins.dbt.schema.DBTRunOutput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbtrunoutput) |Output of DBT run task. |
| [`flytekitplugins.dbt.schema.DBTTestInput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbttestinput) |Input to DBT Test task. |
| [`flytekitplugins.dbt.schema.DBTTestOutput`](../packages/flytekitplugins.dbt.schema#flytekitpluginsdbtschemadbttestoutput) |Output of DBT test task. |
| [`flytekitplugins.dbt.task.DBTFreshness`](../packages/flytekitplugins.dbt.task#flytekitpluginsdbttaskdbtfreshness) |Execute DBT Freshness CLI command. |
| [`flytekitplugins.dbt.task.DBTRun`](../packages/flytekitplugins.dbt.task#flytekitpluginsdbttaskdbtrun) |Execute DBT Run CLI command. |
| [`flytekitplugins.dbt.task.DBTTest`](../packages/flytekitplugins.dbt.task#flytekitpluginsdbttaskdbttest) |Execute DBT Test CLI command. |
