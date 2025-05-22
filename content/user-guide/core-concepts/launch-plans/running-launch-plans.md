---
title: Running launch plans
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Running launch plans

## Running a launch plan in the UI


To invoke a launch plan, go to the **Workflows** list, select the desired workflow, click **Launch Workflow**. In the new execution dialog, select the desired launch plan from from the **Launch Plan** dropdown menu and click **Launch**.

## Running a launch plan on the command line with `uctl`

To invoke a launch plan via the command line, first generate the execution spec file for the launch plan:

```shell
$ uctl get launchplan \
       --project <project-id>
       --domain <domain> \
       <launch-plan-name> \
       --execFile <execution-spec-file-name>.yaml
```

Then you can execute the launch plan with the following command:

```shell
$ uctl create execution \
       --project <project-id> \
       --domain <domain> \
       --execFile <execution-spec-file-name>.yaml
```

See [Uctl CLI](../../../api-reference/uctl-cli) for more details.

<!-- TODO: adjust Remote code for serverless vs everything else -->
## Running a launch plan in Python with `{{< key kit_remote >}}`

The following code executes a launch plan using `{{< key kit_remote >}}`:

```python
import {{< key kit_import >}}
from flytekit.remote import Config

remote = {{< key kit_as >}}.{{< key kit_remote >}}(config=Config.auto(), default_project=<project-id>, default_domain=<domain>)
launch_plan = remote.fetch_launch_plan(name=<launch-plan-name>, version=<launch-plan-version>)
remote.execute(launch_plan, inputs=<inputs>)
```

See the [{{< key kit_remote >}}](../../development-cycle/union-remote) for more details.

## Sub-launch plans

The above invocation examples assume you want to run your launch plan as a top-level entity within your project.
However, you can also invoke a launch plan from *within a workflow*, creating a *sub-launch plan*.
This causes the invoked launch plan to kick off its workflow, passing any parameters specified to that workflow.

This differs from the case of [subworkflows](../workflows/subworkflows-and-sub-launch-plans) where you invoke one workflow function from within another.
A subworkflow becomes part of the execution graph of the parent workflow and shares the same execution ID and context.
On the other hand, when a sub-launch plan is invoked a full, top-level workflow is kicked off with its own execution ID and context.

See [Subworkflows and sub-launch plans](../workflows/subworkflows-and-sub-launch-plans) for more details.
