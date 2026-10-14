---
title: Telemetry
weight: 8
variants: -flyte +union
description: Turn off the web console's analytics and the Flyte SDK's telemetry with telemetry.enabled.
---

# Telemetry

A self-hosted deployment sends telemetry from two places:

| Source | What it sends |
|---|---|
| Web console | Product analytics through Google Tag Manager, and error and performance monitoring through Grafana Faro. |
| `flyte` SDK in task pods | Crash reports for unexpected errors, and counts of runs, deploys, and their outcomes. Errors caused by user code or input are not reported. |

Both honor the [`DO_NOT_TRACK`](https://donottrack.sh) environment variable. Set `telemetry.enabled` to `false` in each chart to set it for you.

## Turn off telemetry in the web console

In the `controlplane` chart values:

```yaml
telemetry:
  enabled: false
```

This sets `DO_NOT_TRACK=1` on the console, which then loads neither Google Tag Manager nor Grafana Faro. The console reads it at request time, so you don't need to rebuild the image.

## Turn off telemetry in task pods

In the `dataplane` chart values of each data plane:

```yaml
telemetry:
  enabled: false
```

The data plane then adds `DO_NOT_TRACK=1` to every task pod. `DO_NOT_TRACK` is a cross-tool convention, so it also turns off telemetry in other tools in your task images that honor it.

## Turn off telemetry on developer machines

The `flyte` CLI and SDK read the same variable:

```bash
export DO_NOT_TRACK=1
```

To turn off telemetry for {{< key product_name >}} only, set `FLYTE_DISABLE_TELEMETRY=true` instead. Values `1`, `true`, and `yes` (in any case) turn telemetry off. Any other value, or no value, leaves it on.
