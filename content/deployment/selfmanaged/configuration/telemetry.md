---
title: Telemetry
icon: eye-slash
weight: 10
variants: -flyte +union
description: Turn off the telemetry the Flyte SDK sends from your data plane with DO_NOT_TRACK.
---

# Telemetry

The `flyte` SDK sends crash reports for unexpected errors, and counts of runs, deploys, and their outcomes, to help find bugs. Errors caused by user code or input are not reported. To turn this off, set the [`DO_NOT_TRACK`](https://donottrack.sh) environment variable to `1`.

## Turn off telemetry in task pods

Set `telemetry.enabled` to `false` in the `dataplane` Helm chart values:

```yaml
telemetry:
  enabled: false
```

The data plane then adds `DO_NOT_TRACK=1` to every task pod.

`DO_NOT_TRACK` is a cross-tool convention, so it also turns off telemetry in other tools in your task images that honor it.

## Turn off telemetry for a single environment

To opt out one task environment without changing the chart, set the variable on it:

```python
import flyte

env = flyte.TaskEnvironment(
    name="training",
    env_vars={"DO_NOT_TRACK": "1"},
)
```

You can also set `ENV DO_NOT_TRACK=1` in the container image.

## Turn off telemetry on your machine

The `flyte` CLI and SDK on a developer's machine read the same variable:

```bash
export DO_NOT_TRACK=1
```

To turn off telemetry for {{< key product_name >}} only, set `FLYTE_DISABLE_TELEMETRY=true` instead. Values `1`, `true`, and `yes` (in any case) turn telemetry off. Any other value, or no value, leaves it on.
