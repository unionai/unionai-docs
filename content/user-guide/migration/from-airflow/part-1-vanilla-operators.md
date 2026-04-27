---
title: Part 1 — Vanilla Operators
weight: 1
variants: +flyte +union
---

# Part 1 — Vanilla Operators

This is the first part of the [Airflow → Flyte migration guide](./_index). It covers:

1. Where dependencies are specified
2. The driver task (in place of a DAG definition)
3. Triggers (in place of DAG schedules)
4. PythonOperator → `@env.task`
5. TaskFlow → `@env.task`
6. BashOperator → ContainerTask
7. KubernetesPodOperator → TaskEnvironment + PodTemplate
8. Orchestration: parallelism, conditionals, error handling

**Part 2** (later) covers provider operators: Beam, Dataproc, BigQuery, Databricks, Spark, sensors.

Each code-heavy section has a paired example in the [`airflow-examples`](https://github.com/unionai/airflow-examples/tree/main/guide/examples) repo, with an `airflow/` and a `flyte/` subdirectory.

---

## 1. Where dependencies are specified

In Airflow, dependencies are specified at the platform level. A single Airflow deployment has a base image with a fixed Python environment; every DAG author writes against the same set of installed libraries. Adding a new library means modifying the deployment (Helm `extraPipPackages`, a custom base image, or a redeploy), or working around the shared env with `PythonVirtualenvOperator`, `DockerOperator`, or `KubernetesPodOperator`.

In Flyte, dependencies are specified at the code level. Each task declares its `TaskEnvironment`, which includes the image and its dependencies. The image is the unit of isolation, and a single workflow can fan out across tasks running in different images.

Two ways to declare the image:

```python
# (a) Build with flyte.Image — from a base, add pip/apt packages, env vars, etc.
etl_env = flyte.TaskEnvironment(
    name="etl",
    image=flyte.Image.from_debian_base()
        .with_pip_packages("pandas", "pyarrow"),
)

# (b) Pass a string reference to an existing image — for example the same one
# you already deploy with in your Airflow KubernetesExecutor / KPO setup.
gpu_env = flyte.TaskEnvironment(
    name="gpu",
    image="registry.example.com/my-org/gpu-training:2026.04.01",
)
```

Docs: [TaskEnvironment](../../core-concepts/task-environment) · [Container Images](../../task-configuration/container-images)

---

## 2. The driver task (in place of DAGs)

Airflow DAGs are static graphs. The `with DAG(...)` block runs at parse time; the scheduler compiles the node/edge structure and then traverses it.

Flyte has no parse-time graph. The driver task is Python code that runs at execution time; the graph is built dynamically as the driver calls other tasks. There is no compilation step.

Flyte tasks are async-native — `@env.task` functions are typically declared `async def` and tasks are invoked with `await`. Plain `def` tasks are also supported when you don't need concurrency.

```python
@env.task
async def driver(start: date, regions: list[str]) -> list[Summary]:
    data = await fetch(start)
    summaries = await asyncio.gather(
        *[summarize(data, region) for region in regions]
    )
    return summaries
```

The driver is just a task that calls other tasks — there's no separate workflow object.

---

## 3. Triggers (in place of schedules)

Airflow's `schedule=` on a DAG maps to a Flyte `Trigger` attached to a task.

| Airflow | Flyte |
|---|---|
| `schedule="@hourly"` | `flyte.Trigger.hourly()` |
| `schedule="@daily"` | `flyte.Trigger.daily()` |
| `schedule="0 5 * * *"` | `flyte.Trigger("nightly", flyte.Cron("0 5 * * *"))` |
| `schedule="30 9 * * 1-5"` + `timezone=...` | `flyte.Trigger("biz_hours", flyte.Cron("30 9 * * 1-5", timezone="America/New_York"))` |

```python
@env.task(triggers=flyte.Trigger("daily_report", flyte.Cron("0 6 * * *")))
def generate_report(trigger_time: datetime) -> str:
    ...
```

Multiple triggers per task and parameterized trigger inputs are supported — see the [Triggers docs](../../task-configuration/triggers).

---

## 4. PythonOperator to `@env.task`

Airflow's `PythonOperator` runs a Python callable in the worker's environment. The callable's return value becomes XCom, and inputs arrive through three channels: `op_args`/`op_kwargs` passed at operator construction, the Airflow context injected as `**kwargs` (`ti`, `ds`, `dag_run`, `logical_date`, …), and `ti.xcom_pull(...)` for data from upstream tasks.

Flyte's equivalent is `@env.task` on a plain function. The function's parameters and return type are the interface — there is no separate context channel and no XCom step.

```python
# Airflow
def fetch_events(**context):
    ds = context["ds"]
    return _fetch(ds)  # returned value is serialized to XCom

def summarize(**context):
    ti = context["ti"]
    records = ti.xcom_pull(task_ids="fetch_events")
    return f"{len(records)} events on {context['ds']}"

with DAG("events", schedule="@daily", ...) as dag:
    t1 = PythonOperator(task_id="fetch_events", python_callable=fetch_events)
    t2 = PythonOperator(task_id="summarize", python_callable=summarize)
    t1 >> t2
```

```python
# Flyte
env = flyte.TaskEnvironment(name="events", image=...)

@env.task
async def fetch_events(ds: str) -> list[dict]:
    return _fetch(ds)

@env.task
async def summarize(ds: str, records: list[dict]) -> str:
    return f"{len(records)} events on {ds}"

@env.task
async def driver(ds: str) -> str:
    records = await fetch_events(ds)
    return await summarize(ds, records)
```

A few things change in the move:

- **Inputs are the function parameters.** No `**context`. If the task needs the run's date, declare it as a parameter (`ds: str`) and the driver passes it in. The driver itself can receive trigger time when a [Trigger](../../task-configuration/triggers) fires it.
- **Data flows through `await`, not XCom.** The value returned by `fetch_events` is the value `summarize` receives — the function call graph IS the dependency graph. No `xcom_pull` and no `t1 >> t2` to maintain separately from the data flow.
- **Types are part of the signature.** Flyte uses the hints to serialize between tasks, but keep expectations calibrated: the runtime is more like typed JSON than a fully enforced contract. It is useful as documentation and for tooling, not as a strict static check.
- **Async-native, sync-also-works.** Tasks are typically `async def` and invoked with `await`. Plain `def` tasks are fully supported if you'd rather stay in a sync codebase — you just give up some of the flexibility async offers.

The driver above has nothing in it but task calls, for readability. It doesn't have to — a driver is just a `@env.task`, and any code that belongs in a Python function belongs in a driver: plain expressions, loops, `if`/`try`, helpers. Turn something into a `@env.task` when you want it to have its own resources, image, retries, caching, or parallelism. Otherwise leave it as regular Python and call it inline.

Docs: [Tasks](../../core-concepts/tasks)

### File and Dir — for data that doesn't fit in a return value

Primitive and JSON-serializable values (`int`, `str`, `list`, `dict`, dataclasses, Pydantic models) flow directly as return values — the SDK serializes them. Same shape as XCom, but typed. Most tasks will use these and nothing else.

Flyte adds `File` and `Dir` for the cases where the payload is too big or too binary to inline. In Airflow this is where pipelines step outside the framework: XCom is a Postgres row with a soft ~48KB limit, so larger payloads are written to a shared filesystem or object storage and a path is passed as a string — the upload, the lifecycle, and the cleanup are the author's responsibility, outside Airflow's model.

Flyte covers both cases with the same interface. A task that returns `File` or `Dir` is declaring that its output is an offloaded blob, and the SDK handles the upload on write and the download on read.

```python
import flyte
from flyte.io import File, Dir

@env.task
async def extract(ds: str) -> File:
    # Stream straight to remote storage — no local temp needed.
    file = File.new_remote()
    async with file.open("wb") as f:
        await f.write(b"col1,col2\nfoo,bar\n")
    return file

@env.task
async def count_rows(csv: File) -> int:
    async with csv.open("rb") as f:
        data = await f.read()
    return data.count(b"\n") - 1
```

The `File` object travels between tasks the same way an `int` does — as a typed argument. Underneath, it carries a remote path. Common methods:

- `File.new_remote()` — new reference in the run's scratch area, for streaming writes.
- `File.from_local(path)` / `from_local_sync(path)` — upload a local file, get a `File` back.
- `File.from_existing_remote(uri)` — wrap an existing remote URI (for example, a path produced by an upstream system).
- `await file.open("rb" | "wb")` / `file.open_sync(...)` — stream read/write.
- `await file.download()` / `file.download_sync()` — materialize to a local path and return it.

`Dir` has the same surface for directories, plus `walk()` and `list_files()` to iterate entries.

Docs: [Files and directories](../../task-programming/files-and-directories)

**Example pair:** [`examples/02_python/`](https://github.com/unionai/airflow-examples/tree/main/guide/examples/02_python)

---

## 5. TaskFlow to `@env.task`

If the DAG you're porting uses Airflow's TaskFlow API (`@task`, `@dag`), the surface move is small: `@task` becomes `@env.task`, the function's return value is the data (no `ti.xcom_pull`), and function calls ARE the dependencies (no `>>`). A lot of TaskFlow code compiles to Flyte with little more than a find-and-replace on the decorator.

```python
# Airflow TaskFlow
from airflow.decorators import dag, task

@dag(schedule="@daily", start_date=datetime(2026, 1, 1), catchup=False)
def events():
    @task
    def fetch_events() -> list[dict]:
        return _fetch()

    @task
    def summarize(records: list[dict]) -> str:
        return f"{len(records)} events"

    summarize(fetch_events())

events()
```

```python
# Flyte
env = flyte.TaskEnvironment(name="events", image=...)

@env.task
async def fetch_events() -> list[dict]:
    return _fetch()

@env.task
async def summarize(records: list[dict]) -> str:
    return f"{len(records)} events"

@env.task(triggers=flyte.Trigger.daily())
async def driver() -> str:
    return await summarize(await fetch_events())
```

The thing worth internalizing — and the main place this stops being a find-and-replace — is what the outer function is doing.

An Airflow `@dag` function runs at **parse time**. Calling `fetch_events()` inside it doesn't run `fetch_events` — it registers a task and an edge in the static graph. The scheduler later traverses that graph. By the time the tasks actually execute, the `@dag` function is long gone.

A Flyte driver is a `@env.task` that runs at **execution time**. There is no parse-time graph-building step. Calling `await fetch_events()` actually calls `fetch_events`. That means the driver — and any task — is just Python: `if`/`else`, `try`/`except`, loops, recursion, calling other tasks from inside other tasks, nested drivers, reading a value from one task and deciding what to do next. All of it works because there is no static graph to fit into.

To make the point concrete — a task can call itself:

```python
@env.task
async def countdown(n: int) -> int:
    if n == 0:
        return 0
    return 1 + await countdown(n - 1)
```

Each `await countdown(...)` call is a real task invocation — the graph grows as the computation runs. This is impossible to express in Airflow's `@dag` model, where the graph has to be known before execution.

The practical effect: patterns that Airflow encodes with its own primitives (`BranchPythonOperator`, `ShortCircuitOperator`, `trigger_rule`, `.expand()` for dynamic mapping, custom `XComArg` gymnastics) are just Python constructs in Flyte. Branching is `if`. Short-circuit is `return`. Dynamic mapping is `asyncio.gather` or `flyte.map`. Error handling is `try`/`except`/`finally`. Section 8 covers these with runnable examples.

### TaskFlow decorator variants

TaskFlow ships several decorators beyond `@task`. Rough mapping:

| TaskFlow | Flyte equivalent |
|---|---|
| `@task` | `@env.task` |
| `@task.bash` | [`ContainerTask`](#6-bashoperator-to-containertask) |
| `@task.virtualenv` | `@env.task` on a `TaskEnvironment` with its own image |
| `@task.docker` | `@env.task` on a `TaskEnvironment` with `image=...` |
| `@task.kubernetes` | [`TaskEnvironment` + PodTemplate](#7-kubernetespodoperator-to-taskenvironment--podtemplate) |
| `@task.branch` | plain `if` in the driver |
| `@task.short_circuit` | plain `return` in the driver |

**Example pair:** [`examples/03_taskflow/`](https://github.com/unionai/airflow-examples/tree/main/guide/examples/03_taskflow)

---

## 6. BashOperator to ContainerTask

Airflow's `BashOperator` runs a shell command in the Airflow worker's image, with inputs rendered into the command via Jinja templating and output captured as the last line of stdout.

```python
BashOperator(
    task_id="extract",
    bash_command="gsutil cp gs://bucket/data-{{ ds }}.csv /tmp/data.csv "
                 "&& wc -l /tmp/data.csv | awk '{print $1}'",
    do_xcom_push=True,
)
```

Flyte's equivalent is a `ContainerTask`: specify an image, a command, typed inputs, and typed outputs. Inputs are substituted via `{{.inputs.<name>}}`; outputs are files the container writes to `output_data_dir`, which Flyte reads back with the declared types.

```python
import flyte
from flyte.extras import ContainerTask

extract = ContainerTask(
    name="extract",
    image=flyte.Image.from_base("google/cloud-sdk:slim"),
    inputs={"date": str},
    outputs={"row_count": int},
    input_data_dir="/var/inputs",
    output_data_dir="/var/outputs",
    command=[
        "/bin/sh", "-c",
        "gsutil cp gs://bucket/data-{{.inputs.date}}.csv /tmp/data.csv && "
        "wc -l /tmp/data.csv | awk '{print $1}' > /var/outputs/row_count",
    ],
)
```

A `ContainerTask` is invoked the same way as any other task — by calling it from a driver with `await`:

```python
container_env = flyte.TaskEnvironment.from_task("extract_env", extract)
env = flyte.TaskEnvironment(
    name="pipeline",
    image=flyte.Image.from_debian_base().with_uv_project(pyproject_file="pyproject.toml"),
    depends_on=[container_env],
)

@env.task
async def driver(date: str) -> int:
    return await extract(date=date)
```

Two things about the invocation:

- `TaskEnvironment.from_task(...)` wraps the container task in an environment so it can be registered alongside the driver.
- The driver's env `depends_on=[container_env]` so Flyte registers both together. The driver's own image needs Flyte installed (that's what `from_uv_project` does — builds an image from your `pyproject.toml`, which includes `flyte`). The container task's image does *not* need Flyte — it just needs the tools its command invokes.

### When to use `ContainerTask`

`ContainerTask` is the right choice when the container shouldn't or can't have Flyte installed — for example:

- The tool is not Python (a Go/C CLI, a bioinformatics binary, an ML framework container)
- You want to reuse an existing production image without modifying it
- You want to stay out of Python entirely for the task body

If you already have Python in the loop and just need to shell out for one step, a regular `@env.task` with `subprocess` is simpler:

```python
@env.task
async def extract(date: str) -> int:
    import subprocess
    subprocess.run(["gsutil", "cp", f"gs://bucket/data-{date}.csv", "/tmp/data.csv"], check=True)
    out = subprocess.check_output(["wc", "-l", "/tmp/data.csv"])
    return int(out.split()[0])
```

### How the arguments map

| BashOperator | ContainerTask |
|---|---|
| `bash_command` (string) | `command=[...]` (list; you choose the shell) |
| (implicit worker image) | `image=` (explicit, per task) |
| `env` / `append_env` | `flyte.Image.from_...().with_env_vars(...)` or the `TaskEnvironment` |
| `{{ ds }}`, `{{ ti.xcom_pull(...) }}` | `{{.inputs.<name>}}` |
| `do_xcom_push=True` (last stdout line) | `outputs={...}`, written to files in `output_data_dir` |
| `cwd` | `cd ... && ...` inside the command |

**Example pair:** [`examples/01_bash/`](https://github.com/unionai/airflow-examples/tree/main/guide/examples/01_bash)

Docs: [Container Tasks](../../task-programming/container-tasks)

---

## 7. KubernetesPodOperator to TaskEnvironment + PodTemplate

`KubernetesPodOperator` (KPO) gives you the full pod spec: image, commands, env, secrets, resources, volumes, node selectors, tolerations, service accounts, affinity — plus XCom via a sidecar writing to `/airflow/xcom/return.json`.

In Flyte, the same knobs live in three places:

1. **`TaskEnvironment(...)`** — the common knobs. Image, resources, env vars, secrets, interruptible/spot, and an option to add a `pod_template` for every task in the env.
2. **`@env.task(...)`** — per-task overrides on top of the env: retries, timeout, cache, triggers, and a task-level `pod_template` if this one task needs to differ.
3. **`flyte.PodTemplate(...)`** — raw Kubernetes escape hatch. Wraps `kubernetes.client.V1PodSpec`, so anything in the pod spec (volumes, node selectors, tolerations, affinity, service accounts, sidecars, init containers, image pull secrets, security contexts, lifecycle hooks) is available.

XCom has no equivalent — the task's typed return value is the output, and large payloads use `File`/`Dir` (Section 4). The sidecar-writing-to-`/airflow/xcom/return.json` contract doesn't exist.

### Where every KPO knob lands

| KPO argument | Flyte location |
|---|---|
| `image` | `TaskEnvironment(image=...)` |
| `cmds`, `arguments` | function body of `@env.task` |
| `env_vars` (dict) | `TaskEnvironment(env_vars={...})` |
| `secrets=[Secret(...)]` | `TaskEnvironment(secrets=[flyte.Secret(...)])` |
| `container_resources` (requests/limits) | `TaskEnvironment(resources=flyte.Resources(cpu=(1,4), memory="2Gi", gpu="T4:1"))` |
| `node_selector`, `tolerations`, `affinity` | `flyte.PodTemplate(pod_spec=V1PodSpec(node_selector=..., tolerations=..., affinity=...))` |
| `service_account_name` | `PodTemplate(pod_spec=V1PodSpec(service_account_name=...))` |
| `volumes`, `volume_mounts` | `PodTemplate(pod_spec=V1PodSpec(volumes=[...], containers=[V1Container(volume_mounts=[...])]))` |
| `image_pull_secrets` | `PodTemplate(pod_spec=V1PodSpec(image_pull_secrets=[V1LocalObjectReference(name=...)]))` |
| `security_context` | `PodTemplate(pod_spec=V1PodSpec(security_context=...))` |
| `labels`, `annotations` | `PodTemplate(labels={...}, annotations={...})` |
| `init_containers`, sidecars | `PodTemplate(pod_spec=V1PodSpec(init_containers=[...], containers=[primary, ...]))` |
| `retries`, `retry_delay` | `@env.task(retries=...)` |
| `execution_timeout` | `@env.task(timeout=timedelta(...))` |
| `do_xcom_push` + sidecar contract | function return type — primitives/dataclasses inline, large payloads via `File`/`Dir` |
| `on_finish_action` / pod cleanup | handled by Flyte — pods are cleaned up per run lifecycle |

### What a fully-specified task looks like

```python
from datetime import timedelta
from kubernetes.client import V1Container, V1PodSpec

import flyte

pod_template = flyte.PodTemplate(
    primary_container_name="primary",
    labels={"team": "etl"},
    pod_spec=V1PodSpec(
        service_account_name="etl-runner",
        init_containers=[
            V1Container(
                name="warm-cache",
                image="busybox:1.36",
                command=["sh", "-c", "echo warming cache && sleep 1"],
            ),
        ],
    ),
)

etl_env = flyte.TaskEnvironment(
    name="etl",
    image="registry.example.com/etl:2026.04.01",
    resources=flyte.Resources(cpu=(1, 4), memory="2Gi", gpu="T4:1"),
    env_vars={"LOG_LEVEL": "INFO"},
    secrets=[flyte.Secret(key="db-password", as_env_var="DB_PASSWORD")],
    pod_template=pod_template,
    interruptible=True,
)


@etl_env.task(retries=3, timeout=timedelta(minutes=30))
async def load_warehouse(ds: str) -> int:
    ...
```

You don't have to list the primary container in the pod_spec — Flyte fills it in from the env's image, the function's command, and the decorator's resources. Add a `V1Container(name="primary", ...)` entry only when you need to put fields on it directly (volume mounts, extra env, security context).

**Example pair:** [`examples/04_kubernetes_pod/`](https://github.com/unionai/airflow-examples/tree/main/guide/examples/04_kubernetes_pod)

Docs: [TaskEnvironment](../../core-concepts/task-environment) · [Secrets](../../task-configuration/secrets) · [PodTemplate / advanced k8s config](../../task-configuration/pod-templates)

---

## 8. Orchestration: parallelism, conditionals, error handling

Airflow encodes orchestration in first-class primitives — `[t1, t2, t3] >> merge` for fan-out, `.expand()` for dynamic mapping, `BranchPythonOperator` / `@task.branch` for branching, `ShortCircuitOperator` for early exit, `trigger_rule` for post-branch merges, and `on_failure_callback` / `trigger_rule=ALL_DONE` for failure paths.

In Flyte these are plain Python inside a driver task, because the driver runs at execution time. There is no static graph to encode into.

### Parallelism

Static fan-out in Airflow:

```python
fetch >> [summarize_us, summarize_eu, summarize_apac] >> merge
```

Flyte — concurrent awaits with `asyncio.gather`:

```python
@env.task
async def driver(ds: str) -> Summary:
    raw = await fetch(ds)
    us, eu, apac = await asyncio.gather(
        summarize(raw, "us"),
        summarize(raw, "eu"),
        summarize(raw, "apac"),
    )
    return await merge(us, eu, apac)
```

Each `summarize(...)` returns a coroutine; `asyncio.gather` runs them concurrently and awaits all of them. Tasks called concurrently run in their own pods — the concurrency is real, not just asyncio on one worker.

### Dynamic mapping

Airflow uses `.expand()` to fan out over values known only at runtime:

```python
process.partial(batch_size=100).expand(shard_id=list_shards())
```

Flyte — regular comprehension over the runtime list:

```python
shards = await list_shards()
results = await asyncio.gather(*(process(shard) for shard in shards))
```

To bound concurrency (for example, when the downstream is rate-limited), wrap the call in an `asyncio.Semaphore`:

```python
sem = asyncio.Semaphore(20)

async def process_one(shard):
    async with sem:
        return await process(shard)

results = await asyncio.gather(
    *(process_one(s) for s in shards),
    return_exceptions=True,
)
```

`return_exceptions=True` collects per-item failures instead of failing the batch. The semaphore is also the pattern when different tasks in the same fan-out need different concurrency limits.

If your codebase is sync, `flyte.map(process, shards, concurrency=20)` is the sync equivalent of the pattern above.

Docs: [Controlling parallelism](../../task-programming/controlling-parallelism) · [Fanout](../../task-programming/fanout)

### Conditionals

Airflow: `BranchPythonOperator` (or `@task.branch`) returns the task_id(s) to run next; `ShortCircuitOperator` skips the rest of the branch; a `trigger_rule=NONE_FAILED_MIN_ONE_SUCCESS` on the merge task reconciles skipped upstreams.

Flyte:

```python
@env.task
async def driver(ds: str) -> Summary:
    size = await inspect(ds)
    if size == 0:
        return Summary(status="empty")
    if size < 1_000_000:
        return await fast_path(ds)
    return await slow_path(ds)
```

Plain `if` / `elif` / `else`, plain `return`. There is no `trigger_rule` to set because there are no skipped tasks to reconcile — the code below the branch simply doesn't run.

### Error handling

Per-task retries and timeouts live on the `@env.task` decorator:

```python
@env.task(retries=3, timeout=timedelta(minutes=15))
async def flaky(ds: str) -> int:
    ...
```

Orchestration-level error handling — Airflow's `trigger_rule=ALL_DONE` cleanup and `on_failure_callback` alerts — is `try` / `except` / `finally` in the driver:

```python
@env.task
async def driver(ds: str) -> Summary:
    try:
        result = await heavy_step(ds)
        return await publish(result)
    except Exception as e:
        await alert(f"{ds} failed: {e}")
        raise
    finally:
        await cleanup(ds)
```

`finally` runs on both success and failure. `except` catches task failures at the `await` site after the task's own retries are exhausted. Specific failure modes live in `flyte.errors` — `OOMError`, `TaskTimeoutError`, `RetriesExhaustedError`, `ActionAbortedError` — and can be caught by type. A common pattern is retrying an OOM with larger resources via `.override(...)`:

```python
import flyte.errors

env = flyte.TaskEnvironment(
    name="transforms",
    image=...,
    resources=flyte.Resources(cpu=1, memory="250Mi"),
)

@env.task
async def transform(ds: str) -> int:
    ...

@env.task
async def driver(ds: str) -> int:
    try:
        return await transform(ds)
    except flyte.errors.OOMError:
        return await transform.override(
            resources=flyte.Resources(cpu=1, memory="2Gi"),
        )(ds)
```

Docs: [Retries and timeouts](../../task-configuration/retries-and-timeouts) · [Error handling](../../task-programming/error-handling)

**Example pair:** [`examples/05_orchestration/`](https://github.com/unionai/airflow-examples/tree/main/guide/examples/05_orchestration)

---

## What's next

Once the port is in place, a few Flyte features don't have direct Airflow counterparts and are worth knowing about.

### Caching

A task can be marked cacheable; subsequent calls with the same inputs short-circuit to the previous output instead of re-running. The cache key is derived from inputs and a task version, so bumping the version invalidates.

```python
@env.task(cache="auto")
async def expensive(ds: str) -> Result:
    ...
```

Airflow has no equivalent — XCom stores outputs but doesn't short-circuit on re-execution.

Docs: [Caching](../../task-configuration/caching)

### Reusable containers

By default each task call gets a fresh pod. A reuse policy keeps the container warm across calls so follow-up invocations skip pod startup and image pull.

```python
warm_env = flyte.TaskEnvironment(
    name="warm",
    image=...,
    reusable=flyte.ReusePolicy(replicas=(1, 3), concurrency=2),
)
```

Useful when a fan-out issues many short tasks against a heavy image.

Docs: [Reusable containers](../../task-configuration/reusable-containers)

### Reports

A task can emit an HTML report — tables, plots, logs — attached to the run and viewable in the UI. Written from inside the task with `flyte.report`.

```python
@env.task(report=True)
async def summarize(ds: str) -> Summary:
    tab = flyte.report.get_tab("main")
    tab.log(f"<h2>{ds}</h2>")
    tab.log(dataframe.to_html())
    await flyte.report.flush.aio()
    ...
```

Docs: [Reports](../../task-programming/reports)

### Apps

A long-running HTTP server (FastAPI, Panel, Streamlit, a webhook endpoint) can be deployed alongside your tasks. The app has a URL and can call tasks via the Flyte API. This is the path for webhook-triggered runs, a UI on top of a pipeline, or a custom inference endpoint.

Docs: [Serve and deploy apps](../../serve-and-deploy-apps/_index) · [Build apps](../../build-apps/_index)
