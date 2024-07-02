# Running in a local Python environment

To quickly try out the code, you can run it in your local Python environment using `unionai run`:

```{code-block} shell
$ unionai run workflows/example.py wf --name 'Albert'
```

Here you are invoking `unionai run` and passing the name of the Python file and the name of the workflow within that file that you want to run.
In addition, you are passing the named parameter `name` and its value.

You should see the following output:

```{code-block} shell
Hello, Albert!
```

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

```{code-block} shell
$ unionai run example.py wf --last-name 'Einstein'
```

would pass the value `Einstein` for the parameter `last_name`.

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
