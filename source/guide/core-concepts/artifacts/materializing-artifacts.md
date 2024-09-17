# Materializing artifacts

You can materialize an artifact by executing the task or workflow that emits the artifact.

In the example below, to materialize the `BasicArtifact` artifact, the `t1` task must be executed. The `wf` workflow runs the `t1` task three times with different values for the `key1` partition each time. Note that each time `t1` is executed, it emits a new version of the `BasicArtifact` artifact.

{@@ if byoc @@}
:::{note}
To use the example code on this page, you will need to add your `registry` to the `pandas_image` ImageSpec block.
:::
{@@ endif @@}

```{literalinclude} ../../_static/includes/core-concepts/artifacts/partition_keys_runtime.py
:language: python
```

:::{note}
You can also materialize an artifact by executing the `create_artifact` method of `UnionRemote`. For more information, see the [UnionRemote documentation](../../development-cycle/union-remote.md#creating-artifacts).
:::
