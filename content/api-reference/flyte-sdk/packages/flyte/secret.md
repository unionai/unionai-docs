---
title: Secret
version: 2.0.0
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Secret

**Package:** `flyte`

Secrets are used to inject sensitive information into tasks or image build context.
Secrets can be mounted as environment variables or files.
 The secret key is the name of the secret in the secret store. The group is optional and maybe used with some
secret stores to organize secrets. The as_env_var is an optional parameter that can be used to specify the
name of the environment variable that the secret should be mounted as.

Example:
```python
@task(secrets="my-secret")
async def my_task():
    # This will be set to the value of the secret. Note: The env var is always uppercase, and - is replaced with _.
    os.environ["MY_SECRET"]

@task(secrets=Secret("my-openai-api-key", as_env_var="OPENAI_API_KEY"))
async def my_task2():
    os.environ["OPENAI_API_KEY"]
```

TODO: Add support for secret versioning (some stores) and secret groups (some stores) and mounting as files.



```python
class Secret(
    key: str,
    group: typing.Optional[str],
    mount: pathlib._local.Path | None,
    as_env_var: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | The name of the secret in the secret store. |
| `group` | `typing.Optional[str]` | The group of the secret in the secret store. |
| `mount` | `pathlib._local.Path \| None` | For now, the only supported mount path is "/etc/flyte/secrets". TODO: support arbitrary mount paths. Today only "/etc/flyte/secrets" is supported |
| `as_env_var` | `typing.Optional[str]` | The name of the environment variable that the secret should be mounted as. |

## Methods

| Method | Description |
|-|-|
| [`stable_hash()`](#stable_hash) | Deterministic, process-independent hash (as hex string). |


### stable_hash()

```python
def stable_hash()
```
Deterministic, process-independent hash (as hex string).


