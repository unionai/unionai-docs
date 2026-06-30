---
title: flyteplugins.union.ws_proxy
version: 0.4.3
variants: +flyte +union
layout: py_api
---

# flyteplugins.union.ws_proxy

Stdio <-> WebSocket proxy used as an ssh ``ProxyCommand`` for ssh-into-task.

The pod terminates the WebSocket and bridges it to its local sshd; this client
wraps the ssh stream in a standard WebSocket to the per-pod ``wss://`` route. We
ship it (rather than depending on ``websocat``) so ``flyte connect ssh`` works
with no extra install — it only needs ``aiohttp``, already a flyte dependency.

Installed as the ``flyte-ws-proxy`` console script. Usage (normally emitted into
~/.ssh/config by ``flyte connect ssh``):

    ProxyCommand flyte-ws-proxy <wss-url> --http-headers-file <file-with-Authorization-Bearer>
## Directory

### Methods

| Method | Description |
|-|-|
| [`main()`](#main) |  |


## Methods

#### main()

```python
def main()
```
