# Artifacts

Artifacts are entities designed to explicitly reference the outputs of Union tasks or workflows, such as models, files, or any other kind of data. Artifacts allow you to store additional metadata for these outputs in the form of [partitions](#partitions), which are key-value pairs that describe the artifact and which can be used to query the Artifact Service to locate artifacts. Artifacts allow for loose coupling of workflows—for example, a downstream workflow can be configured to consume the latest result of an upstream workflow.

## Versioning

Artifacts are uniquely identified and versioned by the following information:
* Project
* Domain
* Artifact name
* Artifact version

You can set an artifact's name in code when you [declare the artifact](declaring-artifacts) and the artifact version is automatically generated when the artifact is materialized as part of any task or workflow execution that emits an artifact with this name. Any execution of a task or workflow that emits an artifact creates a new version of that artifact.

## Partitions

When you declare an artifact, you can define partitions for it that enable semantic grouping of artifacts. Partitions are metadata that take the form of key-value pairs, with the keys defined at registration time and the values supplied at runtime. You can specify up to 10 partition keys for an artifact. You can set an optional partition called `time_partition` to capture information about the execution timestamp to your desired level of granularity. For more information, see [Declaring artifacts](declaring-artifacts).

:::{note}
The `time_partition` partition is not enabled by default. To enable it, set `time_partitioned=True` in the artifact declaration. For more information, see the [time-partitioned artifact example](declaring-artifacts.md#time-partitioned-artifact).
:::

## Queries

To consume an artifact in a workflow, you can define a query containing the artifact’s name as well as any required partition values. You then supply the query as an input value to the workflow definition. At execution time, the query will return the most recent version of the artifact that meets the criteria by default. You can also query for a specific artifact version.

For more information on querying for and consuming artifacts in workflows, see [Consuming artifacts in workflows](consuming-artifacts-in-workflows).

To query for artifacts programmatically in a Python script using `UnionRemote`, see [UnionRemote](../../development-cycle/unionremote.md#fetching-artifacts).

:::{admonition} UnionRemote vs FlyteRemote
`UnionRemote` is identical to `FlyteRemote`, with additional functionality to handle artifacts. You cannot interact with artifacts using FlyteRemote.
:::

## Lineage

Once an artifact is materialized, its lineage is visible in the Union console. For more information, see [Artifact view](../../web-console/artifact-view).

```{toctree}
:maxdepth: 2
:hidden:

declaring-artifacts
materializing-artifacts
consuming-artifacts-in-workflows
connecting-workflows-with-artifact-event-triggers
```