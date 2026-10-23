---
title: Telemetry
description: What telemetry is sent and how to turn it off with DO_NOT_TRACK.
icon: eye-slash
weight: 15
variants: +flyte -union
---

# Telemetry

Flyte sends telemetry to help find bugs and improve the product. To turn it off, set the [`DO_NOT_TRACK`](https://donottrack.sh) environment variable:

```bash
export DO_NOT_TRACK=1
```

The same variable turns off telemetry in the `flyte` SDK and CLI, the backend, and the web console.

## What is collected

| Source | What it sends |
|---|---|
| `flyte` SDK and CLI | Crash reports for unexpected errors, and counts of runs, deploys, and their outcomes. Errors caused by user code or input are not reported. |
| Flyte backend | Error reports for internal server errors, and counts of runs, task deploys, trigger deploys, and app deploys. |
| Web console | Product analytics through Google Tag Manager. |

## Turn off telemetry on your machine

Set `DO_NOT_TRACK=1` in the shell where you run `flyte`, or in your shell profile:

```bash
echo 'export DO_NOT_TRACK=1' >> ~/.bashrc
```

`DO_NOT_TRACK` is a cross-tool convention, so it also turns off telemetry in other tools that honor it. To turn off telemetry for Flyte only, set `FLYTE_DISABLE_TELEMETRY=true` instead.

Values `1`, `true`, and `yes` (in any case) turn telemetry off. Any other value, or no value, leaves it on.

## Turn off telemetry in tasks and apps

Tasks and apps run the SDK in their own containers, so they don't inherit the variable from your shell.

If the deployment has telemetry turned off (see [Turn off telemetry in a deployment](#turn-off-telemetry-in-a-deployment)), every task pod and app gets `DO_NOT_TRACK=1` automatically. A task's own environment cannot turn it back on.

To opt out a single environment instead, set the variable on it:

```python
import flyte

env = flyte.TaskEnvironment(
    name="training",
    env_vars={"DO_NOT_TRACK": "1"},
)
```

You can also set `ENV DO_NOT_TRACK=1` in the container image.

## Turn off telemetry in a deployment

Set `telemetry.enabled` to `false` in the `flyte-binary` or `flyte-core` Helm chart values:

```yaml
telemetry:
  enabled: false
```

This sets `DO_NOT_TRACK=1` on every backend component and on the web console. The backend then adds `DO_NOT_TRACK=1` to every task pod and app it creates.

For the Flyte Devbox chart, set `flyte-binary.telemetry.enabled` to `false`.

If you deploy without these charts, set `DO_NOT_TRACK=1` on the backend and console containers yourself. The console reads it at request time, so you don't need to rebuild the image.

## Variables reference

| Variable | Scope |
|---|---|
| `DO_NOT_TRACK=1` | Turns off Flyte telemetry and that of other tools that honor the convention. |
| `FLYTE_DISABLE_TELEMETRY=true` | Turns off Flyte telemetry only. |
| `FLYTE_DISABLE_SENTRY=true` | Older name for `FLYTE_DISABLE_TELEMETRY`, honored by the SDK and CLI and the backend. |
