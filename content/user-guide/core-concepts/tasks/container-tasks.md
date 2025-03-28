---
title: Container Tasks
weight: 5
variants: +flyte +serverless +byoc +byok
---

This example demonstrates how to use arbitrary containers in 5 different languages, all orchestrated in {{< key kit >}} seamlessly. {{< key product_name >}} mounts an input data volume where all the data needed by the container is available, and an output data volume for the container to write all the data which will be stored away.

The data is written as separate files, one per input variable. The format of the file is serialized strings. Refer to the raw protocol to understand how to leverage this.

> [!NOTE]
> To clone and run the example code on this page, see the [Flytesnacks repo][flytesnacks].

<!-- TODO: copy in this code
```{literalinclude} /examples/customizing_dependencies/customizing_dependencies/raw_container.py
:caption: customizing_dependencies/raw_container.py
:lines: 1-6
```
-->


## Container tasks

A `{{< key kit >}}.ContainerTask` denotes an arbitrary container. In the following example, the name of the task is `calculate_ellipse_area_shell`. This name has to be unique in the entire project. Users can specify:

* `input_data_dir` -> where inputs will be written to.
* `output_data_dir` -> where {{< key product_name >}} will expect the outputs to exist.

`inputs` and `outputs` specify the interface for the task; thus it should be an ordered dictionary of typed input and
output variables.

The `image` field specifies the container image for the task, either as an image name or
an [ImageSpec](/user-guide/core-concepts/tasks/task-software-environment/image-spec#imagespec).
To access the file that is not included in the image, use `ImageSpec` to copy files or
directories into container `/root`.

[Cache](/user_guide/development_lifecycle/caching.html) can be enabled in a `ContainerTask` by configuring the cache settings in the `TaskMetadata` in the `metadata` parameter.

<!-- TODO: copy in this code
```{literalinclude} /examples/customizing_dependencies/customizing_dependencies/raw_container.py
:caption: customizing_dependencies/raw_container.py
:lines: 16-118
```
-->

As can be seen in this example, `ContainerTask`s can be interacted with like normal Python functions, whose inputs
correspond to the declared input variables. All data returned by the tasks are consumed and logged by a {{< key product_name >}} task.

<!-- TODO: copy in this code
```{literalinclude} /examples/customizing_dependencies/customizing_dependencies/raw_container.py
:caption: customizing_dependencies/raw_container.py
:pyobject: wf
```
-->

One of the benefits of raw container tasks is that {{< key kit >}} does not need to be installed in the target container.

> [!NOTE]
> Raw containers can be run locally when {{< key kit >}} version >= 1.11.0.


### User Errors

Raw containers handle errors by checking for the presence of an `_ERROR` file in the `output_data_dir` after the container's execution. If this file exists, {{< key product_name >}} treats it as a user-defined error and retries the task if `retries` parameter is set in the task metadata.

## Scripts

The contents of each script specified in the `ContainerTask` is as follows:

### calculate-ellipse-area.sh

<!-- TODO: copy in this code
```{literalinclude} raw-containers-supporting-files/per-language/shell/calculate-ellipse-area.sh
:language: shell
```
-->

### calculate-ellipse-area.py

<!-- TODO: copy in this code
```{literalinclude} raw-containers-supporting-files/per-language/python/calculate-ellipse-area.py
:language: python
```
-->

### calculate-ellipse-area.R

<!-- TODO: copy in this code
```{literalinclude} raw-containers-supporting-files/per-language/r/calculate-ellipse-area.R
:language: r
```
-->

### calculate-ellipse-area.hs

<!-- TODO: copy in this code
```{literalinclude} raw-containers-supporting-files/per-language/haskell/calculate-ellipse-area.hs
:language: haskell
```
-->

### calculate-ellipse-area.jl

<!-- TODO: copy in this code
```{literalinclude} raw-containers-supporting-files/per-language/julia/calculate-ellipse-area.jl
:language: julia
```

[flytesnacks]: https://github.com/flyteorg/flytesnacks/tree/master/examples/customizing_dependencies/
-->