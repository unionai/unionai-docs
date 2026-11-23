---
title: Apps depending on other environments
description: Use depends_on so deploying an app or task environment also deploys the environments it needs.
icon: link-45deg
weight: 6
variants: +flyte +union
---

# Apps depending on other environments

The `depends_on` parameter allows you to specify that one app depends on another app (or task environment). When you deploy an app with `depends_on`, Flyte deploys its dependencies in the same deployment.

## Basic usage

Use `depends_on` to specify a list of environments that this app depends on:

```python
app1_env = flyte.app.AppEnvironment(name="backend-api", ...)

app2_env = flyte.app.AppEnvironment(
    name="frontend-app",
    depends_on=[app1_env],  # Deploying frontend-app also deploys backend-api
    # ...
)
```

When you deploy `app2_env`, Flyte puts `app1_env` and `app2_env` in one deployment plan and deploys them together. It doesn't wait for `app1_env` to be ready before it deploys `app2_env`, so code in `app2_env` that calls `app1_env` as soon as it starts should retry until `app1_env` answers.

## Example: App calling another app

Here's a complete example where one FastAPI app calls another:

{{< code file="/unionai-examples/v2/user-guide/build-apps/fastapi/app_calling_app.py" lang=python >}}

When you deploy `env2`, Flyte deploys `env1` (backend-api) and `env2` (frontend-api) together. `env2` then reaches `env1` through `env1.endpoint`.

## Dependency chain

You can create chains of dependencies:

```python
app1_env = flyte.app.AppEnvironment(name="service-1", ...)
app2_env = flyte.app.AppEnvironment(name="service-2", depends_on=[app1_env], ...)
app3_env = flyte.app.AppEnvironment(name="service-3", depends_on=[app2_env], ...)

# Deploying app3_env also deploys app2_env and app1_env, all in one deployment
```

## Multiple dependencies

An app can depend on multiple environments:

```python
backend_env = flyte.app.AppEnvironment(name="backend", ...)
database_env = flyte.app.AppEnvironment(name="database", ...)

api_env = flyte.app.AppEnvironment(
    name="api",
    depends_on=[backend_env, database_env],  # Depends on both
    # ...
)
```

When you deploy `api_env`, `backend_env` and `database_env` are deployed with it.

## Using AppEndpoint for dependency URLs

When one app depends on another, you can use `AppEndpoint` to get the URL:

```python
backend_env = flyte.app.AppEnvironment(name="backend-api", ...)

frontend_env = flyte.app.AppEnvironment(
    name="frontend-app",
    depends_on=[backend_env],
    parameters=[
        flyte.app.Parameter(
            name="backend_url",
            value=flyte.app.AppEndpoint(app_name="backend-api"),
        ),
    ],
    # ...
)
```

The `backend_url` parameter will be automatically set to the backend app's endpoint URL.
You can get this value in your app code using `flyte.app.get_input("backend_url")`.

## Deployment behavior

When deploying with `flyte.deploy()`:

```python
# Deploy the app (dependencies are automatically deployed)
deployments = flyte.deploy(env2)

# All dependencies are included in the deployment plan
for deployment in deployments:
    print(f"Deployed: {deployment.env.name}")
```

Flyte will:

1. Build a deployment plan that includes all dependencies
2. Deploy every environment in the plan at the same time

## Task environment dependencies

You can also depend on task environments:

```python
task_env = flyte.TaskEnvironment(name="training-env", ...)

serving_env = flyte.app.AppEnvironment(
    name="serving-app",
    depends_on=[task_env],  # Can depend on task environments too
    # ...
)
```

Deploying the app then also deploys the task environment, which is useful if the app calls tasks in it.

## Best practices

1. **Explicit dependencies**: Always use `depends_on` to make app dependencies explicit
2. **Circular dependencies**: Avoid circular dependencies (app A depends on B, B depends on A)
3. **Dependency order**: Design your dependency graph to be a DAG (Directed Acyclic Graph)
4. **Endpoint access**: Use `AppEndpoint` to pass dependency URLs as inputs
5. **Document dependencies**: Make sure your app documentation explains its dependencies

## Example: A/B testing with dependencies

Here's an example of an A/B testing setup where a root app depends on two variant apps:

```python
app_a = FastAPI(title="Variant A")
app_b = FastAPI(title="Variant B")
root_app = FastAPI(title="Root App")

env_a = FastAPIAppEnvironment(name="app-a-variant", app=app_a, ...)
env_b = FastAPIAppEnvironment(name="app-b-variant", app=app_b, ...)

env_root = FastAPIAppEnvironment(
    name="root-ab-testing-app",
    app=root_app,
    depends_on=[env_a, env_b],  # Depends on both variants
    # ...
)
```

The root app can route traffic to either variant A or B based on A/B testing logic, and both variants are deployed together with it.

## Limitations

- Circular dependencies are not supported
- Dependencies must be in the same project/domain
- `depends_on` decides which environments are deployed, not the order: all of them deploy at the same time
