---
title: End in an app
description: Deploy an app with the exact model version a factory built, after checks and a person's approval, and roll it back by pinning a version.
icon: rocket-takeoff
weight: 3
variants: -flyte +union
---

# End in an app

> [!NOTE] Preview feature
> Factories are in preview. If you want changes or improvements, talk to the Union team.
>
> Serving from a factory requires `flyteplugins-union` 0.15.0 or later.

A factory can end in a running [app](../apps/_index) instead of an artifact. The factory builds the data and the model, checks them, and then deploys the app with the exact model version it built. One `materialize` does all of it.

## Serve a model

`factory.serve(name).using(app, **params)` works like `factory.build(...).using(task, **args)`. The name is the app's name, and each keyword binds one of the app's [parameters](../apps/configure-apps/passing-parameters) to an artifact:

```python
from flyteplugins.union import factory

from beans_app import serving        # a FastAPIAppEnvironment named "beans-api"
from beans_tasks import finetune, gate, prepare

dataset = factory.build("beans_dataset").using(prepare, dataset="AI-Lab-Makerere/beans")
model, metrics = factory.build("beans_classifier", "beans_metrics", kind={"beans_classifier": "model"}).using(
    finetune, data=dataset, epochs=2
)
approved = factory.build("beans_approved", kind="model").using(gate, model=model, report=metrics, min_accuracy=0.9)
api = factory.serve("beans-api").using(serving, model=approved)

beans = factory.Factory("beans", api)
```

The app is an ordinary app environment. Its parameter names the artifact it serves, and the factory binds it to one version at a time:

```python
serving = FastAPIAppEnvironment(
    name="beans-api",
    app=app,
    image=flyte.Image.from_debian_base(name="beans-api").with_pip_packages("fastapi", "uvicorn", "transformers", "torch"),
    parameters=[
        Parameter(name="model", value=flyte.app.ArtifactValue(name="beans_approved", type="directory"), mount="/tmp/model"),
    ],
)
```

`serve` returns an endpoint. You can materialize it and list it in `Factory(...)`, but no build can read it. Each parameter takes one artifact that holds a `flyte.io.File` or `flyte.io.Dir`.

## Deploy and materialize

```bash
flyte factory deploy beans.py
flyte factory materialize beans beans-api --wait
```

At deploy, the factory builds the app's image and code bundle and records the app definition. When you materialize the endpoint, the factory builds whatever is stale, then deploys the app with each parameter set to the artifact version it resolved. The factory task deploys the app itself, so no extra pod starts. The version is recorded as the app's input, so the artifact's page lists the app that serves it.

Run it again and every build is a cache hit. The app's definition is unchanged, so it is left alone.

## Check before it goes live

A gate is a build that returns its input or fails. When it fails, nothing after it is built and the app keeps serving the model it had:

```python
@env.task(cache="auto")
async def gate(model: Dir, report: File, min_accuracy: float = 0.9) -> Dir:
    async with report.open("rb") as fh:
        accuracy = json.loads(bytes(await fh.read()))["accuracy"]
    if accuracy < min_accuracy:
        raise flyte.errors.RuntimeUserError("BelowBar", f"accuracy {accuracy:.3f} is below {min_accuracy}")
    return model
```

To have a person approve a release, add a gate that waits on an [external condition](../tasks/task-programming/conditions):

```python
@env.task(cache="auto")
async def release(model: Dir, report: File) -> Dir:
    decision = await flyte.new_condition.aio(
        "release-beans-classifier",
        prompt="**Release the new beans classifier?**",
        prompt_type="markdown",
        data_type=bool,
        timeout=datetime.timedelta(hours=24),
    )
    if not await decision.wait.aio():
        raise flyte.errors.RuntimeUserError("Rejected", "a reviewer rejected this model")
    return model


released = factory.build("beans_released", kind="model").using(release, model=approved, report=metrics)
api = factory.serve("beans-api").using(serving, model=released)
```

While it waits, the factory's materialization page shows a bar above the graph with the prompt and a **Review** button. You can also answer from the run page, or with `flyte signal condition <run> <action> true`. An approval is cached like any build, so a later materialization of the same model doesn't ask again. A rejection isn't cached, so the next materialization asks again.

## One app, one partition

An endpoint is one app, so it serves one partition at a time. It can have at most one partition key, and it must be a time. For example, a model retrained each day:

* **A range deploys the newest partition.** Materializing `--partition date=2026-09-01..2026-09-07` builds and deploys the September 7 model, and skips the older days' builds, since nothing would serve them.
* **A newer model is never replaced by an older one.** If the app already serves September 7, a backfill or a late-arriving September 3 builds that day's model but leaves the app alone.
* **Roll back by pinning.** `--version` reads a version instead of building it, and deploys it even when it is older:

  ```bash
  flyte factory materialize beans beans-api --version beans_released=<version> --wait
  ```

## Sharded models

A model imported with [prefetch](../apps/serve-and-deploy-apps/prefetching-models) and sharded for tensor parallelism can only be loaded with the GPU count and engine it was sharded for. The factory reads both from the artifact and refuses to deploy an app that asks for a different number of GPUs or runs a different engine.

## Examples

The `flyteplugins-union` repository has runnable examples in `examples/factory/`:

* `gates/`: two approvals and an automatic check between raw data and a small API. Each step runs in seconds.
* `beans/`: data preparation, fine-tuning, an accuracy gate, an approval, daily batch scoring, and a FastAPI app.
* `hf_model.py`: import a Hugging Face model, check it, and serve it with vLLM.

Next, [trigger a factory](./triggers) to keep the app up to date.
