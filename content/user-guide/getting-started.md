---
title: Getting started
weight: 10
variants: +flyte +serverless +byoc +selfmanaged
---

# Getting started

This section gives you a quick introduction to writing and running workflows on Union and Flyte v2.

## Configuration setup

First, make sure you are in a Python virtual environment, then install the v2 SDK.
For example, you can use the [`uv` package manager](https://docs.astral.sh/uv/) to create a virtual environment and install the `flyte` package like this:

```shell
uv venv
source .venv/bin/activate
uv pip install --no-cache --prerelease=allow --upgrade flyte
```

Next, create a `config.yaml` file in the same directory as your `hello.py` file that points to your Union instance using the [flyte create config](../api-reference/flyte-cli#flyte-create-config) command:

```shell
flyte create config \
    --endpoint dns:///<your-union-endpoint> \
    --org <your-union-org> \
    --project <default-project> \
    --domain <default-domain>
```

For example, your config file might look like:

```shell
flyte create config \
    --endpoint dns:///demo.hosted.unionai.cloud \
    --org demo \
    --project flytesnacks \
    --domain development
```

Note that the v2 configuration includes a default project (`<default-project>`) and domain (`<default-domain>`), as well as an `org` (`<your-union-org>`).

The default project and domain will be used when you deploy your workflows without specifying a project or domain explicitly.

Please reach out to Union support if you're unable to locate values for `<your-union-endpoint>` and `<your-union-org>`.


## Hello world

We'll start with a "Hello world" example.

Create a file called `hello.py` with the following content:

{{< code file="/external/migrate-to-unionai-examples-flyte2/getting_started.py" lang="python" >}}

This script defines three asynchronous functions: `say_hello`, `square`, and `hello_wf`.
The `hello_wf` is the top-level "workflow" function that orchestrates the execution of the other two functions.

We have instrumented this code to run remotely in a Flyte or Union instance:
* Import the `flyte` package,
* Create a `TaskEnvironment`.
* Decorate functions with `@env.task`.
* Add logic below the main guard to initialize and run the workflow using the Flyte SDK.

## Running remotely

Now, simply run the script:

```shell
python hello.py
```

You can also run using the CLI:

```shell
flyte run hello.py hello_wf --data "hello world"
```

You should see an output like this:

```shell
(unionv2) johnvotta@JV---Work unionv2 % python hello.py                         
Files to be copied for fast registration...
📂 /Users/johnvotta/code/unionv2 (detected source root)
┗━━ hello.py
[flyte] Code bundle created at /var/folders/1b/j0rhj5ms7hg20_jml81gscsh0000gn/T/tmpighost5t/fast1891d8b2749d0bb45bbe938d8221fef6.tar.gz, size: 0.009765625 MB, archive size: 0.0005626678466796875 MB
62ml7tgbdcb6llmbbb8l
https://demo.hosted.unionai.cloud/v2/runs/project/flytesnacks/domain/development/62ml7tgbdcb6llmbbb8l
Run 'a0' completed successfully.
```

Click the link to go to your Union instance and see the run in the UI:

![V2 UI](/_static/images/user-guide/v2ui.png)

