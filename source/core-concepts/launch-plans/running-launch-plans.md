# Running launch plans

## Running a launch plan in the UI

In the [Launch Plans section](./index), we defined `my_workflow_custom_lp` with fixed input `a=3` and default inputs `b=4` and `c=5`:

![my_workflow_custom_lp](/_static/images/concepts-launch-plans-4.png)

To invoke the launch plan, go to the **Workflows** view, select `workflows.launch_plan_example.my_workflow`, click **Launch Workflow**, then select `my_workflow_custom_lp` from the **Launch Plan** dropdown menu:

![my_workflow_custom_lp](/_static/images/concepts-launch-plans-5.png)

You will see that the two default inputs are available to be overridden, but the fixed input is not:

![my_workflow_custom_lp](/_static/images/concepts-launch-plans-6.png)

Click **Launch** to execute the launch plan.

## Running a launch plan on the command line with `uctl`

To invoke a launch plan via the command line, first generate the execution spec file for the launch plan:

```{code-block} shell
$ uctl get launchplan \
       --project <project-id>
       --domain <domain> \
       <launch-plan-name> \
       --execFile <execution-spec-file-name>.yaml
```

Then you can execute the launch plan with the following command:

```{code-block} shell
$ uctl create execution \
       --project <project-id> \
       --domain <domain> \
       --execFile <execution-spec-file-name>.yaml
```

<!-- TODO add back when uctl reference exists
See the [`uctl` reference]() for more details.
-->

## Running a launch plan in Python with `UnionRemote`

The following code executes a launch plan using `UnionRemote`:

```{code-block} python
from union.remote import UnionRemote
from flytekit.remote import Config

remote = UnionRemote(config=Config.auto(), default_project=<project-id>, default_domain=<domain>)
launch_plan = remote.fetch_launch_plan(name=<launch-plan-name>, version=<launch-plan-version>)
remote.execute(launch_plan, inputs=<inputs>)
```

See the [UnionRemote](../../development-cycle/unionremote) and [UnionRemote.execute](../../development-cycle/unionremote.md#executing-entities) documentation for more details.

## Sub-launch plans

The above invocation examples assume you want to run your launch plan as a top-level entity within your project.
However, you can also invoke a launch plan from *within a workflow*, creating an *sub-launch plan*.
This causes the invoked launch plan to kick off its workflow, passing any parameters specified to that workflow.

This differs from the case of [subworkflows](../workflows/subworkflows-and-sub-launch-plans) where you invoke one workflow function from within another.
A subworkflow becomes part of the execution graph of the parent workflow and shares the same execution ID and context.
On the other hand, when a sub-launch plan is invoked a full, top-level workflow is kicked off with its own execution ID and context.

See [Subworkflows and sub-launch plans](../workflows/subworkflows-and-sub-launch-plans) for more details.
