# Caching

Union allows you to cache the output of nodes ([tasks](./tasks/index), [subworkflows, and sub-launch plans](./workflows/subworkflows-and-sub-launch-plans)) to make subsequent executions faster.

Caching is useful when many executions with the same inputs may occur.

Here's a video with a brief explanation and demo, focused on task caching:

<iframe width="560" height="315" src="https://www.youtube.com/embed/WNkThCp-gqo?si=sFATJHv3avFRf6Tn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

```{note}
Caching is implemented at the node level of the workflow directed acyclic graph (DAG). Nodes in this sense include tasks, subworkflows (workflows called directly within another workflow), and sub-launch plans (launch plans called within a workflow).

Caching is not enabled for top-level workflows or launch plans (which are not invoked from within a parent workflow but rather via the UI or CLI).
```

## Caching configuration

There are four parameters and one command-line flag that pertain to caching:

### Parameters

* `cache`(`bool`): Enables or disables caching of the workflow, task, or launch plan.
By default, caching is disabled to avoid unintended consequences when caching executions with side effects.
To enable caching set `cache=True`.
* `cache_version` (`str`): Part of the cache key.
A change to this parameter will invalidate the cache.
This allows you to explicitly indicate when a change has been made to the node that should invalidate any existing cached results.
Note that this is not the only change that will invalidate the cache (see below).
Also, note that you can manually trigger cache invalidation per execution using the [`overwrite-cache` flag](#where-to-use-the-overwrite-cache-flag).
* `cache_serialize` (`bool`): Enables or disables [cache serialization](#cache-serialization).
When enabled, Union ensures that a single instance of the node is run before any other instances that would otherwise run concurrently.
This allows the initial instance to cache its result and lets the later instances reuse the resulting cached outputs.
Cache serialization is disabled by default.
* `cache_ignore_input_vars` (`Tuple[str, ...]`): Input variables that should not be included when calculating hash for cache. By default, no input variables are ignored. This parameter only applies to task serialization.

### Command-line flag `overwrite-cache`

*  `overwrite-cache` (`bool`): Invalidates the cache and forces re-execution of the node. This flag can be used when launching an execution from [the command line](#overwrite-cache-on-the-command-line), [the UI](#overwrite-cache-in-the-ui), or [programmatically through `UnionRemote`](#overwrite-cache-programmatically).

## Where to specify caching parameters

* Task caching parameters can be specified at task definition time within `@task` decorator or at task invocation time using `with_overrides` method.
* Workflow and launch plan caching parameters can be specified at invocation time using `with_overrides` method.

## Example

```{code-block} python
from flytekit import task, workflow, LaunchPlan
from typing import List


@task(cache=True, cache_version="1.0", cache_serialize=True)
def sum(a: int, b: int, c: int) -> int:
    return a + b + c


@workflow
def child_wf(a: int, b: int, c: int) -> List[int]:
    return [
        sum(a=a, b=b, c=c)
        for _ in range(5)
    ]


child_lp = LaunchPlan.get_or_create(child_wf)


@workflow
def parent_wf_with_subwf(input: int = 0):
    return [
        child_wf(a=input, b=3, c=4).with_overrides(cache=True, cache_version="1.0", cache_serialize=True)
        for i in [1, 2, 3]
    ]


@workflow
def parent_wf_with_sublp(input: int = 0):
     return [
        child_lp(a=input, b=1, c=2).with_overrides(cache=True, cache_version="1.0", cache_serialize=True)
        for i in [1, 2, 3]
    ]
```

In the above example, caching is enabled at multiple levels:
    * At the task level, in the `@task` decorator of the task `sum`.
    * At the workflow level, in the `with_overrides` method of the invocation of the workflow `child_wf`.
    * At the launch plan level, in the `with_overrides` method of the invocation of the launch plan `child_lp`.

In each case, the result of the execution is cached and reused in subsequent executions.
Here the reuse is demonstrated by calling the `child_wf` and `child_lp` workflows multiple times with the same inputs.
Additionally, if the same node is invoked again with the same inputs, even externally through the UI or CLI,
the cached result is returned immediately instead of re-executing the process.

## Where to use the `overwrite-cache` flag

When launching the execution of a workflow, launch plan or task, you can use the `overwrite-cache` flag to invalidate the cache and force re-execution.

### Overwrite cache on the command line

The `overwrite-cache` flag can be used from the command line with the `union run` command. For example:

```{code-block} shell
$ union run --remote  --overwrite-cache example.py wf
```

### Overwrite cache in the UI

You can also trigger cache invalidation when launching an execution from the UI by checking the **Override, in the launch dialog:

![Overwrite cache flag in the UI](/_static/images/user-guide/core-concepts/caching/overwrite-cached-outputs.png)

### Overwrite cache programmatically

When using `UnionRemote`, you can use the `overwrite_cache` parameter in the [`flytekit.remote.remote.FlyteRemote.execute`](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.remote.remote.FlyteRemote.html#flytekit.remote.remote.FlyteRemote.execute) method:

```{code-block} python
{@@ if byoc @@}
from flytekit.configuration import Config
{@@ endif @@}
from union.remote import UnionRemote

{@@ if serverless @@}
remote = UnionRemote()
{@@ elif byoc @@}
remote = UnionRemote(
    config=Config.auto(),
    default_project="flytesnacks",
    default_domain="development"
)
{@@ endif @@}

wf = remote.fetch_workflow(name="workflows.example.wf")
execution = remote.execute(wf, inputs={"name": "Kermit"}, overwrite_cache=True)
```

## How caching works

When a node (with caching enabled) completes on Union, a **key-value entry** is created in the **caching table**. The **value** of the entry is the output.
The **key** is composed of:

* **Project:** A task run under one project cannot use the cached task execution from another project which would cause inadvertent results between project teams that could result in data corruption.
* **Domain:** To separate test, staging, and production data, task executions are not shared across these environments.
* **Cache version:** When task functionality changes, you can change the `cache_version` of the task.
Flyte will know not to use older cached task executions and create a new cache entry on the subsequent execution.
* **Node signature:** The cache is specific to the signature associated with the execution.
The signature comprises the name, input parameter names/types, and the output parameter name/type of the node.
If the signature changes, the cache entry is invalidated.
* **Input values:** A well-formed Flyte node always produces deterministic outputs.
This means that, given a set of input values, every execution should have identical outputs.
When an execution is cached, the input values are part of the cache key.
If a node is run with a new set of inputs, a new cache entry is created for the combination of that particular entity with those particular inputs.

The result is that within a given project and domain, a cache entry is created for each distinct combination of name, signature, cache version, and input set for every node that has caching enabled.
If the same node with the same input values is encountered again, the cached output is used instead of running the process again.

### Cache version

When a change to code is made that should invalidate the cache for that node, you can explicitly indicate this by incrementing the `cache_version` parameter value.
For a task example, see below. (For workflows and launch plans, the parameter would be specified in the `with_overrides` method.)

```{code-block} python
@task(cache=True, cache_version="1.1", cache_serialize=True)
def t(n: int) -> int:
   return n * n + 1
```

Here the `cache_version` parameter has been bumped from `1.0`to `1.1`, resulting in the removal of the cache entries for that task.
The next time the task is called it will be executed and the result re-cached under an updated key.

Because the `cache_version` parameter must be explicitly changed, not every Git revision of a node will necessarily invalidate the cache.
A change in Git SHA does not necessarily correlate to a change in functionality.
You can refine the code without invalidating its outputs as long as you don't change the `cache_version` parameter (or the signature, see below) of the node.

The idea behind this is to decouple syntactic sugar (for example, changed documentation or renamed variables) from changes to logic that can affect the process's result.
When you use Git (or any version control system), you have a new version per code change.
Since the behavior of most nodes in a Git repository will remain unchanged, you don't want their cached outputs to be lost.

When a node's behavior does change though, you can bump `cache_version` to invalidate the cache entry and make the system recompute the outputs.

### Node signature

If you modify the signature of a node by adding, removing, or editing input parameters or output return types, Union invalidates the cache entries for that node.
During the next execution, Union executes the process again and caches the outputs as new values stored under an updated key.

{@@ if byoc @@}
### Caching when running locally

The description above applies to caching when executing a node remotely on your Union cluster.
Caching is also available [when running on a local cluster](../development-cycle/running-in-a-local-cluster).

When running locally the caching mechanism is the same except that the cache key does not include **project** or **domain** (since there are none).
The cache key is composed only of **cache version**, **signature**, and **inputs**.
The results of local executions are stored under `~/.flyte/local-cache/`.

Similar to the remote case, a local cache entry for a node will be invalidated if either the `cache_version` or the signature is modified.
In addition, the local cache can also be emptied by running

```{code-block} shell
$ union local-cache clear
```

which essentially removes the contents of the `~/.flyte/local-cache/` directory.
{@@ endif @@}

## Cache serialization

Cache serialization means only executing a single instance of a unique cacheable task (determined by the `cache_version` parameter and task signature) at a time.
Using this mechanism, Flyte ensures that during multiple concurrent executions of a task only a single instance is evaluated and all others wait until completion and reuse the resulting cached outputs.

Ensuring serialized evaluation requires a small degree of overhead to coordinate executions using a lightweight artifact reservation system.
Therefore, this should be viewed as an extension to rather than a replacement for non-serialized cacheable tasks.
It is particularly well fit for long-running or otherwise computationally expensive tasks executed in scenarios similar to the following examples:

* Periodically scheduled workflow where a single task evaluation duration may span multiple scheduled executions.
* Running a commonly shared task within different workflows (which receive the same inputs).

### Enabling cache serialization

Task cache serializing is disabled by default to avoid unexpected behavior for task executions.
To enable set `cache_serialize=True` in the `@task` decorator (this only has an effect if `cache=True` is also set)

The cache key definitions follow the same rules as non-serialized cache tasks.
It is important to understand the implications of the task signature and `cache_version` parameter in defining cached results.

```{code-block} python
@task(cache=True, cache_version="1.0", cache_serialize=True)
def t(n: int) -> int:
    return n * n
```

In the above example calling `t(n=2)` multiple times concurrently (even in different executions or workflows) will only execute the multiplication operation once.
Concurrently evaluated tasks will wait for completion of the first instance before reusing the cached results and subsequent evaluations will instantly reuse existing cache results.

### How does cache serialization work?

The cache serialization paradigm introduces a new artifact reservation system. Executions with cache serialization enabled use this reservation system to acquire an artifact reservation, indicating that they are actively evaluating a node, and release the reservation once the execution is completed.
Union uses a clock-skew algorithm to define reservation timeouts. Therefore, executions are required to periodically extend the reservation during their run.

The first execution of a serializable node will successfully acquire the artifact reservation.
Execution will be performed as usual and upon completion, the results are written to the cache, and the reservation is released.
Concurrently executed node instances (those that would otherwise run in parallel with the initial execution) will observe an active reservation, in which case these instances will wait until the next reevaluation and perform another check.
Once the initial execution completes, they will reuse the cached results as will any subsequent instances of the same node.

Union handles execution failures using a timeout on the reservation.
If the execution currently holding the reservation fails to extend it before it times out, another execution may acquire the reservation and begin processing.

## Caching of offloaded objects

In some cases, the default behavior displayed by Union’s caching feature might not match the user's intuition.
For example, this code makes use of pandas dataframes:

```{code-block} python
@task
def foo(a: int, b: str) -> pandas.DataFrame:
    df = pandas.DataFrame(...)
    ...
    return df


@task(cache=True, cache_version="1.0")
def bar(df: pandas.DataFrame) -> int:
    ...


@workflow
def wf(a: int, b: str):
    df = foo(a=a, b=b)
    v = bar(df=df)
```

If run twice with the same inputs, one would expect that `bar` would trigger a cache hit, but that’s not the case because of the way dataframes are represented in Union.

However, Union provides a new way to control the caching behavior of literals.
This is done via a `typing.Annotated` call on the node signature.
For example, in order to cache the result of calls to `bar`, you can rewrite the code above like this:

```{code-block} python
def hash_pandas_dataframe(df: pandas.DataFrame) -> str:
    return str(pandas.util.hash_pandas_object(df))


@task
def foo_1(a: int, b: str) -> Annotated[pandas.DataFrame, HashMethod(hash_pandas_dataframe)]:
    df = pandas.DataFrame(...)
    ...
    return df


@task(cache=True, cache_version="1.0")
def bar_1(df: pandas.DataFrame) -> int:
    ...


@workflow
def wf_1(a: int, b: str):
    df = foo(a=a, b=b)
    v = bar(df=df)
```

Note how the output of the task `foo` is annotated with an object of type `HashMethod`.
Essentially, it represents a function that produces a hash that is used as part of the cache key calculation in calling the task `bar`.

### How does caching of offloaded objects work?

Recall how input values are taken into account to derive a cache key.
This is done by turning the literal representation into a string and using that string as part of the cache key.
In the case of dataframes annotated with `HashMethod`, we use the hash as the representation of the literal.
In other words, the literal hash is used in the cache key.
This feature also works in local execution.

Here’s a complete example of the feature:

```{code-block} python
def hash_pandas_dataframe(df: pandas.DataFrame) -> str:
    return str(pandas.util.hash_pandas_object(df))


@task
def uncached_data_reading_task() -> Annotated[pandas.DataFrame, HashMethod(hash_pandas_dataframe)]:
    return pandas.DataFrame({"column_1": [1, 2, 3]})


@task(cache=True, cache_version="1.0")
def cached_data_processing_task(df: pandas.DataFrame) -> pandas.DataFrame:
    time.sleep(1)
    return df * 2


@task
def compare_dataframes(df1: pandas.DataFrame, df2: pandas.DataFrame):
    assert df1.equals(df2)


@workflow
def cached_dataframe_wf():
    raw_data = uncached_data_reading_task()

    # Execute `cached_data_processing_task` twice, but force those
    # two executions to happen serially to demonstrate how the second run
    # hits the cache.
    t1_node = create_node(cached_data_processing_task, df=raw_data)
    t2_node = create_node(cached_data_processing_task, df=raw_data)
    t1_node >> t2_node

    # Confirm that the dataframes actually match
    compare_dataframes(df1=t1_node.o0, df2=t2_node.o0)


if __name__ == "__main__":
    df1 = cached_dataframe_wf()
    print(f"Running cached_dataframe_wf once : {df1}")
```
