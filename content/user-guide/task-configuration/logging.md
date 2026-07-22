---
title: Logging
weight: 14
variants: +flyte +union
---

# Logging

Flyte uses two separate loggers, each with its own level:

- The **framework logger** (`flyte`): Flyte's own internal messages. Lines are prefixed with `[flyte]`. Defaults to `WARNING`.
- The **user logger** (`flyte.user`): the logger you get from `flyte.logger`, for your own application messages. Defaults to `INFO`.

Splitting the two lets you turn up Flyte's internal logging for debugging without flooding your output with framework noise during normal use, and vice versa.

## Set the logging level with environment variables

The quickest way to set the level is via environment variables. They apply to both local and remote runs.

| Variable | Controls | Default |
|----------|----------|---------|
| `LOG_LEVEL` | The framework logger (`flyte`) | `WARNING` |
| `USER_LOG_LEVEL` | The user logger (`flyte.user`) | `INFO` |
| `LOG_FORMAT` | Output format: `console` or `json` | `console` |
| `DISABLE_RICH_LOGGING` | If set (to any value), disables the Rich-formatted console handler | *unset* |
| `FLYTE_RESET_ROOT_LOGGER` | If set to `1`, resets the root logger so third-party library logs are captured as JSON too (see [JSON logging and third-party libraries](#json-logging-and-third-party-libraries)) | *unset* |

For example, to see Flyte's internal debug messages:

```bash
LOG_LEVEL=debug flyte run --local my_workflow.py main
```

Each level variable accepts either a **named level** (`critical`, `error`, `warning` or `warn`, `info`, `debug`, case-insensitive) or a **numeric** Python logging level, such as `10` (`DEBUG`) or `20` (`INFO`):

```bash
LOG_LEVEL=10 USER_LOG_LEVEL=debug flyte run --local my_workflow.py main
```

An unrecognized value falls back to the default for that variable.

## Set the framework verbosity from the CLI

The `flyte` CLI's `-v` flag is a shorthand for the **framework** log level (the `flyte` logger). It's a global option, so it goes *before* the subcommand, and repeating it raises the verbosity:

| Flag | Framework level |
|------|-----------------|
| *(none)* or `-v` | `WARNING` |
| `-vv` | `INFO` |
| `-vvv` | `DEBUG` |

```bash
flyte -vvv run --local my_workflow.py main
```

`-v` controls only the framework logger; it does **not** change your task (user) log level. Set that separately with `--user-log-level` (also a global option, so likewise before the subcommand), or the `USER_LOG_LEVEL` environment variable:

```bash
flyte --user-log-level debug run --local my_workflow.py main
```

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

## JSON logging and third-party libraries

Setting `LOG_FORMAT=json` (or `log_format="json"`) switches Flyte's output to JSON, but only for the two Flyte loggers, `flyte` and `flyte.user`. Both have propagation disabled, so neither reaches the Python **root logger**. Third-party libraries (`urllib3`, `boto3`, your own dependencies) typically emit through the root logger, so their lines are not converted to JSON: your Flyte output is JSON, but library log lines stay plain text.

This matters when you ship logs to a cloud logging backend (Google Cloud Logging (Stackdriver), AWS CloudWatch, Datadog) that expects one consistent JSON format across every line.

To make third-party lines JSON as well, also set `reset_root_logger=True`. Flyte then clears the root logger's existing handlers and attaches a JSON handler at the root, so every library that propagates to the root logger is captured as JSON:

```python
import flyte

flyte.with_runcontext(
    log_format="json",
    reset_root_logger=True,
).run(main)
```

By default (`reset_root_logger=False`), Flyte does **not** clear the root logger; it only wraps your existing root handlers so their lines carry the run/action context. The root reset is what makes third-party output uniform JSON.

`reset_root_logger` is also available on `flyte.init()`.

### Set it at registration with `FLYTE_RESET_ROOT_LOGGER`

Passing `reset_root_logger=True` to `flyte.with_runcontext()` automatically injects `FLYTE_RESET_ROOT_LOGGER=1` into the task container, so the reset happens in the remote task as well as locally.

To configure it on the task environment instead (resetting the root logger for every run, at registration time rather than per-run), set the environment variable directly. The value must be the string `1`:

```python
import flyte

env = flyte.TaskEnvironment(
    name="my_env",
    env_vars={
        "LOG_FORMAT": "json",
        "FLYTE_RESET_ROOT_LOGGER": "1",
    },
)
```

## Related

The same logging parameters can be set per-run via `flyte.with_runcontext()`. See the [Logging parameters](../task-deployment/run-context#logging) in the run context reference.
