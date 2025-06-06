---
title: Flyte CLI
weight: 10
variants: +flyte +serverless +byoc +selfmanaged
---

# Flyte CLI

So far, we have executed our example scripts directly in Python. We enabled this by adding a main guard to each script that called the appropriate Flyte command to deploy the code.

Deploying and executing code programmatically as we have been doing is a powerful feature, but there are cases where you want to deploy and run workflows from the command line.
[The Flyte CLI](../api-reference/flyte-cli) provides a convenient way to do this.

## API CLI equivalence

The [Flyte SDK API](../api-reference/flyte-sdk) provides all the functionality of the Flyte CLI.
Every command in the CLI has a corresponding function in the SDK.

## Example

In our example [`hello.py` example](./getting-started) we used a main guard that looked like this:

```python
if __name__ == "__main__":
    flyte.init_auto_from_config("./config.yaml")
    run = flyte.run(hello_wf, data="hello world")
    print(run.name)
    print(run.url)
    run.wait(run)
```

The equivalent `flyte CLI` command is:

```shell
$ flyte --config ./config.yaml run hello.py hello_wf --data "hello world"
```
