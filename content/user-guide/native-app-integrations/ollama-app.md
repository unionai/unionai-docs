---
title: Ollama app
weight: 13
variants: +flyte +union
---

# Ollama app

[Ollama](https://ollama.com/) is a lightweight runtime for serving open large language models (LLMs) locally, with a built-in OpenAI-compatible API. It is a good fit for smaller models and quick local-style serving, and complements the higher-throughput [vLLM](./vllm-app) and [SGLang](./sglang-app) integrations.

Unlike vLLM and SGLang, Ollama has no dedicated `*AppEnvironment` plugin. Instead, you serve it with the generic [`AppEnvironment`](../build-apps/single-script-apps): an image that installs Ollama plus a small entrypoint that launches `ollama serve` and pulls the model on startup.

## Installation

Ollama needs no Flyte plugin — it is installed into the app image. Start from the default Flyte base image and add the Ollama binary with a build command:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/basic_ollama.py" fragment=ollama-image lang=python >}}

The `install.sh` script drops the `ollama` binary into `/usr/local/bin`; no systemd service is needed inside a container.

## Basic Ollama app

Define the app with a GPU-backed `AppEnvironment`. The `args` run the script's `--server` entrypoint, which starts Ollama and pulls the model:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/basic_ollama.py" fragment=ollama-app lang=python >}}

The `--server` entrypoint binds Ollama to the app port, waits for it to be ready, and pulls the model so the OpenAI-compatible endpoint can serve it:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/basic_ollama.py" fragment=server lang=python >}}

Deploy it with `flyte.serve`:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/basic_ollama.py" fragment=deploy lang=python >}}

## Choosing a model

`MODEL` can be any tag from the [Ollama library](https://ollama.com/library) — for example `qwen3:0.6b`, `llama3.2:1b`, or `gemma3:1b`. Larger models need more GPU memory and disk; size the `resources` accordingly.

> [!NOTE]
> Small models run comfortably on CPU. To run without a GPU, drop the `gpu` field from `resources`. A GPU is recommended for larger models or higher throughput.

## Using the OpenAI-compatible API

Once deployed, the Ollama app exposes an OpenAI-compatible API. Call it exactly like the vLLM or SGLang apps:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://your-app-url/v1",  # Ollama endpoint
    api_key="ollama",  # Ollama ignores the key; any non-empty string works
)

response = client.chat.completions.create(
    model="qwen3:0.6b",  # Your MODEL tag
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ],
)

print(response.choices[0].message.content)
```

## Chat UI with Streamlit

To put a browser UI in front of the model, run Ollama internally and expose a [Streamlit](./streamlit-app) chat interface instead of the raw API. Only the Streamlit port is exposed; the browser talks to Streamlit, and Streamlit talks to Ollama over localhost:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/ollama_streamlit.py" fragment=app-env lang=python >}}

The UI is a standard Streamlit chat app that points its OpenAI client at the local Ollama server:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/ollama_streamlit.py" fragment=ui lang=python >}}

A helper starts Ollama in the background and pulls the model:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/ollama_streamlit.py" fragment=server lang=python >}}

The container entrypoint runs that helper, then hands the exposed port to Streamlit:

{{< code file="/unionai-examples/v2/user-guide/build-apps/ollama/ollama_streamlit.py" fragment=deploy lang=python >}}

## Authentication

The generic `AppEnvironment` uses Union's platform-level authentication. Leave `requires_auth=True` (the default) to require an authenticated caller, or set `requires_auth=False` for a public endpoint. Ollama has no built-in API-key argument of its own, so prefer platform auth over exposing a public endpoint. See [Secret-based authentication](../build-apps/secret-based-authentication) for injecting secrets into an app.

## Autoscaling

Ollama apps work well with scale-to-zero, so an idle model server costs nothing:

```python
app_env = flyte.app.AppEnvironment(
    name="autoscaling-ollama-app",
    image=image,
    args=["python", "basic_ollama.py", "--server"],
    port=8080,
    resources=flyte.Resources(cpu="4", memory="16Gi", gpu="L40s:1", disk="20Gi"),
    scaling=flyte.app.Scaling(
        replicas=(0, 1),  # Scale to zero when idle
        scaledown_after=600,  # 10 minutes idle before scaling down
    ),
    requires_auth=True,
)
```

Because the model is pulled at startup, a larger `scaledown_after` avoids re-pulling on every cold start.

## Best practices

1. **Right-size resources**: Match GPU memory and disk to the model. Small models run on CPU; drop the `gpu` field to save cost.
2. **Bake big models into the image**: For faster, more reproducible cold starts, `ollama pull` the model in a build command instead of at startup.
3. **Use scale-to-zero**: Set an appropriate `scaledown_after` to balance cost against cold-start latency.
4. **Prefer platform auth**: Ollama has no native API-key auth, so rely on `requires_auth` rather than exposing a public endpoint.
5. **Pick the right runtime**: Use Ollama for lightweight or local-style serving; reach for [vLLM](./vllm-app) or [SGLang](./sglang-app) for high-throughput production inference.

## Troubleshooting

**Model pull fails or times out:**

- Verify the `MODEL` tag exists in the [Ollama library](https://ollama.com/library)
- Increase `disk` in `resources` for larger models
- Review container logs for the `ollama pull` output

**Server not reachable:**

- Confirm Ollama is bound to `0.0.0.0` on the app port via `OLLAMA_HOST`
- Check that the app `port` matches the port Ollama serves on

**Slow first response:**

- The model is pulled on startup; use a larger `scaledown_after` or bake the model into the image
- Use a smaller model, or add a GPU for faster inference
