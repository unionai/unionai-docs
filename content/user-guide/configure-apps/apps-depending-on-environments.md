---
title: Apps depending on other environments
weight: 6
variants: +flyte +serverless +byoc +selfmanaged
---

# Apps depending on other environments

The `depends_on` parameter allows you to specify that one app depends on another app (or task environment). When you deploy an app with `depends_on`, Flyte ensures that all dependencies are deployed first.

## Basic usage

Use `depends_on` to specify a list of environments that this app depends on:

```python
app1_env = flyte.app.AppEnvironment(name="backend-api", ...)

app2_env = flyte.app.AppEnvironment(
    name="frontend-app",
    depends_on=[app1_env],  # Ensure backend-api is deployed first
    # ...
)
```

When you deploy `app2_env`, Flyte will:
1. First deploy `app1_env` (if not already deployed)
2. Then deploy `app2_env`
3. Make sure `app1_env` is available before `app2_env` starts

## Example: App calling another app

Here's a complete example where one FastAPI app calls another:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/app_calling_app.py" lang=python >}}

When you deploy `env2`, Flyte will:
1. Deploy `env1` first (backend-api)
2. Wait for `env1` to be ready
3. Deploy `env2` (frontend-api)
4. `env2` can then access `env1.endpoint` to make requests

## Dependency chain

You can create chains of dependencies:

```python
app1_env = flyte.app.AppEnvironment(name="service-1", ...)
app2_env = flyte.app.AppEnvironment(name="service-2", depends_on=[app1_env], ...)
app3_env = flyte.app.AppEnvironment(name="service-3", depends_on=[app2_env], ...)

# Deploying app3_env will deploy in order: app1_env -> app2_env -> app3_env
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

When deploying `api_env`, both `backend_env` and `database_env` will be deployed first (they may be deployed in parallel if they don't depend on each other).

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
2. Deploy dependencies in the correct order
3. Ensure dependencies are ready before deploying dependent apps

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

This ensures the task environment is available when the app is deployed (useful if the app needs to call tasks in that environment).

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

The root app can route traffic to either variant A or B based on A/B testing logic, and both variants will be deployed before the root app starts.

## Limitations

- Circular dependencies are not supported
- Dependencies must be in the same project/domain
- Dependency deployment order is deterministic but dependencies at the same level may deploy in parallel

