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
