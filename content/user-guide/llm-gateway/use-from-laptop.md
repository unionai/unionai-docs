---
title: Use from your laptop
description: Reach the LLM Gateway from local tools, either through a public endpoint or behind Union sign-in with flyte proxy app.
icon: laptop
weight: 5
variants: -flyte +union
---

# Use from your laptop

Developers use the same gateway from their laptops as production does: notebooks, scripts, coding assistants, and any tool that accepts an OpenAI-compatible base URL. Local experiments then draw on the same budgets, appear in the same usage view, and pass through the same guardrails as production traffic.

How a laptop reaches the gateway depends on the gateway's access mode. See [Choose who can reach the gateway](./deploy-gateway#choose-who-can-reach-the-gateway).

| | Public endpoint | Behind Union sign-in |
|---|---|---|
| **Allow anonymous access** | Checked | Unchecked |
| Credentials a caller needs | A virtual key | A Union sign-in and a virtual key |
| Base URL on the laptop | The gateway's endpoint | `http://127.0.0.1:8600`, through `flyte proxy app` |
| If a virtual key leaks | Anyone on the internet can spend it, up to its budget, until you revoke it | It is useless without a Union sign-in |

## Public endpoint

When anonymous access is allowed, the gateway's endpoint is reachable from anywhere and the virtual key works like a provider API key. Configure any tool with the endpoint and the key:

```bash
export OPENAI_BASE_URL=https://<your-gateway-endpoint>/v1
export OPENAI_API_KEY=sk-un-...
```

```python
from openai import OpenAI

client = OpenAI()  # reads OPENAI_BASE_URL and OPENAI_API_KEY
response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[{"role": "user", "content": "Hello"}],
)
```

This mode is the simplest, and it suits tools that can only send an API key. The virtual key is the only thing standing between the internet and your spend. Give laptop keys small budgets and only the models they need, and revoke a key as soon as you suspect it leaked.

## Behind Union sign-in

When anonymous access is off, only callers signed in to Union reach the gateway. A standard OpenAI client can't do that on its own: it sends the virtual key in the `Authorization` header, which is the header Union sign-in uses.

`flyte proxy app` solves this. It opens a local port that forwards to the gateway, adding your Union credential to every request:

```bash
flyte proxy app --url https://<your-gateway-endpoint> --port 8600
```

You can also pass the gateway's app name instead of `--url`. The proxy runs in the foreground; stop it with Ctrl-C.

Then point any tool at the local port and keep using your virtual key as the API key:

```bash
export OPENAI_BASE_URL=http://127.0.0.1:8600/v1
export OPENAI_API_KEY=sk-un-...
```

```bash
curl http://127.0.0.1:8600/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/gpt-4.1-mini", "messages": [{"role": "user", "content": "Hello"}]}'
```

On each request, the proxy:

- moves an `Authorization: Bearer sk-un-...` virtual key into the header the gateway reads it from, so the key still identifies the caller and its budget applies,
- adds your Union credential, using the same sign-in as the `flyte` CLI, and
- refreshes the credential when it expires and retries the request once.

Responses stream back unchanged, so streaming completions work.

### Proxy options

| Option | Default | Meaning |
|---|---|---|
| `NAME` | | The gateway's app name. Use `--url` instead to give the endpoint directly. |
| `--url` | | The gateway's endpoint. |
| `--port` | `8600` | The local port. `0` picks a free one. |
| `--address` | `127.0.0.1` | The local address to listen on. |
| `--emit-mcp-config` | | Print an MCP client configuration that points at the local port. |
| `-v`, `--verbose` | | Log each request. Credentials are never logged. |

> [!WARNING] Keep the proxy on localhost
> Anyone who can reach the proxy's port uses the gateway with your Union identity. Leave `--address` at `127.0.0.1` unless you mean to share it, and the proxy warns if you bind it to any other address.

See the [`flyte proxy app` reference](../../api-reference/flyte-cli#flyte-proxy-app) for every option.
