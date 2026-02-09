---
title: ConnectorService
version: 2.0.0b55
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ConnectorService

**Package:** `flyte.connectors`

## Methods

| Method | Description |
|-|-|
| [`run()`](#run) |  |


### run()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ConnectorService.run.aio()`.
```python
def run(
    cls,
    port: int,
    prometheus_port: int,
    worker: int,
    timeout: int | None,
    modules: typing.Optional[typing.List[str]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `port` | `int` | |
| `prometheus_port` | `int` | |
| `worker` | `int` | |
| `timeout` | `int \| None` | |
| `modules` | `typing.Optional[typing.List[str]]` | |

