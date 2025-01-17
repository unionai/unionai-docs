# Running locally

You can run the workflow in your local Python environment with the [`union run` command](./api-reference/union-cli.md#union-cli-commands):

```{code-block} shell
$ union run hello.py hello_world_wf
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, world!
```

Since the `@workflow` function takes an argument called `name`, you can also pass that in
as a command-line argument like this:

```{code-block} shell
$ union run hello.py hello_world_wf --name Ada
```

You should see the following output:

```{code-block} shell
Running Execution on local.
Hello, Ada!
```

## Run the workflow locally in Python

To quickly check your workflow code, you can run it in your local Python environment with the following command:

```{code-block} shell
$ union run user_guide/first_workflow/ml_workflow/ml_workflow.py main --max_bins 64
```

If the code runs successfully, you should see output like this:

```{code-block} shell
Running Execution on local.
0.9767441860465116
```


