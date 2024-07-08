# `unionai run` details

The `unionai run` command is used to run a specific workflow or task in your local Python environment or on Union.
In this section we will discuss some of the details of how and why to use it.

## Passing parameters

`unionai run` enables you to execute a specific workflow using the syntax:

```{code-block} shell
$ unionai run <path/to/script.py> <workflow_or_task_function_name>
```

Keyword arguments can be supplied to `unionai run` by passing them in like this:

```{code-block} shell
--<keyword> <value>
```

For example, above we invoked `unionai run` with script `example.py`, workflow `wf`, and named parameter `name`:

```{code-block} shell
$ unionai run example.py wf --name 'Albert'
```

The value `Albert` is passed for the parameter `name`.

With `snake_case` argument names, you have to convert them to `kebab-case`. For example,
if the code were altered to accept a `last_name` parameter then the following command:

```{code-block} shell
$ unionai run example.py wf --last-name 'Einstein'
```

would pass the value `Einstein` for that parameter.

## Why `unionai run` rather than `python`?

You could add a `main` guard at the end of the script like this:

```{code-block} python
if __name__ == "__main__":
    training_workflow(hyperparameters={"C": 0.1})
```

This would let you run it with `python example.py`, though you have to hard code your arguments.

It would become even more verbose if you want to pass in your arguments:

```{code-block} python
if __name__ == "__main__":
    import json
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--hyperparameters", type=json.loads)
    ...  # add the other options

    args = parser.parse_args()
    training_workflow(hyperparameters=args.hyperparameters)Py

```

`unionai run` lets you dispense with this verbosity and run the workflow with the desired arguments conveniently.