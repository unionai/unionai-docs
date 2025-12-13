---
title: Anatomy of an app
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Anatomy of an app

To understand how app serving works in Flyte 2, it helps to understand the key concepts and how they relate to tasks.

## Key concepts

* **App**: A long-running service that provides functionality via HTTP endpoints. Unlike tasks, which run to completion, apps remain active and can handle multiple requests over time.

* **AppEnvironment**: An `AppEnvironment` object is the abstraction that defines the hardware and software environment in which an app runs.
    * The hardware environment is specified by parameters that define the type of compute resources (e.g., CPU, memory, GPU) allocated to the app.
    * The software environment is specified by parameters that define the container image, including dependencies, required to run the app.
    * Apps have additional configuration options specific to services, such as port configuration, scaling behavior, and domain settings.

* **Task**: A Python function that runs to completion.
    * Tasks are defined using the `@env.task` decorator, where the `env` refers to a `TaskEnvironment` object.
    * Tasks execute, produce outputs, and then terminate.
    * Tasks can invoke other tasks, creating workflows.

* **App vs Task**: The fundamental difference is that apps are services that stay running and handle requests, while tasks are functions that execute once and complete.

## How app serving works

When you serve an app:

1. **Configuration**: You define an `AppEnvironment` that specifies:
   - The container image and dependencies
   - Compute resources (CPU, memory, GPU)
   - Port configuration
   - Scaling settings
   - Domain/subdomain (optional)

2. **Deployment**: The app is deployed to your Union/Flyte instance, which:
   - Builds or pulls the container image
   - Allocates compute resources
   - Starts the app service
   - Makes it accessible via HTTP

3. **Serving**: The app runs continuously and:
   - Listens on the configured port
   - Handles incoming HTTP requests
   - Can scale up or down based on traffic (if autoscaling is configured)
   - Remains active until explicitly stopped or deactivated

4. **Access**: Once served, the app is accessible:
   - Via the generated URL from your Union/Flyte instance
   - Through custom domains/subdomains (if configured)
   - By other apps or tasks that need to call it

## Relationship to tasks

Apps and tasks work together:

- **Tasks can call apps**: Tasks can make HTTP requests to apps to use their functionality
- **Apps can call tasks**: Apps can invoke tasks to perform computations
- **Apps can depend on tasks**: Apps can use outputs from task runs as inputs (via `RunOutput`)
- **Apps can depend on other apps**: Apps can reference other apps' endpoints (via `AppEndpoint`)

This integration allows you to build complex systems where long-running services (apps) work together with on-demand computations (tasks).

## Next steps

To learn more about building and serving apps:

- [**Serving apps**](./serving-apps): A hello world example of serving an app
- [**Configuring apps**](../configure-apps/): Learn how to configure app environments
- [**Building apps**](../build-apps/): Explore different types of apps you can build
- [**Serving and deploying apps**](../serve-and-deploy-apps/): Understand serving vs deployment

