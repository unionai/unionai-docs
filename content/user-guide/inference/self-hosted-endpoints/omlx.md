---
title: oMLX
description: Serve MLX models on a Mac's Apple Silicon GPU from a devbox with oMLX's OpenAI-compatible API.
icon: cpu
weight: 5
variants: +flyte +union
---

# oMLX

The `flyteplugins-omlx` plugin serves LLMs with [oMLX](https://github.com/jundot/omlx), an OpenAI-compatible inference server built on Apple's MLX framework. `OMLXAppEnvironment` runs `omlx serve` as a Flyte app on the Mac's Apple Silicon GPU, through a [devbox started with `--apple-silicon`](../../get-started/run-modes/running-devbox#using-the-apple-silicon-gpu).

Use it to serve a model locally on a Mac. oMLX runs only on macOS with Apple Silicon, so an oMLX endpoint can't run in a Linux container or on a remote cluster. To serve a model on a cluster, use [vLLM](./vllm), [SGLang](./sglang), [Ollama](./ollama), or [llama.cpp](./llamacpp).

## Installation

On the Mac:

1. Install oMLX by following the [oMLX installation guide](https://github.com/jundot/omlx#installation). oMLX isn't published to PyPI.
2. Install the plugin with `pip install flyteplugins-omlx`.
3. Start a devbox with `flyte start devbox --apple-silicon`. For its requirements, see [Using the Apple Silicon GPU](../../get-started/run-modes/running-devbox#using-the-apple-silicon-gpu).

The app finds an `omlx` binary on its `PATH`, in `/opt/homebrew/bin`, or in `/usr/local/bin`. If it finds none, the server exits with code 127 and prints that oMLX is not installed, with the install commands.

## Basic oMLX endpoint

Define the app by importing `OMLXAppEnvironment` from `flyteplugins.omlx` and creating one with a `name`, for example `OMLXAppEnvironment(name="omlx-local")`. With no other settings, it:

- Requests `gpu="AppleSilicon"`, so the app runs natively on the Mac.
- Runs `omlx serve --host 127.0.0.1 --port 8000`.
- Uses a default image with `flyteplugins-omlx` installed. oMLX itself isn't in the image.
- Adds an **oMLX Models** link to the app, pointing at `/v1/models`.

To serve it, point the `flyte` CLI at the devbox with `flyte create config --devbox`. Then, in a script, call `flyte.init_from_config()` and pass the environment to `flyte.serve()`. The returned app's `url` is the endpoint's address. This is how the plugin's own example, `examples/accelerators/omlx_serve.py` in [flyte-sdk](https://github.com/flyteorg/flyte-sdk), serves it.

oMLX serves the MLX-format models in its model directory. Without `model_dir`, the plugin passes no `--model-dir`, and oMLX uses its own default, which the plugin's documentation gives as `~/.omlx/models`. See the [oMLX documentation](https://github.com/jundot/omlx) for where your oMLX version looks.

## Configuration

| Field | Description |
|---|---|
| `port` | Port oMLX listens on. Default `8000`. |
| `model_dir` | Directory of MLX models on the Mac, passed as `--model-dir`. Use an absolute path. |
| `model_id` | A name for the model, stored on the environment. It doesn't change which models oMLX serves. |
| `api_key` | Key oMLX requires from callers, passed as `--api-key`. |
| `extra_args` | More `omlx serve` flags, as a string or a list. See `omlx serve --help`. |
| `resources` | Defaults to `gpu="AppleSilicon"`. If you set `resources` without a GPU, the plugin adds `gpu="AppleSilicon"`. |
| `image` | The pip packages installed into the environment the app runs in. Override it only to add packages. |

Values with spaces are quoted for you. An argument of the form `$MY_VAR` isn't quoted.

To accept connections on another interface, pass `--host` in `extra_args`. It replaces the default `--host 127.0.0.1`.

## Call the endpoint

oMLX's API is OpenAI-compatible. The plugin's documentation points OpenAI clients at the app's URL with `/v1` appended, and lists the model ids to pass as `model` at `/v1/models`, which the **oMLX Models** link opens. See the [oMLX documentation](https://github.com/jundot/omlx) for the routes your oMLX version serves.

If you set `api_key`, oMLX requires that key, so pass it as the client's `api_key`. `OMLXAppEnvironment` also keeps the app default `requires_auth=True`, so where the app's URL enforces Flyte auth, a caller needs Flyte credentials too. Set `requires_auth=False` to serve the endpoint without Flyte auth.

## Limitations

- `OMLXAppEnvironment` sets its own command. Passing `args` raises a `ValueError`, so use `extra_args` instead.
- Requesting any accelerator other than Apple Silicon, such as `gpu="L4:1"`, raises a `ValueError`.
- An app that requests Apple Silicon runs only on a devbox started with `--apple-silicon`. For what happens elsewhere, see [Using the Apple Silicon GPU](../../get-started/run-modes/running-devbox#using-the-apple-silicon-gpu).

## API reference

See the [oMLX API reference](../../../api-reference/integrations/omlx/_index).
