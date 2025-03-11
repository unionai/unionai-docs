---
title: Details of union run
weight: 11
variants: "+flyte +serverless +byoc +byok"
---

# Details of union run

The `union run` command is used to run a specific workflow or task in your local Python environment or on Union.
In this section we will discuss some of the details of how and why to use it.

## Passing parameters

`union run` enables you to execute a specific workflow using the syntax:

```shell
$ union run <path/to/script.py> <workflow_or_task_function_name>
```

Keyword arguments can be supplied to `union run` by passing them in like this:

```shell
--<keyword> <value>
```

For example, above we invoked `union run` with script `example.py`, workflow `wf`, and named parameter `name`:

```shell
$ union run example.py wf --name 'Albert'
```

The value `Albert` is passed for the parameter `name`.

With `snake_case` argument names, you have to convert them to `kebab-case`. For example,
if the code were altered to accept a `last_name` parameter then the following command:

```shell
$ union run example.py wf --last-name 'Einstein'
```

would pass the value `Einstein` for that parameter.

## Why `union run` rather than `python`?

You could add a `main` guard at the end of the script like this:

```python
if __name__ == "__main__":
    training_workflow(hyperparameters={"C": 0.1})
```

This would let you run it with `python example.py`, though you have to hard code your arguments.

It would become even more verbose if you want to pass in your arguments:

```python
if __name__ == "__main__":
    import json
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--hyperparameters", type=json.loads)
    ...  # add the other options

    args = parser.parse_args()
    training_workflow(hyperparameters=args.hyperparameters)Py

```

`union run` lets you dispense with this verbosity and run the workflow with the desired arguments conveniently.