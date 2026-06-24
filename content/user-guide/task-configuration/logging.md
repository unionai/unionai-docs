---
title: Logging
weight: 14
variants: +flyte +union
---

# Logging

Flyte uses two separate loggers, each with its own level:

- The **framework logger** (`flyte`) — Flyte's own internal messages. Lines are prefixed with `[flyte]`. Defaults to `WARNING`.
- The **user logger** (`flyte.user`) — the logger you get from `flyte.logger`, for your own application messages. Defaults to `INFO`.

Splitting the two lets you turn up Flyte's internal logging for debugging without flooding your output with framework noise during normal use, and vice versa.

## Set the logging level with environment variables

The quickest way to set the level is via environment variables. They apply to both local and remote runs.

| Variable | Controls | Default |
|----------|----------|---------|
| `LOG_LEVEL` | The framework logger (`flyte`) | `WARNING` |
| `USER_LOG_LEVEL` | The user logger (`flyte.user`) | `INFO` |
| `LOG_FORMAT` | Output format: `console` or `json` | `console` |
| `DISABLE_RICH_LOGGING` | If set (to any value), disables the Rich-formatted console handler | *unset* |

For example, to see Flyte's internal debug messages:

```bash
LOG_LEVEL=debug python my_workflow.py
```

Each level variable accepts either a **named level** — `critical`, `error`, `warning` (or `warn`), `info`, `debug` (case-insensitive) — or a **numeric** Python logging level, such as `10` (`DEBUG`) or `20` (`INFO`):

```bash
LOG_LEVEL=10 USER_LOG_LEVEL=debug python my_workflow.py
```

An unrecognized value falls back to the default for that variable.

## Set the logging level with `flyte.init()`

You can also set logging when you initialize the SDK. The `log_level` and `user_log_level` parameters take numeric Python logging levels:

```python
import logging
import flyte

flyte.init(
    log_level=logging.DEBUG,        # framework logger
    user_log_level=logging.INFO,    # user logger
    log_format="console",           # or "json"
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `log_level` | `int` | `LOG_LEVEL` env var, else `WARNING` | Level for the framework logger (`flyte`). |
| `user_log_level` | `int` | `USER_LOG_LEVEL` env var, else `INFO` | Level for the user logger (`flyte.user`). |
| `log_format` | `"console"` \| `"json"` | `LOG_FORMAT` env var, else `"console"` | Output format. |
| `reset_root_logger` | `bool` | `False` | When `True`, Flyte clears the root logger's existing handlers and installs its own. When `False` (the default), Flyte leaves your existing root handlers in place and wraps their formatters so third-party log lines also carry the run/action context. |

> [!NOTE]
> Explicit `flyte.init()` arguments take precedence over the environment variables. An argument left unset falls back to the corresponding environment variable, then to the built-in default.

## Write to the user logger

Use `flyte.logger` for your own application messages so they render with the same run/action context as Flyte's output:

```python
import flyte

flyte.logger.info("Processing %d records", len(records))
flyte.logger.debug("Intermediate value: %r", value)
```

## Related

The same logging parameters can be set per-run via `flyte.with_runcontext()`. See the [Logging parameters](../task-deployment/run-context#logging) in the run context reference.
