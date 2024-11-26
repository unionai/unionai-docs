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

## A simple example

In the following example we register and run a workflow and retrieve its output:

```{code-block} bash
:caption: A simple project

├── remote.py
└── workflow
    ├── __init__.py
    └── example.py
```

The workflow code that will be registered and run on Union resides in the `workflow` directory and consists of an empty `__init__.py` file and the workflow and task code in `example.py`:

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

The file `remote.py` contains the `UnionRemote` logic. It is not part of the workflow code, and is meant to be run on your local machine.

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

You can run the code with:

```{code-block} bash
$ python remote.py
```

The `my_workflow` workflow and the `create_file` task is registered and run.
Once the the workflow completes, the output is passed back to the `run_workflow` function and printed out.

The output is also be available via the UI, in the **Outputs** tab of the `create_file` task details view.

The steps above demonstrates the most straightforward way of registering and running a workflow with `UnionRemote`.
For more options and details see [API reference > UnionRemote > Entrypoint](../../api-reference/union-remote/entrypoint.md).
