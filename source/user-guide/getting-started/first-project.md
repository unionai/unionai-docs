# First project

In this section we will set up a Union project on your local machine.

## Initialize a new project

To create a new project, run the following command:

```{code-block} shell
$ union init --template first-project first-project
```

This will create a directory called `first-project` with the following structure:

```{code-block} shell
first-project
├── LICENSE
├── README.md
├── uv.lock
├── pyproject.toml
├── docs
│   └── docs.md
└── src
    ├── core
    │   ├── __init__.py
    │   └── core.py
    ├── orchestration
    │   ├── __init__.py
    │   └── orchestration.py
    ├── tasks
    │   ├── __init__.py
    │   └── tasks.py
    └── workflows
        ├── __init__.py
        └── workflows.py
```

## Understand the project structure


To create an example workflow file, copy the following into a file called `hello.py`:

```{code-block} python
from flytekit import task, workflow

@task
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@workflow
def hello_world_wf(name: str = 'world') -> str:
    res = say_hello(name=name)
    return res
```

## Tasks and workflows

The "Hello, world!" code contains a task and a workflow, which are Python functions decorated with the `@task` and `@workflow` decorators, respectively.
For more information, see the [tasks](./user-guide/core-concepts/tasks/index.md) and [workflows](./user-guide/core-concepts/workflows/index.md) documentation.
