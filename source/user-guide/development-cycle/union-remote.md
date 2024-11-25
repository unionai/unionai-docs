# UnionRemote

The `UnionRemote` Python API supports functionality similar to that of the `union` CLI, enabling you to manage Union workflows, tasks, launch plans and artifacts from within your Python code.

:::{note}
The primary use case of `UnionRemote` is to automate the deployment of Union entities. As such, it is intended for use within scripts *external* to actual Union workflow and task code, for example CI/CD pipeline scripts.

In other words: _Do not use `UnionRemote` within task code._
:::

## Creating a `UnionRemote` object

Ensure that you have the `union` SDK installed, import the `UnionRemote` class and create the object like this:

```{code-block} python
from union.remote import UnionRemote

remote = UnionRemote()
```

By default, when created with a no-argument constructor, `UnionRemote` will use the prevailing configuration in the local environment to connect to Union, that is, the same configuration as would be used by the `union` CLI in that environment (see [Union CLI > `union` CLI configuration search path](../../api-reference/union-cli.md#union-cli-configuration-search-path)).

In the default case, as with the `union` CLI, all operations will be applied to the default project, `flytesnacks` and default domain, `development`.

{@@ if byoc @@}

Alternatively, you can initialize `UnionRemote` by explicitly specifying a `flytekit.configuration.Config` object with connection information to a Union instance, a project, and a domain. Additionally the constructor supports specifying a file upload location (equivalent to a default raw data prefix. See [TODO](TODO)):

```{code-block} python
from union.remote import UnionRemote
from flytekit.configuration import Config

remote = UnionRemote(
    config=Config.for_endpoint(endpoint="union.example.com"),
    default_project="my-project",
    default_domain="my-domain",
    data_upload_location="<s3|gs|abs>://my-bucket/my-prefix",
)
```

Here we use the `Config.for_endpoint` method to specify the URL to connect to.
There are number of other ways to configure the `Config` object.
In general, you have all the same options as you would when specifying a connection for the `union` CLI using a `config.yaml` file.
For details see [the API docs for `flytekit.configuration.Config`](TODO).

{@@ elif serverless @@}

Alternatively, you can initialize `UnionRemote` by explicitly specifying a project, and a domain:

```{code-block} python
from union.remote import UnionRemote
from flytekit.configuration import Config

remote = UnionRemote(
    default_project="my-project",
    default_domain="my-domain",
)
```

{@@ endif @@}

## Registering and running a workflow

The simplest way to register and run a workflow is to use `UnionRemote.fast_register_workflow` and `UnionRemote.execute`

Here is  an example project structure:

```{code-block} bash
:caption: A simple project

├── remote.py
└── workflow
    ├── __init__.py
    └── example.py
```

The workflow code resides in the `workflow` directory and consists of an empty `__init__.py` file and the workflow and task code in `example.py`:

```{code-block} python
:caption: example.py
import os
from flytekit import task, workflow
from flytekit.types.file import FlyteFile


@task()
def create_file(message: str) -> FlyteFile:
    with open("data.txt", "w") as f:
        f.write(message)
    return FlyteFile(path="data.txt")

@workflow
def my_workflow(message: str) -> FlyteFile:
    f = create_file(message)
    return f
```

The file `remote.py` contains the UnionRemote logic (and is not part of the workflow code):

```{code-block} python
:caption: remote.py
from union.remote import UnionRemote
from flytekit.tools.translator import Options
from workflow.example import my_workflow


def run_workflow():
    remote = UnionRemote()
    remote.fast_register_workflow(entity=my_workflow)
    execution = remote.execute(
        entity=my_workflow,
        inputs={"message": "Hello, world!"},
        wait=True)
    output = execution.outputs["o0"]
    print(output)
    with open(output, "r") as f:
        read_lines = f.readlines()
    print(read_lines)


if __name__ == "__main__":
    run_workflow()
```

Note a few things about the code above:
* Since no project or domain are specified when creating the `UnionRemote` object the default project (`flytesnacks`) and the default domain (`development`)
  will be used.
* Since no container image is specified in the `@task` declaration, the default container image will be used.
* The method `UnionRemote.fast_register_workflow` take the actual workflow function (the Python object) as input.
* The registration logic then registers that workflow and all tasks referenced by it (you don't have to individually register each task)
* If you the results of an execution you have to retrieve the execution and then wait for it to complete.
  The method `UnionRemote.execute` provides the `wait` flag for this purpose. When `wait=True` `execute` will block until the execution is completed and then return.


You can run the code with:

```{code-block} bash
$ python remote.py
```

`UnionRemote` provides a variety methods for registering and running workflows.
For details see [API reference > UnionRemote > Entrypoint](../../api-reference/union-remote/entrypoint.md)



## Executing tasks, workflows, and launch plans

You can execute a task, workflow, or launch plan using the `execute` method
which returns a `FlyteWorkflowExecution` object:

```{code-block} python
some_entity = ...  # one of FlyteTask, FlyteWorkflow, or FlyteLaunchPlan
execution = remote.execute(
    some_entity,
    inputs={...},
    execution_name="my_execution",
    wait=True,
)
```

* `inputs`: the inputs to the entity.
* `execution_name`: the name of the execution. This is useful to avoid de-duplication of executions.
* `wait`: synchronously wait for the execution to complete.

Additional arguments include:

* `project`: the project on which to execute the entity.
* `domain`: the domain on which to execute the entity.
* `type_hints`: a dictionary mapping Python types to their corresponding Flyte types.
* `options`: options can be configured for a launch plan during registration or overridden during execution. Refer to `Options` to know all the acceptable parameters.

The following is an example demonstrating how to use the `Options` class to configure a Flyte entity:

```{code-block} python
from flytekit.models.common import AuthRole, Labels
from flytekit.tools.translator import Options

some_entity = ...  # one of FlyteTask, FlyteWorkflow, or FlyteLaunchPlan
execution = remote.execute(
    some_entity,
    inputs={...},
    execution_name="my_execution",
    wait=True,
    options=Options(
        raw_data_prefix="s3://my-bucket/my-prefix",
        auth_role=AuthRole(assumable_iam_role="my-role"),
        labels=Labels({"my-label": "my-value"}),
    ),
)
```

## Retrieving and inspecting executions

After an execution is completed, you can retrieve the execution using the `fetch_execution` method.
The fetched execution can be used to retrieve the inputs and outputs of an execution:

```{code-block} python
execution = remote.fetch_execution(
    name="fb22e306a0d91e1c6000",
    project="flytesnacks",
    domain="development",
)
input_keys = execution.inputs.keys()
output_keys = execution.outputs.keys()
```

##

The `inputs` and `outputs` correspond to the top-level execution or the workflow itself.

To fetch a specific output, say, a model file:

```{code-block} python
model_file = execution.outputs["model_file"]
with open(model_file) as f:
    # use mode
    ...
```

## Syncing state

You can use `sync` to sync the entity object's state with the remote state during the execution run:

```{code-block} python
synced_execution = remote.sync(execution, sync_nodes=True)
node_keys = synced_execution.node_executions.keys()
```

`node_executions` will fetch all the underlying node executions recursively.

To fetch output of a specific node execution:

```{code-block} python
node_execution_output = synced_execution.node_executions["n1"].outputs["model_file"]
```

Node here can correspond to a task, workflow, or branch node.

## Terminating an execution

To terminate an execution, use the `terminate` method:

```{code-block} python
execution = remote.fetch_execution(
    name="fb22e306a0d91e1c6000",
    project="flytesnacks",
    domain="development",
)
remote.terminate(execution, cause="Code needs to be updated")
```



















## Fetching tasks, workflows, launch plans, and executions

```{code-block} python
my_task = remote.fetch_task(name="my_task", version="v1")
my_workflow = remote.fetch_workflow(name="my_workflow", version="v1")
my_launch_plan = remote.fetch_launch_plan(name="my_launch_plan", version="v1")
my_execution = remote.fetch_execution(name="my_execution")
```

`project` and `domain` can also be specified in all the `fetch_*` calls.
If not specified, the default values given during the creation of the `UnionRemote`
object will be used.

The following is an example that fetches tasks and creates a workflow:

```{code-block} python
from flytekit import workflow

task_1 = remote.fetch_task(name="core.basic.hello_world.say_hello", version="v1")
task_2 = remote.fetch_task(
    name="core.basic.lp.greet",
    version="v13",
    project="flytesnacks",
    domain="development",
)

@workflow
def my_remote_wf(name: str) -> int:
    return task_2(task_1(name=name))
```

Another example that dynamically creates a launch plan for the `my_remote_wf` workflow:

```{code-block} python
from flytekit import LaunchPlan

my_workflow = remote.fetch_workflow(
    name="my_workflow",
    version="v1",
    project="flytesnacks",
    domain="development",
)
launch_plan = LaunchPlan.get_or_create(name="my_launch_plan", workflow=my_workflow)
```

## Fetching artifacts

Each artifact version has a unique URI of the form `flyte://<organization>/<project>/<domain>/<artifact_name>@<artifact_version>`.

To fetch a single artifact, pass this URI to the `get_artifact` method:

{@@ if byoc @@}

```{code-block} python
from flytekit.configuration import Config, PlatformConfig, AuthType
from union.remote import UnionRemote

remote = UnionRemote(
    Config.auto().with_params(
        platform=PlatformConfig(
            endpoint="example.domain.unionai.cloud",
            insecure=False,
        )
    )
)

remote.get_artifact("flyte://<organization>/<project>/<domain>/<artifact_name>@<artifact_version>")
```

{@@ elif serverless @@}

```{code-block} python
from union.remote import UnionRemote

remote = UnionRemote()

remote.get_artifact("flyte://<organization>/<project>/<domain>/<artifact_name>@<artifact_version>")
```

{@@ endif @@}

To dynamically query for artifacts, you can pass an artifact URI with a query to the `get_artifact` method, adding as many partition key-value pairs as you wish to filter on. The query will retrieve the latest artifact version that matches the partition-based filters:

{@@ if byoc @@}

```{code-block} python
from flytekit.configuration import Config, PlatformConfig, AuthType
from union.remote import UnionRemote

remote = UnionRemote(
    Config.auto().with_params(
        platform=PlatformConfig(
            endpoint="example.domain.unionai.cloud",
            insecure=False,
        )
    )
)

remote.get_artifact("flyte://<organization>/<project>/<domain>/<artifact_name>?<partition_key1>=<partition_value1>&...")
```

{@@ elif serverless @@}

```{code-block} python
from union.remote import UnionRemote

remote = UnionRemote()

remote.get_artifact("flyte://<organization>/<project>/<domain>/<artifact_name>?<partition_key1>=<partition_value1>&...")
```

{@@ endif @@}

## Creating artifacts

To create an artifact with `UnionRemote`, declare the artifact, then pass it to the `create_artifact` method:

{@@ if byoc @@}

```{code-block} python
from flytekit.configuration import Config, PlatformConfig, AuthType
from union.remote import UnionRemote
from flytekit.core.artifact import Artifact

remote = UnionRemote(
    Config.auto().with_params(
        platform=PlatformConfig(
            endpoint="example.domain.unionai.cloud",
            insecure=False,
        )
    )
)

BasicArtifact = Artifact(name="my_basic_artifact")
remote.create_artifact(BasicArtifact)
```

{@@ elif serverless @@}

```{code-block} python
from union.remote import UnionRemote
from flytekit.core.artifact import Artifact

remote = UnionRemote()

BasicArtifact = Artifact(name="my_basic_artifact")
remote.create_artifact(BasicArtifact)
```

{@@ endif @@}

For the full list of parameters, see the [Artifact class documentation](../../api-reference/flytekit-sdk/core-flytekit/artifacts).

:::{note}
If you want to create a new version of an existing artifact, be sure to set the `version` parameter. Without it, attempting to recreate the same artifact will result in an error.
:::














## Reference launch plan executions

When retrieving and inspecting an execution which calls a launch plan, the launch plan manifests as a sub-workflow which can be found within the `workflow_executions` of a given node execution.
Note that the workflow execution of interest must again be synced in order to inspect the input and output of the contained tasks.

```{code-block} python
@task
def add_random(x: int) -> int:
    return x + random.randint(1, 100)

@workflow
def sub_wf(x: int) -> int:
    x = add_random(x=x)
    return add_random(x=x)

sub_wf_lp = LaunchPlan.get_or_create(
    name="sub_wf_lp",
    workflow=sub_wf,
)

@workflow
def parent_wf(x: int = 1) -> int:
    x = add_random(x=x)
    return sub_wf_lp(x=x)
```

To get the output of the first `add_random` call in `sub_wf`, you can do the following with the `execution` from the `parent_wf`:

```{code-block} python
execution = remote.fetch_execution(
    name="adgswtrzfn99k2cws49q",
    project="flytesnacks",
    domain="development",
)
remote.sync_execution(execution, sync_nodes=True)
remote.sync_execution(execution.node_executions['n1'].workflow_executions[0], sync_nodes=True)
out = execution.node_executions['n1'].workflow_executions[0].node_executions['n0'].outputs['o0']
```

## Listing entities

To list recent executions, use the `recent_executions` method:

```{code-block} python
recent_executions = remote.recent_executions(
    project="flytesnacks",
    domain="development",
    limit=10,
)
```

The `limit` parameter is optional and defaults to 100.

To list tasks by version, use the `UnionRemote.list_tasks_by_version` method.

```{code-block} python
tasks = remote.list_tasks_by_version(
    project="flytesnacks",
    domain="development",
    version="v1",
)
```


