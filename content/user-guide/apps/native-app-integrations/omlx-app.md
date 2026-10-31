---
title: oMLX app
description: Serve LLMs on a Mac's Apple Silicon GPU with oMLX from an Apple Silicon devbox.
icon: cpu
weight: 14
variants: +flyte +union
---

# oMLX app

[oMLX](https://github.com/jundot/omlx) is an OpenAI-compatible inference server built on Apple's MLX framework. Flyte provides `OMLXAppEnvironment` for serving LLMs with oMLX on your Mac's Apple Silicon GPU.

oMLX runs only on macOS with Apple Silicon, so `OMLXAppEnvironment` runs only on a [devbox started with `--apple-silicon`](../../get-started/run-modes/running-devbox#using-the-apple-silicon-gpu). The devbox runs `omlx serve` natively on the Mac and forwards the app's URL, port and logs. The app can't run in a Linux container or on a remote cluster.

## Installation

Install oMLX on the Mac. It isn't published on PyPI; see the [oMLX install guide](https://github.com/jundot/omlx#installation). The plugin suggests Homebrew:

```bash
brew tap jundot/omlx https://github.com/jundot/omlx && brew install omlx
```

The app finds an `omlx` binary in `/opt/homebrew/bin` or `/usr/local/bin`. The app runs in a separate Python environment on the Mac, built from the image's pip packages, so an oMLX installed with `pip` into another Python on the Mac isn't found.

Then install the plugin:

```bash
pip install flyteplugins-omlx
```

Start an Apple Silicon devbox and point your configuration at it:

```bash
flyte start devbox --apple-silicon
flyte create config --devbox
```

See [Using the Apple Silicon GPU](../../get-started/run-modes/running-devbox#using-the-apple-silicon-gpu) for the devbox's requirements.

## Basic oMLX app

oMLX serves each model subdirectory under `~/.omlx/models` by default:

```python
import flyte
from flyteplugins.omlx import OMLXAppEnvironment

omlx_app = OMLXAppEnvironment(
    name="omlx-local",
    extra_args="--log-level info",
)

if __name__ == "__main__":
    flyte.init_from_config()
    app = flyte.serve(omlx_app)
    print(app.url)
```

This runs `omlx serve --host 127.0.0.1 --port 8000 --log-level info` on the Mac. The app also gets an **oMLX Models** link to `/v1/models`. For a fuller example, see [`examples/accelerators/omlx_serve.py`](https://github.com/flyteorg/flyte-sdk/blob/main/examples/accelerators/omlx_serve.py) in the Flyte SDK repository.

## Configuration

| Parameter | Description |
|---|---|
| `name` | App name. |
| `port` | Port `omlx serve` listens on. Defaults to `8000`. |
| `model_dir` | Directory of MLX models on the Mac, passed as `--model-dir`. Use an absolute, expanded path. Each subdirectory is served as a model. |
| `model_id` | A friendly model id stored on the environment. It isn't passed to `omlx serve`. |
| `api_key` | Passed as `--api-key`, so it appears in the server's command line. For real secrets, use `secrets` and `env_vars`. |
| `extra_args` | Extra flags appended to `omlx serve`, as a string or a list. A `--host` here replaces the default `127.0.0.1`; a non-loopback host such as `0.0.0.0` exposes the server to your network. See `omlx serve --help`. |
| `image` | The image's pip packages are installed into the app's Python environment on the Mac. The image is still built as a container image, so its packages must also install on Linux. Defaults to an image with `flyteplugins-omlx`. |
| `resources` | Defaults to `gpu="AppleSilicon"`, which is added if you set resources without a GPU. |
| `env_vars` | Environment variables for the server process. |

`OMLXAppEnvironment` rejects two settings:

- A non-Apple Silicon GPU in `resources` raises `ValueError: OMLXAppEnvironment only runs on Apple Silicon (gpu='AppleSilicon') ...`.
- Setting `args` raises ``ValueError: args cannot be set for OMLXAppEnvironment. Use `extra_args` to add extra arguments.``

## Troubleshooting

**`[flyteplugins-omlx] oMLX is not installed on this machine.`**
The app couldn't find oMLX on the Mac and exited. Install oMLX as described in [Installation](#installation), then serve the app again.

**`APPLE_SILICON_NOT_AVAILABLE`**
The app isn't running on a devbox started with `--apple-silicon` (for example, a devbox started without the flag, or a remote cluster). Recreate the devbox with `flyte delete devbox && flyte start devbox --apple-silicon`. See [Using the Apple Silicon GPU](../../get-started/run-modes/running-devbox#using-the-apple-silicon-gpu).
