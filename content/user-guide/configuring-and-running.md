---
title: Configuring and running
weight: 30
variants: +flyte +serverless +byoc +selfmanaged
---

# Configuring and running

You can run workflows in Union.ai in two main ways: programmatically from Python code or via the command line using the Flyte CLI.
In either case you can specify the required configuration either via a configuration file or by passing parameters when invoking the execution.

## Setting up a configuration file

As we saw in [Getting started](./getting-started) you can create a configuration file using the command [`flyte create config`](../api-reference/flyte-cli#flyte-create-config):

```shell
flyte create config \
    --endpoint dns:///<your-union-endpoint> \
    --org <your-union-org> \
    --project <default-project> \
    --domain <default-domain> \
    --output <path-to-config-file>
    --force
```

The `--output` flag specifies the path to the configuration file that will be created.
If not specified, the configuration file will be created in the current directory with the name `config.yaml`.

The `--force` flag is used to overwrite the existing configuration file if it already exists.

## Programmatic execution

Programmatic execution means running workflows directly from Python code executing on your local machine.

### `init_from_config`

You can use the [`flyte.init_from_config`](../api-reference/flyte-sdk/packages/flyte#init_from_config) function to initialize the Flyte SDK with the configuration file you created earlier.
This is the way we do it in the examples in this guide.

For example, in [Getting started](./getting-started) we run our workflow using this main guard in the same file as the workflow definition:


```python
if __name__ == "__main__":
    flyte.init_from_config("config.yaml")
    run = flyte.run(hello_wf, data="hello world")
    print(run.name)
    print(run.url)
    run.wait(run)
```

This requires that you have a `config.yaml` file in the same directory as the script.

To run the workflow on Union, you simply execute the workflow definition file in Python, like this:

```shell
$ python hello.py
```

You can also execute via the CLI like so:

```shell
flyte run hello.py hello_wf --data "hello world"
```

### `init`

You can also initialize the Flyte SDK using the [`flyte.init`](../api-reference/flyte-sdk/packages/flyte#init) function, which allows you to specify the backend endpoint and other parameters directly in your code.
If we wanted to replace the above `init_from_config` with `init`, it would look like this:

```python
if __name__ == "__main__":
    flyte.init(
        endpoint="dns:///<your-union-url>",
        org="<your-union-org>",
        project="<default-project>",
        domain="<default-domain>",
    )
    run = flyte.run(hello_wf, data="hello world")
    print(run.name)
    print(run.url)
    run.wait(run)
```

## CLI execution

You can also run workflows using the Flyte CLI.

### `flyte run` with a configuration file

For example, you can run the same workflow we defined in [Getting started](./getting-started) using the following command:

```shell
flyte --config config.yaml run hello.py hello_wf --data "hello world"
```
This command will execute the `hello_wf` workflow with the specified inputs and using the configuration file you created earlier.


### `flyte run` with command line parameters

You can also pass the configuration parameters directly in the command line, like this:

```shell
flyte \
    --endpoint dns:///<your-union-endpoint> \
    --org <your-union-org> \
    run \
    --project <project> \
    --domain <domain> \
    hello.py hello_wf --data "hello world" 
```

This will run the workflow without requiring a configuration file, but you will have to specify all the parameters every time you run the command.

## API/CLI equivalence

The [Flyte SDK API](../api-reference/flyte-sdk) provides all the functionality of the Flyte CLI.
Every command in the CLI has a corresponding function in the SDK.
