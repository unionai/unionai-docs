---
title: Configure apps
weight: 10
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Configure apps

`[[AppEnvironment]]` allows you to configure the environment in which your app runs, including the container image, compute resources, secrets, domains, scaling behavior, and more.

Similar to `[[TaskEnvironment]]`, configuration can be set when creating the `[[AppEnvironment]]` object. Unlike tasks, apps are long-running services, so they have additional configuration options specific to web services:

- **Port configuration**: What port the app listens on
- **Command and arguments**: How to start the app
- **Scaling**: Autoscaling configuration for handling variable load
- **Domains**: Custom domains and subdomains for your app
- **Authentication**: Whether the app requires authentication to access
- **App dependencies**: Apps that this app depends on (via `depends_on`)

## Hello World example

Here's a complete example of deploying a simple Streamlit "hello world" app with a custom subdomain:

{{< code file="/external/unionai-examples/v2/user-guide/configure-apps/hello-world-app.py" lang=python >}}

This example demonstrates:

- Creating a custom Docker image with Streamlit
- Setting the command to run the Streamlit hello app
- Configuring the port
- Setting resource limits
- Disabling authentication (for public access)
- Using a custom subdomain

Once deployed, your app will be accessible at the generated URL or your custom subdomain.

## Configuration topics

Learn more about configuring apps:

- [**Environment settings**](./app-environment-settings): Images, resources, secrets, and app-specific settings like `type`, `port`, `args`, `requires_auth`
- [**App startup**](./app-environment-settings#app-startup): Understanding the difference between `args` and `command`
- [**Including additional files**](./including-additional-files): How to include additional files needed by your app
- [**App inputs**](./passing-inputs): Pass inputs to your app at deployment time
- [**Autoscaling apps**](./app-environment-settings#autoscaling-apps): Configure scaling up and down based on traffic with idle TTL
- [**App depending on other environments**](./apps-depending-on-environments): Use `depends_on` to deploy dependent apps together

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
| `inputs` | ✅ | ❌ | Inputs to pass to app |
| `cluster_pool` | ✅ | ❌ | Cluster pool for deployment |

Parameters like `image`, `resources`, `secrets`, `env_vars`, and `depends_on` are shared between both environment types. See the [task configuration](../task-configuration/) docs for details on these shared parameters.

