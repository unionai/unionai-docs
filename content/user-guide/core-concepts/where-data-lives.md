---
title: Where your data lives
weight: 4
variants: +flyte +union
description: A developer's map of what Flyte stores in the control plane database versus the data plane object store, and what "metadata," "literals," and "raw data" actually mean.
---

# Where your data lives

When you run a Flyte task, your data ends up in two stores: a **database** in the control plane and an **object-store bucket** in the data plane.

## The two stores

| | Control plane database | Data plane object store |
|---|---|---|
| **Backing tech** | Postgres (plus a few internal coordination stores) | S3, GCS, or ABS bucket |
| **What's in it** | Every record Flyte uses to *describe* your runs, plus pointers to where each run's inputs and outputs live | Every run's inputs and outputs, and all bulk/offloaded content |
| **Lifetime** | Durable; long-lived history | Durable, but you can apply lifecycle/retention rules |

{{< variant union >}}
{{< markdown >}}
## Who manages the stores

* The control plane database (being part of the control plane) is always managed by Union.ai, regardless of whether you are using a BYOC or self-managed deployment.

* The data plane bucket lives in your cloud account. In a BYOC deployment, it is managed by Union.ai (as is the entire data plane). In a self-managed deployment, you manage the bucket yourself.
{{< /markdown >}}
{{< /variant >}}

The database is the **source of truth for what executed**. The bucket is **where your runs' actual input and output values live**.

## What goes in the database

The control plane database holds everything Flyte needs to enumerate, schedule, and replay your work. Specifically:

- **Registrations** — every task you've deployed, every trigger you've registered, every project and domain. A task's definition includes its *default* input values, which are stored inline as part of the registration.
- **Execution records** — every run, every action (task / trace / condition) inside that run, attempts, phases, timing, error messages, parent/child relationships.
- **Schedules and triggers** — `Cron`, event triggers, and their revision history.
- **Pointers to runtime inputs and outputs** — the database stores the *URI* of each run's `inputs.pb` / `outputs.pb`, not the values themselves. (One exception: an awaited *condition* / approval action stores the value that satisfies it inline.)
- **Caches** — the cache key → output-URI mapping for `@env.task(cache=...)`.

The values your tasks actually pass at runtime — even a bare `int` — do **not** live in the database. They are written to `inputs.pb` / `outputs.pb` in the bucket, and the database keeps only the pointer. See the next section.

(Internally, Flyte uses several backing databases — Postgres for registrations and run history, separate stores for in-flight action coordination and caches. For developer purposes the only thing that matters is that they're all small-record, structured stores; none of them hold bulk content.)

## What goes in the bucket

Every run's inputs and outputs are written to the bucket as `inputs.pb` / `outputs.pb`, and the database stores a **pointer** (URI) to them. Within those files, small scalar values are inlined directly while large values are offloaded to separate objects and referenced by URI. The bucket holds:

- **Task inputs**, serialized as `inputs.pb` per run.
- **Task outputs**, serialized as `outputs.pb` per attempt.
- **Offloaded values** — `flyte.io.File`, `flyte.io.Dir`, `flyte.io.DataFrame`, pickled objects, models, anything large.
- **Decks** — the HTML reports your task renders.
- **Trace checkpoints** — used by `@flyte.trace` to resume partial work.
- **Fast-registered code bundles** — what `flyte deploy` and `flyte run --copy-style all` upload so the cluster can run your local Python.
- **Image-build contexts** — when {{< key product_name >}} builds a container image from an `Image` definition that requires a build context.

The layout under your bucket is `<project>/<domain>/...`, with the bulk of execution artifacts under per-run, per-action subprefixes (`<run-name>/<action>/...` for outputs / Decks / checkpoints) and sibling prefixes for offloaded inputs and SDK uploads (code bundles, image-build contexts). You don't typically need to know the exact paths; you do need to know that **everything above lives behind one configured bucket prefix**.

## What "literal" and "raw data" mean

Every value a task takes in or returns is, in Flyte's data model, a **literal** — a typed, serialized representation of that value. Literals are how data flows between tasks, and each one is stored in one of two ways:

- **Inline** — small values (primitives like `int` / `float` / `str` / `bool`, collections, and JSON-serializable dataclasses and Pydantic models) are serialized *by value* directly into the run's `inputs.pb` / `outputs.pb`.
- **By reference** — large values (`flyte.io.File`, `flyte.io.Dir`, `flyte.io.DataFrame`, large model objects, larger pickled objects) are offloaded to their own objects in the bucket; the literal recorded in `inputs.pb` / `outputs.pb` then holds only a *URI pointer* to them.

**Raw data** is that offloaded content itself — the file, directory, DataFrame, or model bytes a by-reference literal points at, plus other offloaded artifacts such as checkpoints. It's exactly the offloaded values listed under [What goes in the bucket](#what-goes-in-the-bucket) above, and it's what `raw_data_path` (below) relocates. Because it's carried as a URI rather than copied inline, raw data is often described as being "passed by reference" (as opposed to inline literals, which are "passed by value").

(In the deployment and architecture guides you may also see execution data split into *literal data* and *raw data*. There, *literal data* means specifically the inline values above and *raw data* the offloaded ones — the same distinction, named as two categories.)

In short: every input and output is a **literal**; a literal is stored either **inline** (the value lives in `inputs.pb` / `outputs.pb`) or **by reference** to **raw data** offloaded elsewhere in the bucket.

## What "metadata" means

The word "metadata" appears in several places and means a different thing each time. The two senses that matter for developers:

### 1. "Metadata" as in the control plane database (Flyte's usage)

When Flyte documentation says **"metadata is preserved"** or **"metadata lives in the control plane,"** it means the database records above: registrations (including task default values), run history, and status. It does **not** mean "the contents of the bucket."

This is the sense most relevant to you: the database is durable, and losing the bucket does not lose your execution history — it loses the *large values* those history records pointed at.

### 2. "Metadata bucket" (a deployment/ops term you may see)

The Helm chart and some operational guides refer to a **"metadata bucket"** or `metadataContainer`. **This is a legacy name.** The bucket it refers to does *not* hold the database-style metadata above — it holds `inputs.pb`, `outputs.pb`, Decks, checkpoints, code bundles, and offloaded data. In other words, it holds exactly the "bucket" contents listed in the previous section.

If you see "metadata bucket" in an ops context, read it as **"the data plane object-store bucket."** The naming is unfortunate; the contents are what you'd expect from a data bucket.

You can largely ignore other appearances of the word in API surfaces (`TaskMetadata`, `ActionMetadata`, and `metadata_path` on `RunContext`, which is a local scratch directory used only by `from_local()` execution) — those are small property bags or local scratch paths and don't change where your data is stored.

## Per-run customization: `raw_data_path`

By default, offloaded values (`File`, `Dir`, `DataFrame`, checkpoints) land alongside everything else under the deployment's configured bucket prefix. You can route them to a different prefix — including a different bucket entirely — for a single run:

```python
import flyte

flyte.init_from_config()

run = flyte.with_runcontext(
    raw_data_path="s3://my-other-bucket/some/prefix",
).run(my_task, x=1)
```

This is the supported way to send a sensitive run to an isolated bucket, point at a bucket with different lifecycle rules, or otherwise route offloaded data per run. The `inputs.pb` / `outputs.pb` themselves still land in the deployment's bucket; only the *raw* offloaded contents move.

See [Run context](../task-deployment/run-context) for the full set of `with_runcontext` options.

## What happens if the bucket is purged

If a retention rule deletes objects out of the bucket, the database records that pointed at them are **not** deleted — but their pointers now dangle. Concretely:

- Execution history, status, timing, structure: **still visible** in the UI. They come from the database.
- Input/output **previews, Deck views, artifact payloads**: show "not found" if the underlying bytes were purged.
- **Cache hits** for purged outputs: the cached pointer is dead, the task re-executes.
- **Trace resumption**: not possible if the checkpoint blob is gone.
- **Re-running an old execution**: fails if any input it needs has been purged.

This is the trade-off behind retention policies: you save storage cost at the price of being able to inspect or re-run old executions whose offloaded values have aged out. New executions are unaffected.

Lifecycle / retention rules should be scoped to the offloaded-data prefixes, **not** applied bucket-wide — `inputs.pb` and `outputs.pb` are needed for in-flight executions to complete, so purging them mid-run breaks things.

{{< variant union >}}
{{< markdown >}}
For how retention policies are configured in your deployment, see [BYOC data retention policy](../../deployment/byoc/data-retention-policy) or [Self-managed data retention](../../deployment/selfmanaged/configuration/data-retention).
{{< /markdown >}}
{{< /variant >}}

## The short version

- **Database** = the system of record. Holds registrations (including task default values), run history, schedules, and pointers to each run's inputs/outputs.
- **Bucket** = the object-store bucket. Holds every run's `inputs.pb`/`outputs.pb`, Decks, checkpoints, code bundles, and offloaded `File` / `Dir` / `DataFrame` contents.
- **Values** = every task input/output is a **literal**, stored either *inline* in `inputs.pb`/`outputs.pb` or *by reference* to **raw data** offloaded in the bucket.
- **"Metadata" in docs** usually means database-side records. **"Metadata bucket" in Helm/ops** is legacy naming for the data plane bucket — it does *not* hold database metadata.
- **`flyte.with_runcontext(raw_data_path=...)`** is your knob to send offloaded data elsewhere per run.
