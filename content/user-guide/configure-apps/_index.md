---
title: Configure apps
weight: 13
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Configure apps

`[[AppEnvironment]]`s allows you to configure the environment in which your app runs, including the container image, compute resources, secrets, domains, scaling behavior, and more.

Similar to `[[TaskEnvironment]]`, configuration can be set when creating the `[[AppEnvironment]]` object. Unlike tasks, apps are long-running services, so they have additional configuration options specific to web services:

- `port`: What port the app listens on
- `command` and `args`: How to start the app
- `scaling`: Autoscaling configuration for handling variable load
- `domain`: Custom domains and subdomains for your app
- `requires_auth`: Whether the app requires authentication to access
- `depends_on`: Other app or task environments that the app depends on

## Hello World example

Here's a complete example of deploying a simple Streamlit "hello world" app with a custom subdomain.

There are two ways to build apps in Flyte:
1. Defining `AppEnvironment(.., args=[...])` to run the app with the underlying `fserve` command.
2. Defining `@app_env.server` to run the app with a custom server function.

{{< tabs "hello-world-app" >}}
{{< tab "Using fserve args" >}}

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/hello-world-app.py" lang=python >}}

{{< markdown >}}
This example demonstrates:

- Creating a custom Docker image with Streamlit
- Setting the `args` to run the Streamlit hello app, which uses the underlying `fserve` command to run the app.
- Configuring the port
- Setting resource limits
- Disabling authentication (for public access)
- Using a custom subdomain
{{< /markdown >}}

{{< /tab >}}
{{< tab "Using @app_env.server" >}}
{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/hello-world-app-server.py" lang=python >}}

{{< markdown >}}
This example demonstrates:

- Creating a custom Docker image with Streamlit
- Using the `@app_env.server` decorator to define a server function that runs the Streamlit hello app.
- Configuring the port
- Setting resource limits
- Disabling authentication (for public access)
- Using a custom subdomain
{{< /markdown >}}

{{< /tab >}}
{{< /tabs >}}

Once deployed, your app will be accessible at the generated URL or your custom subdomain.

## Differences from TaskEnvironment

While `AppEnvironment` inherits from `Environment` (the same base class as `TaskEnvironment`), it has several app-specific parameters:

| Parameter | AppEnvironment | TaskEnvironment | Description |
|-----------|----------------|-----------------|-------------|
| `type` | ✅ | ❌ | Type of app (e.g., "FastAPI", "Streamlit") |
| `port` | ✅ | ❌ | Port the app listens on |
| `args` | ✅ | ❌ | Arguments to pass to the app |
| `command` | ✅ | ❌ | Command to run the app |
| `requires_auth` | ✅ | ❌ | Whether app requires authentication |
| `scaling` | ✅ | ❌ | Autoscaling configuration |
| `domain` | ✅ | ❌ | Custom domain/subdomain |
| `links` | ✅ | ❌ | Links to include in the App UI page |
| `include` | ✅ | ❌ | Files to include in app |
| `parameters` | ✅ | ❌ | Parameters to pass to app |
| `cluster_pool` | ✅ | ❌ | Cluster pool for deployment |

Parameters like `image`, `resources`, `secrets`, `env_vars`, and `depends_on` are shared between both environment types. See the [task configuration](../task-configuration/) docs for details on these shared parameters.


## Configuration topics

Learn more about configuring apps:

- [**Environment settings**](./app-environment-settings): Images, resources, secrets, and app-specific settings like `type`, `port`, `args`, `requires_auth`
- [**App startup**](./app-environment-settings#app-startup): Understanding the difference between `args` and `command`
- [**Including additional files**](./including-additional-files): How to include additional files needed by your app
- [**App parameters**](./passing-parameters): Pass parameters to your app at deployment time
- [**Autoscaling apps**](./app-environment-settings#scaling): Configure scaling up and down based on traffic with idle TTL
- [**App depending on other environments**](./apps-depending-on-environments): Use `depends_on` to deploy dependent apps together
