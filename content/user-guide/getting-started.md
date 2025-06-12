---
title: Getting started
weight: 2
variants: +flyte +serverless +byoc +selfmanaged
---

# Getting Started

This section gives you a quick introduction to writing and running workflows on Union.ai.


## Hello world

We'll start with a "Hello world" example.

Create a file called `hello.py` with the following content:

{{< code file="/external/migrate-to-unionai-examples-flyte2/getting_started.py" lang="python" >}}

This script defines three asynchronous functions: `say_hello`, `square`, and `hello_wf`.
The `say_hello_wf` is the top-level "workflow" function that orchestrates the execution of the other two functions.

Now let's say that some parts of the above program could benefit from running in a different environment,
for example on a GPU or with more memory.
Obviously, this is not really the case in this example, but let's pretend.

With Flyte, you can easily augment your code with a few decorators and auxiliary functions, and it is ready to be deployed to a Kubernetes cluster where each function runs in its own container with, potentially, its own dependencies and specific hardware.

In our example above, we can achieve this as follows:
* Import the flyte package,
* Create a `TaskEnvironment`.
* Decorate your functions with `@env.task`.
* Change your main guard initialize and run the workflow using the Flyte SDK.

## Configuration Setup

First, make sure you are in a Python virtual environment, then install the v2 SDK.
For example, you can use the [`uv` package manager](https://docs.astral.sh/uv/) to create a virtual environment and install the `flyte` package like this:

```shell
uv venv
source .venv/bin/activate
uv pip install --no-cache --prerelease=allow --upgrade flyte
```

Next, create a `config.yaml` file in the same directory as your `hello.py` file that points to your Union instance by running the following: 

```shell
flyte create config --endpoint dns:///<your-union-endpoint> --org <your-union-org> --project <default-project> --domain <default-domain> 
```

Note that the v2 configuration includes a default project (`<default-project>`) and domain (`<default-domain>`), as well as an `org` (`<your-union-org>`). 
Please reach out to Union support if you're unable to locate values for `<your-union-endpoint>` and `<your-union-org>`.

## Running Remotely

Now, simply run the script:

```shell
$ python hello.py
```

You should see something like this:

```shell
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1749121657.498681 3214165 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
I0000 00:00:1749121657.558185 3214165 fork_posix.cc:71] Other threads are currently calling into gRPC, skipping fork() handlers
Files to be copied for fast registration...
📂 /Users/myuser/repos/unionai/unionv2 (detected source root)
┗━━ examples
    ┗━━ basics
        ┗━━ hello_2.py
[flyte] Code bundle created at /var/folders/vn/72xlcb5d5jbbb3kk_q71sqww0000gn/T/tmpo18zj1vx/fast520a2f2d50cc981784e0180c3b32943d.tar.gz, size: 0.009765625 MB, archive size: 0.0005788803100585938 MB
t4m7ph57xchdw2dxx7bc
https://union.example.com/v2/runs/project/myproject/domain/development/t4m7ph57xchdw2dxx7bc

```

Click the link to go to your Union.ai instance and see the run in the UI:

![V2 UI](/_static/images/user-guide/v2ui.png)

