# Caching

Union allows you to cache the output of nodes ([tasks](./tasks/index.md), [subworkflows, and sub-launch plans](./workflows/subworkflows-and-sub-launch-plans.md)) to make subsequent executions faster.

Caching is useful when many executions with the same inputs may occur.

Here's a video with a brief explanation and demo, focused on task caching:

<iframe width="560" height="315" src="https://www.youtube.com/embed/WNkThCp-gqo?si=sFATJHv3avFRf6Tn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

```{note}
Caching is implemented at the node level of the workflow directed acyclic graph (DAG).
Nodes in this sense include tasks, subworkflows (workflows called directly within another workflow), and sub-launch plans (launch plans called within a workflow).
Caching is not available for top-level workflows or launch plans (that is, those invoked from UI or CLI).
By default, caching is disabled on all tasks, subworkflows and sub-launch plans, to avoid unintended consequences when caching executions with side effects.
```


## Cache configuration

Cache configuration can be done by setting the `cache` parameter of the `@union.task` decorator or `with_overrides` method to a `Cache` object:

The [Cache class](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.Cache.html#flytekit-cache) takes the following parameters:

* `version` (`Optional[str]`): Part of the cache key.
A change to this parameter will invalidate the cache.
This allows you to explicitly indicate when a change has been made to the node that should invalidate any existing cached results.
Note that this is not the only change that will invalidate the cache (see below).
Also, note that you can manually trigger cache invalidation per execution using the [`overwrite-cache` flag](#where-to-use-the-overwrite-cache-flag).
If not set, the version will be generated based on the specified cache policies.
When using `cache=True`, [as shown below](#default-cache-configuration), the [default cache policy (`CacheFunctionBody()`)](#default-cache-policy--cachefunctionbody) generates the version.

* `serialize` (`bool`): Enables or disables [cache serialization](#cache-serialization).
When enabled, Union ensures that a single instance of the node is run before any other instances that would otherwise run concurrently.
This allows the initial instance to cache its result and lets the later instances reuse the resulting cached outputs.
If not set (for example, when using `cache=True`, [as shown below](#default-cache-configuration)) cache serialization is disabled.


* `ignored_inputs` (`Union[Tuple[str, ...], str]`): Input variables that should not be included when calculating the hash for the cache.
If not set, (for example, when simply using `cache=True`, [as shown below](#default-cache-configuration)) no inputs are ignored.

* `salt` (`str`): A salt used in the hash generation.

* `policies` (`Optional[Union[List[CachePolicy], CachePolicy]]`): A list of [CachePolicy]() objects.
If no `version` is specified and one or more polices are specified then these policies generate the version.
If no `version` is specified and no policies are specified then the [default cache policy (`CacheFunctionBody()`)](#default-cache-policy--cachefunctionbody) generates the version.
When using `cache=True`, [as shown below](#default-cache-configuration), the [default cache policy (`CacheFunctionBody()`)](#default-cache-policy--cachefunctionbody) generates the version.


### Example

```{code-block} python
:emphasize-lines: 4,19,27
import union


@union.task(cache=union.Cache(version="1.0", serialize=True, ignored_inputs=["a"]))
def sum(a: int, b: int, c: int) -> int:
    return a + b + c


@union.workflow
def child_wf(a: int, b: int, c: int) -> list[int]:
    return [
        sum(a=a, b=b, c=c)
        for _ in range(5)
    ]


child_lp = union.LaunchPlan.get_or_create(child_wf)


@union.workflow
def parent_wf_with_subwf(input: int = 0):
    return [
        child_wf(a=input, b=3, c=4).with_overrides(cache=union.Cache(version="1.0", serialize=True, ignored_inputs=["a"]))
        for i in [1, 2, 3]
    ]


@union.workflow
def parent_wf_with_sublp(input: int = 0):
     return [
        child_lp(a=input, b=1, c=2).with_overrides(cache=union.Cache(version="1.0", serialize=True, ignored_inputs=["a"]))
        for i in [1, 2, 3]
    ]
```

In the above example, caching is enabled at multiple levels:
    * At the task level, in the `@union.task` decorator of the task `sum`.
    * At the workflow level, in the `with_overrides` method of the invocation of the workflow `child_wf`.
    * At the launch plan level, in the `with_overrides` method of the invocation of the launch plan `child_lp`.

In each case, the result of the execution is cached and reused in subsequent executions.
Here the reuse is demonstrated by calling the `child_wf` and `child_lp` workflows multiple times with the same inputs.
Additionally, if the same node is invoked again with the same inputs (excluding input "a", as it is ignored for purposes of versioning)
the cached result is returned immediately instead of re-executing the process.
This applies even if the cached node is invoked externally through the UI or CLI.


## Default cache configuration

Instead of specifying a Cache object, a simpler way to enable caching is to set `cache=True` in the `@union.task` decorator (for tasks) or the `with_overrides` method (for subworkflows and sub-launch plans).
For example:

```{code-block} python
:emphasize-lines: 5,20,28
import union
from typing import List


@union.task(cache=True)
def sum(a: int, b: int, c: int) -> int:
    return a + b + c


@union.workflow
def child_wf(a: int, b: int, c: int) -> List[int]:
    return [
        sum(a=a, b=b, c=c)
        for _ in range(5)
    ]


child_lp = union.LaunchPlan.get_or_create(child_wf)


@union.workflow
def parent_wf_with_subwf(input: int = 0):
    return [
        child_wf(a=input, b=3, c=4).with_overrides(cache=True)
        for i in [1, 2, 3]
    ]


@union.workflow
def parent_wf_with_sublp(input: int = 0):
     return [
        child_lp(a=input, b=1, c=2).with_overrides(cache=True)
        for i in [1, 2, 3]
    ]
```

In this case caching is enabled with the following:
* `version` is generated by the [default cache policy `CacheFunctionBody()`](#default-cache-policy--cachefunctionbody).
* `serialize` is set to `False`.
* `ignored_inputs` is not set. No parameters are ignored.


## Default cache policy: : `CacheFunctionBody`

The `CacheFunctionBody` policy generates a version based on the function body of the task.
This means that if the function body changes, the cache is invalidated.


## The `overwrite-cache` flag

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
Union will know not to use older cached task executions and create a new cache entry on the subsequent execution.
When cache policies are specified (and no `version` is set), the policies generate the version.
When using `cache=True`, the [default cache policy (`CacheFunctionBody()`)](#default-cache-policy--cachefunctionbody) generates the version.
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
@union.task(cache=union.Cache(version="1.1"))
def t(n: int) -> int:
   return n * n + 1
```

Here the `version` parameter has been bumped from `1.0`to `1.1`, resulting in the removal of the cache entries for that task.
The next time the task is called it will be executed and the result re-cached under an updated key.

If used, the `version` parameter must be explicitly changed in order to invalidate the cache.
(if not used, then a cache policy may be used to generate the version).

Not every Git revision of a node will necessarily invalidate the cache.
A change in Git SHA does not necessarily correlate to a change in functionality.
You can refine the code without invalidating its outputs as long as you use and don't change the `version` parameter (or the signature, see below) of the node.

The idea behind this is to decouple syntactic sugar (for example, changed documentation or renamed variables) from changes to logic that can affect the process's result.
When you use Git (or any version control system), you have a new version per code change.
Since the behavior of most nodes in a Git repository will remain unchanged, you don't want their cached outputs to be lost.

When a node's behavior does change though, you can bump `version` to invalidate the cache entry and make the system recompute the outputs.

Alternatively, you can use the `policies` parameter to generate the version automatically.

The default cache policy is `CacheFunctionBody()`, for example, generates a version based on the function body of the task.


### Node signature

If you modify the signature of a node by adding, removing, or editing input parameters or output return types, Union invalidates the cache entries for that node.
During the next execution, Union executes the process again and caches the outputs as new values stored under an updated key.

{@@ if byoc @@}
### Caching when running locally

The description above applies to caching when executing a node remotely on your Union cluster.
Caching is also available [when running on a local cluster](../development-cycle/running-in-a-local-cluster.md).

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
To enable set `cache_serialize=True` in the `@union.task` decorator (this only has an effect if `cache=True` is also set)

The cache key definitions follow the same rules as non-serialized cache tasks.
It is important to understand the implications of the task signature and `cache_version` parameter in defining cached results.

```{code-block} python
@union.task(cache=union.Cache(cache_serialize=True))
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
@union.task
def foo(a: int, b: str) -> pandas.DataFrame:
    df = pandas.DataFrame(...)
    ...
    return df


@union.task(cache=True)
def bar(df: pandas.DataFrame) -> int:
    ...


@union.workflow
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


@union.task
def foo_1(a: int, b: str) -> Annotated[pandas.DataFrame, HashMethod(hash_pandas_dataframe)]:
    df = pandas.DataFrame(...)
    ...
    return df


@union.task(cache=True)
def bar_1(df: pandas.DataFrame) -> int:
    ...


@union.workflow
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


@union.task
def uncached_data_reading_task() -> Annotated[pandas.DataFrame, HashMethod(hash_pandas_dataframe)]:
    return pandas.DataFrame({"column_1": [1, 2, 3]})


@union.task(cache=True)
def cached_data_processing_task(df: pandas.DataFrame) -> pandas.DataFrame:
    time.sleep(1)
    return df * 2


@union.task
def compare_dataframes(df1: pandas.DataFrame, df2: pandas.DataFrame):
    assert df1.equals(df2)


@union.workflow
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
