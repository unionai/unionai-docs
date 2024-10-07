# MemVerge Memory Machine Cloud (MMC) agent example

This example shows how to use the MMCloud agent to execute tasks on MemVerge Memory Machine Cloud.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/mmcloud_agent/mmcloud_agent/mmcloud_agent_example_usage.py
:language: python
:lines: 8-9
```

`MMCloudConfig` configures `MMCloudTask`. Tasks specified with `MMCloudConfig` will be executed using MMCloud. Tasks will be executed with requests `cpu="1"` and `mem="1Gi"` by default.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/mmcloud_agent/mmcloud_agent/mmcloud_agent_example_usage.py
:language: python
:lines: 16-23
```

[Resource requests and limits](https://docs.flyte.org/en/latest/user_guide/productionizing/customizing_task_resources.html) (CPU and memory), [container images](https://docs.flyte.org/en/latest/user_guide/customizing_dependencies/multiple_images_in_a_workflow.html), and [environment variable](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.task.html) specifications are supported.

```{rli} https://raw.githubusercontent.com/flyteorg/flytesnacks/master/examples/mmcloud_agent/mmcloud_agent/mmcloud_agent_example_usage.py
:language: python
:lines: 31-45
```
