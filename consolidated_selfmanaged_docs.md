# Documentation
**Variant:** selfmanaged  
**Generated:** 2025-12-05

This is a consolidated view of all documentation pages in hierarchical order.

# Documentation

Welcome to the documentation.

## Subpages

- [User Guide](user-guide/index.md)
- [Tutorials](tutorials/index.md)
- [Integrations](integrations/index.md)
- [API Reference](api-reference/index.md)
- [Community](community/index.md)
- [Release Notes](release-notes.md)

---
**PAGE: User Guide**
**SOURCE: user-guide/index.md**


# Union.ai Self-managed

Union.ai empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With Union.ai your team can:

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> These are the Union.ai **2.0 beta** docs.
> To switch to [version 1.0](/docs/v1/selfmanaged/) or to another product variant, use the selectors above.
>
> Union.ai is built on top of the leading open-source workflow orchestrator, [Flyte](/docs/v2/flyte/).
>
> Union.ai Self-managed provides all the features of Flyte, plus much more
> while letting you keep your data and workflow code on your infrastructure and under your own management.

### 💡 [Flyte 2](flyte-2/index.md)

Flyte 2 represents a fundamental shift in how AI workflows are written and executed. Learn
more in this section.

### 🔢 [Getting started](getting-started/index.md)

Install Flyte 2, configure your local IDE, create and run your first task, and inspect the results in 2 minutes.

## Subpages
- [Flyte 2](flyte-2/index.md)
- [Getting started](getting-started/index.md)
- [Task configuration](task-configuration/index.md)
- [Task programming](task-programming/index.md)
- [Considerations](considerations.md)

---
**PAGE: User Guide**
**SOURCE: user-guide/index.md**


# Union.ai Self-managed

Union.ai empowers AI development teams to rapidly ship high-quality code to production by offering optimized performance, unparalleled resource efficiency, and a delightful workflow authoring experience. With Union.ai your team can:

* Run complex AI workloads with performance, scale, and efficiency.
* Achieve millisecond-level execution times with reusable containers.
* Scale out to multiple regions, clusters, and clouds as needed for resource availability, scale, or compliance.

> [!NOTE]
> These are the Union.ai **2.0 beta** docs.
> To switch to [version 1.0](/docs/v1/selfmanaged/) or to another product variant, use the selectors above.
>
> Union.ai is built on top of the leading open-source workflow orchestrator, [Flyte](/docs/v2/flyte/).
>
> Union.ai Self-managed provides all the features of Flyte, plus much more
> while letting you keep your data and workflow code on your infrastructure and under your own management.

### 💡 [Flyte 2](flyte-2/index.md)

Flyte 2 represents a fundamental shift in how AI workflows are written and executed. Learn
more in this section.

### 🔢 [Getting started](getting-started/index.md)

Install Flyte 2, configure your local IDE, create and run your first task, and inspect the results in 2 minutes.

## Subpages
- [Flyte 2](flyte-2/index.md)
- [Getting started](getting-started/index.md)
- [Task configuration](task-configuration/index.md)
- [Task programming](task-programming/index.md)
- [Considerations](considerations.md)

---
**PAGE: Tutorials**
**SOURCE: tutorials/index.md**


# Tutorials

This section contains tutorials that showcase relevant use cases and provide step-by-step instructions on how to implement various features using Flyte and Union.

### 🔗 [Multi-agent trading simulation](trading-agents.md)

A multi-agent trading simulation, modeling how agents within a firm might interact, strategize, and make trades collaboratively.

### 🔗 [Run LLM-generated code](code-agent.md)

Securely execute and iterate on LLM-generated code using a code agent with error reflection and retry logic.

### 🔗 [Deep research](deep-research.md)

Build an agentic workflow for deep research with multi-step reasoning and evaluation.

### 🔗 [Hyperparameter optimization](hpo.md)

Run large-scale HPO experiments with zero manual tracking, deterministic results, and automatic recovery.

### 🔗 [Automatic prompt engineering](auto_prompt_engineering.md)

Easily run prompt optimization with real-time observability, traceability, and automatic recovery.

### 🔗 [Text-to-SQL](text_to_sql.md)

Learn how to turn natural language questions into SQL queries with Flyte and LlamaIndex, and explore prompt optimization in practice.

## Subpages
- [Automatic prompt engineering](auto_prompt_engineering.md)
- [Deep research](deep-research.md)
- [Hyperparameter optimization](hpo.md)
- [Multi-agent trading simulation](trading-agents.md)
- [Run LLM-generated code](code-agent.md)
- [Text-to-SQL](text_to_sql.md)

---
**PAGE: Tutorials**
**SOURCE: tutorials/index.md**


# Tutorials

This section contains tutorials that showcase relevant use cases and provide step-by-step instructions on how to implement various features using Flyte and Union.

### 🔗 [Multi-agent trading simulation](trading-agents.md)

A multi-agent trading simulation, modeling how agents within a firm might interact, strategize, and make trades collaboratively.

### 🔗 [Run LLM-generated code](code-agent.md)

Securely execute and iterate on LLM-generated code using a code agent with error reflection and retry logic.

### 🔗 [Deep research](deep-research.md)

Build an agentic workflow for deep research with multi-step reasoning and evaluation.

### 🔗 [Hyperparameter optimization](hpo.md)

Run large-scale HPO experiments with zero manual tracking, deterministic results, and automatic recovery.

### 🔗 [Automatic prompt engineering](auto_prompt_engineering.md)

Easily run prompt optimization with real-time observability, traceability, and automatic recovery.

### 🔗 [Text-to-SQL](text_to_sql.md)

Learn how to turn natural language questions into SQL queries with Flyte and LlamaIndex, and explore prompt optimization in practice.

## Subpages
- [Automatic prompt engineering](auto_prompt_engineering.md)
- [Deep research](deep-research.md)
- [Hyperparameter optimization](hpo.md)
- [Multi-agent trading simulation](trading-agents.md)
- [Run LLM-generated code](code-agent.md)
- [Text-to-SQL](text_to_sql.md)

---
**PAGE: Integrations**
**SOURCE: integrations/index.md**


# Integrations

Flyte is designed to be highly extensible and can be customized
in multiple ways.

## Flyte Plugins

Flyte plugins extend the functionality of the `flyte` SDK.

| Plugin | Description |
| ------ | ----------- |
| [Ray](flyte-plugins/ray.md) | Run Ray jobs on your Flyte cluster |
| [Spark](flyte-plugins/spark.md) | Run Spark jobs on your Flyte cluster |
| [OpenAI](flyte-plugins/openai/index.md) | Integrate with OpenAI SDKs in your Flyte workflows |
| [Dask](flyte-plugins/dask.md) | Run Dask jobs on your Flyte cluster |

## Subpages
- [Connectors](connectors.md)
- [Flyte plugins](flyte-plugins/index.md)

---
**PAGE: Integrations**
**SOURCE: integrations/index.md**


# Integrations

Flyte is designed to be highly extensible and can be customized
in multiple ways.

## Flyte Plugins

Flyte plugins extend the functionality of the `flyte` SDK.

| Plugin | Description |
| ------ | ----------- |
| [Ray](flyte-plugins/ray.md) | Run Ray jobs on your Flyte cluster |
| [Spark](flyte-plugins/spark.md) | Run Spark jobs on your Flyte cluster |
| [OpenAI](flyte-plugins/openai/index.md) | Integrate with OpenAI SDKs in your Flyte workflows |
| [Dask](flyte-plugins/dask.md) | Run Dask jobs on your Flyte cluster |

## Subpages
- [Connectors](connectors.md)
- [Flyte plugins](flyte-plugins/index.md)

---
**PAGE: API Reference**
**SOURCE: api-reference/index.md**


# Reference

This section provides the reference material for the Flyte SDK and CLI.

To get started, add `flyte` to your project

```shell
$ uv pip install --no-cache --prerelease=allow --upgrade flyte
```

This will install both the Flyte SDK and CLI.

### 🔗 [Flyte SDK](flyte-sdk/index.md)

The Flyte SDK provides the core Python API for building workflows and apps on your Union instance.

### 🔗 [Flyte CLI](flyte-cli.md)

The Flyte CLI is the command-line interface for interacting with your Union instance.

## Subpages
- [Flyte LLM context](flyte-context.md)
- [Flyte CLI](flyte-cli.md)
- [Flyte SDK](flyte-sdk/index.md)

---
**PAGE: API Reference**
**SOURCE: api-reference/index.md**


# Reference

This section provides the reference material for the Flyte SDK and CLI.

To get started, add `flyte` to your project

```shell
$ uv pip install --no-cache --prerelease=allow --upgrade flyte
```

This will install both the Flyte SDK and CLI.

### 🔗 [Flyte SDK](flyte-sdk/index.md)

The Flyte SDK provides the core Python API for building workflows and apps on your Union instance.

### 🔗 [Flyte CLI](flyte-cli.md)

The Flyte CLI is the command-line interface for interacting with your Union instance.

## Subpages
- [Flyte LLM context](flyte-context.md)
- [Flyte CLI](flyte-cli.md)
- [Flyte SDK](flyte-sdk/index.md)

---
**PAGE: Community**
**SOURCE: community/index.md**


# Community

Union.ai is a commercial product built on top of the open source Flyte project.

Since the success of Flyte is essential to the success of Union.ai,
the company is dedicated to building and expanding the Flyte open source project and community.

For information on how to get involved and how to keep in touch, see the [Flyte variant of this page](/docs/v2/flyte//community).

## Contributing to documentation

Union AI maintains and hosts both Flyte and Union documentation at [www.union.ai/docs](/docs/v2/root/).
The two sets of documentation are deeply integrated, as the Union product is built on top of Flyte.
To better maintain both sets of docs, they are hosted in the same repository (but rendered so that you can choose to view one or the other).

Both the Flyte and Union documentation are open source.
Flyte community members and Union customers are both welcome to contribute to the documentation.

If you are interested, see [Contributing documentation and examples](./contributing-docs/_index).

## Subpages
- [Contributing docs and examples](contributing-docs/index.md)

---
**PAGE: Community**
**SOURCE: community/index.md**


# Community

Union.ai is a commercial product built on top of the open source Flyte project.

Since the success of Flyte is essential to the success of Union.ai,
the company is dedicated to building and expanding the Flyte open source project and community.

For information on how to get involved and how to keep in touch, see the [Flyte variant of this page](/docs/v2/flyte//community).

## Contributing to documentation

Union AI maintains and hosts both Flyte and Union documentation at [www.union.ai/docs](/docs/v2/root/).
The two sets of documentation are deeply integrated, as the Union product is built on top of Flyte.
To better maintain both sets of docs, they are hosted in the same repository (but rendered so that you can choose to view one or the other).

Both the Flyte and Union documentation are open source.
Flyte community members and Union customers are both welcome to contribute to the documentation.

If you are interested, see [Contributing documentation and examples](./contributing-docs/_index).

## Subpages
- [Contributing docs and examples](contributing-docs/index.md)

---
**PAGE: Release Notes**
**SOURCE: release-notes.md**


# Release Notes

## November 2025

### :fast_forward: Grouped Runs
We redesigned the Runs page to better support large numbers of runs. Historically, large projects produced so many runs that flat listings became difficult to navigate. The new design groups Runs by their root task - leveraging the fact that while there may be millions of runs, there are typically only dozens or hundreds of deployed tasks. This grouped view, combined with enhanced filtering (by status, owner, duration, and more coming soon), makes it dramatically faster and easier to locate the exact runs users are looking for, even in the largest deployments.

![Grouped Runs View](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/release-notes/2025-11_grouped_runs.gif)

### :globe_with_meridians: Apps (beta)

You can now deploy apps in Union 2.0. Apps let you host ML models, Streamlit dashboards, FastAPI services, and other interactive applications alongside your workflows. Simply define your app, deploy it, and Union will handle the infrastructure, routing, and lifecycle management. You can even call apps from your tasks to build end-to-end workflows that combine batch processing with real-time serving.

To create an app, import `flyte` and use either `FastAPIAppEnvironment` for FastAPI applications or the generic `AppEnvironment` for other frameworks. Here's a simple FastAPI example:

```python
from fastapi import FastAPI
import flyte
from flyte.app.extras import FastAPIAppEnvironment

app = FastAPI()
env = FastAPIAppEnvironment(
    name="my-api",
    app=app,
    image=flyte.Image.from_debian_base(python_version=(3, 12))
        .with_pip_packages("fastapi", "uvicorn"),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

@env.app.get("/greeting/{name}")
async def greeting(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    flyte.init_from_config()
    flyte.deploy(env) # Deploy and serve your app
```

For Streamlit apps, use the generic `AppEnvironment` with a command:

```python
app_env = flyte.app.AppEnvironment(
    name="streamlit-hello-v2",
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages("streamlit==1.41.1"),
    command="streamlit hello --server.port 8080",
    resources=flyte.Resources(cpu="1", memory="1Gi"),
)
```

You can call apps from tasks by using `depends_on` and making HTTP requests to the app's endpoint. Please refer to the example in the [SDK repo](https://github.com/flyteorg/flyte-sdk/blob/main/examples/apps/call_apps_in_tasks/app.py). Similarly, you can call apps from other apps (see this [example](https://github.com/flyteorg/flyte-sdk/blob/main/examples/apps/app_calling_app/app.py)).

### :label: Custom context

You can now pass configuration and metadata implicitly through your entire task execution hierarchy using custom context. This is ideal for cross-cutting concerns like tracing IDs, experiment metadata, environment information, or logging correlation keys—data that needs to be available everywhere but isn't logically part of your task's computation. 

Custom context is a string key-value map that automatically flows from parent to child tasks without adding parameters to every function signature. Set it once at the run level with `with_runcontext()`, or override values within tasks using the `flyte.custom_context()` context manager:

```python
import flyte

env = flyte.TaskEnvironment("custom-context-example")

@env.task
async def leaf_task() -> str:
    # Reads run-level context
    print("leaf sees:", flyte.ctx().custom_context)
    return flyte.ctx().custom_context.get("trace_id")

@env.task
async def root() -> str:
    return await leaf_task()

if __name__ == "__main__":
    flyte.init_from_config()
    # Base context for the entire run
    run = flyte.with_runcontext(custom_context={"trace_id": "root-abc", "experiment": "v1"}).run(root)
    print(run.url)
```

### :lock: Secrets UI

Now you can view and create secrets directly from the UI. Secrets are stored securely in your configured secrets manager and injected into your task environments at runtime.

![Secrets Creation Flow](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/release-notes/2025-11_secrets_creation.gif)

### Image Builds now run in the same project-domain
The image build task is now executed within the same project and domain as the user task, rather than in system-production. This change improves isolation and is a key step toward supporting multi-dataplane clusters.

### Support for secret mounts in Poetry and UV projects
We added support for mounting secrets into both Poetry and UV-based projects. This enables secure access to private dependencies or credentials during image build.

```python
import pathlib

import flyte

env = flyte.TaskEnvironment(
    name="uv_project_lib",
    resources=flyte.Resources(memory="1000Mi"),
    image=(
        flyte.Image.from_debian_base().with_uv_project(
            pyproject_file=pathlib.Path(__file__).parent / "pyproject.toml",
            pre=True,
            secret_mounts="my_secret",
        )
    ),
)
```

## October 2025

### :infinity: Larger fanouts
You can now run up to 50,000 actions within a run and up to 1,000 actions concurrently. 
To enable observability across so many actions, we added group and sub-actions UI views, which show summary statistics about the actions which were spawned within a group or action.
You can use these summary views (as well as the action status filter) to spot check long-running or failed actions.

![50k Fanout Visualization](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_50k_fanout.gif)

### :computer: Remote debugging for Ray head nodes
Rather than locally reproducing errors, sometimes you just want to zoom into the remote execution and see what's happening.
We directly enable this with the debug button.
When you click "Debug action" from an action in a run, we spin up that action's environment, code, and input data, and attach a live VS Code debugger.
Previously, this was only possible with vanilla Python tasks.
Now, you can debug multi-node distributed computations on Ray directly.

![Debugging Ray Head Node](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_ray_head_debug.gif)

### :zap: Triggers and audit history
[Triggers](../user-guide/task-configuration/triggers.md) let you templatize and set schedules for your workflows, similar to Launch Plans in Flyte 1.0.

```python
@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"
```

Once you deploy, it's possible to see all the triggers which are associated with a task:

![Triggers for a Task](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_triggers_for_task.png)

We also maintain an audit history of every deploy, activation, and deactivation event, so you can get a sense of who's touched an automation.

![Triggers Activity Log](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_trigger_activity_log.gif)

### :arrow_up: Deployed tasks and input passing

You can see the runs, task spec, and triggers associated with any deployed task, and launch it from the UI. We've converted the launch forms to a convenient JSON Schema syntax, so you can easily copy-paste the inputs from a previous run into a new run for any task.

![Deployed Tasks and Input Passing](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_tasks_and_input_passing.gif)
