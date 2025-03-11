---
title: MemVerge Memory Machine Cloud (MMC) agent example
weight: 1
variants: "+flyte +serverless +byoc +byok"
---

# MemVerge Memory Machine Cloud (MMC) agent example

This example shows how to use the MMCloud agent to execute tasks on MemVerge Memory Machine Cloud.

{{< code file="/assets/flytesnacks/examples/mmcloud_agent/mmcloud_agent/mmcloud_agent_example_usage.py"
         lang="python" from=8 to=9 >}}

`MMCloudConfig` configures `MMCloudTask`. Tasks specified with `MMCloudConfig` will be executed using MMCloud. Tasks will be executed with requests `cpu="1"` and `mem="1Gi"` by default.

{{< code file="/assets/flytesnacks/examples/mmcloud_agent/mmcloud_agent/mmcloud_agent_example_usage.py"
         lang="python" from="16" to="23" >}}

[Resource requests and limits](https://docs.flyte.org/en/latest/user_guide/productionizing/customizing_task_resources.html) (CPU and memory), [container images](https://docs.flyte.org/en/latest/user_guide/customizing_dependencies/multiple_images_in_a_workflow.html), and [environment variable](https://docs.flyte.org/en/latest/api/flytekit/generated/flytekit.task.html) specifications are supported.

{{< code file="/assets/flytesnacks/examples/mmcloud_agent/mmcloud_agent/mmcloud_agent_example_usage.py"
         lang="python" from=31 to=45 >}}
