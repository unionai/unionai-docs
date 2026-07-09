---
title: Build a custom CLI
weight: 5
variants: +flyte +union
---

# Build a custom CLI

The built-in `flyte run` command (see [Run command options](./run-command-options))
turns your task's parameters into `--<input_name>` options automatically. That's
the fastest way to run a task from the command line, but it gives you the CLI
that Flyte generates.

When you want your **own** command-line interface — custom argument names, grouped
options, subcommands, config files, `--help` text you control — build it with an
argument-parsing library of your choice and hand the parsed values to
`flyte.run()`. Because `flyte.run()` is an ordinary Python function, any parser
works: [`tyro`](https://brentyi.github.io/tyro/), `argparse`, `click`, or `hydra`.

## The pattern

A custom CLI wrapper is three steps:

1. **Parse the command line** into a config object (a dataclass, a Pydantic model,
   or plain arguments) with the parser of your choice.
2. **Initialize Flyte** with `flyte.init_from_config()`.
3. **Run the task** with `flyte.run()`, passing the parsed config as the task's
   input.

## Example: a typed CLI with `tyro`

[`tyro`](https://brentyi.github.io/tyro/) generates a fully-typed CLI directly
from a dataclass, so you describe your parameters once and get parsing,
validation, and `--help` for free.

```python
# /// script
# dependencies = [
#    "tyro",
#    "flyte",
# ]
# ///

from dataclasses import dataclass

import tyro

import flyte

env = flyte.TaskEnvironment(
    name="custom_cli",
    image=flyte.Image.from_uv_script(__file__, name="flyte"),
)


@dataclass
class Config:
    foo: int
    bar: str = "default"


@env.task
async def main(config: Config):
    print(f"foo: {config.foo}, bar: {config.bar}")


if __name__ == "__main__":
    # Generate a CLI and instantiate `Config` with its two arguments: `foo` and `bar`.
    config = tyro.cli(Config)

    flyte.init_from_config()
    r = flyte.run(main, config)
    print(r.url)
```

Run it like any script — `tyro` exposes `foo` and `bar` as CLI options and prints
`--help` for you:

```bash
$ uv run custom_cli.py --foo 42 --bar hello
```

Here `tyro.cli(Config)` does the parsing, `flyte.init_from_config()` loads your
`config.yaml` (endpoint, project, domain, and so on), and
`flyte.run(main, config)` deploys and runs the task with the parsed config as its
input. The `config` object is passed **positionally** to `main`, mapping to its
`config` parameter — the same positional form documented in
[Run command options](./run-command-options).

## Using a different parser

The pattern is identical whichever library you reach for — only step 1 changes.
With the standard library's `argparse`:

```python
import argparse

import flyte

env = flyte.TaskEnvironment(name="custom_cli")


@env.task
async def main(foo: int, bar: str = "default"):
    print(f"foo: {foo}, bar: {bar}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--foo", type=int, required=True)
    parser.add_argument("--bar", default="default")
    args = parser.parse_args()

    flyte.init_from_config()
    r = flyte.run(main, foo=args.foo, bar=args.bar)
    print(r.url)
```

Swap `argparse` for `click` or `hydra` the same way: parse however you like, then
call `flyte.run()` with the resulting values (positionally or by keyword). This is
also the entry point for richer CLIs — subcommands that each run a different task,
`hydra` config composition, environment-driven defaults, and so on.

## When to use which

- **Reach for the built-in `flyte run`** when you just need to run a task from the
  command line and Flyte's generated `--<input_name>` options are enough. See
  [Run command options](./run-command-options).
- **Build a custom CLI** when you need control over the interface itself — your own
  option names, subcommands, config-file loading, or help text — or when the CLI is
  a first-class part of a tool you're shipping.

For configuring the run itself (storage, caching, identity, logging) rather than the
task's inputs, see [Run context](./run-context).
