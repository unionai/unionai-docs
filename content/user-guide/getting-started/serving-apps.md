---
title: Serving apps
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Serving apps

Flyte SDK lets you serve apps on your Union/Flyte instance, making them accessible via HTTP endpoints. Apps are long-running services that can be accessed by users or other services.

> [!TIP] Prerequisites
> Make sure to run the [local setup](./local-setup) before going through this guide.

First install fastapi in your virtual environment:

```shell
pip install fastapi
```

## Hello world example

Create a file called `hello_app.py` with the following content:

{{< code file="/external/unionai-examples/v2/user-guide/getting-started/serving/hello_app.py" lang="python" >}}

## Understanding the code

In the code above we do the following:

- Import the `flyte` package and `FastAPIAppEnvironment` from `flyte.app.extras`.
- Define a FastAPI application using the `FastAPI` class.
- Create an `AppEnvironment` using `FastAPIAppEnvironment`:
  - Apps are long-running services, unlike tasks which run to completion.
  - The `FastAPIAppEnvironment` automatically configures the app to run with uvicorn.
  - We specify the container image with required dependencies (FastAPI and uvicorn).
  - We set resource limits (CPU and memory).
  - We disable authentication for this example (`requires_auth=False`) so you can easily access the app with a `curl` command.

## Serving the app

Make sure that your `config.yaml` file is in the same directory as your `hello_app.py` script.

Now, serve the app with:

```shell
flyte serve hello_app.py env
```

You can also serve it via `python`:

```shell
python hello_app.py
```

This will use the code in the `if __name__ == "__main__":` block to serve the app
with the `flyte.serve()` function.

You can also serve the app using `python hello_app.py`, which
uses the main guard section in the script. It invokes `flyte.init_from_config()` to set up the connection with your Union/Flyte instance and `flyte.serve()` to deploy and serve your app on that instance.

> [!NOTE]
> The example scripts in this guide have a main guard that programmatically serves the apps defined in the same file.
> All you have to do is execute the script itself.
> You can also serve apps using the `flyte serve` CLI command. We will cover this in a later section.

## Viewing the results

In your terminal, you should see output like this:

```shell
https://my-instance.example.com/v2/apps/project/my-project/domain/development/hello-app
App 'hello-app' is now serving.
```

Click the link to go to your Union instance and see the app in the UI, where you can find
the app URL, or visit `/docs` for the interactive Swagger UI API documentation.

## Next steps

Now that you've served your first app, you can learn more about:

- [**Configuring apps**](../configure-apps/): Learn how to configure app environments, including images, resources, ports, and more
- [**Building apps**](../build-apps/): Explore different types of apps you can build (FastAPI, Streamlit, vLLM, SGLang)
- [**Serving and deploying apps**](../serve-and-deploy-apps/): Understand the difference between serving (development) and deploying (production) apps
