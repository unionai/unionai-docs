---
title: ConfigFile
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# ConfigFile

**Package:** `flytekit.configuration`

```python
def ConfigFile(
    location: str,
):
```
Load the config from this location


| Parameter | Type |
|-|-|
| `location` | `str` |
## Methods

### get()

```python
def get(
    c: typing.Union[LegacyConfigEntry, YamlConfigEntry],
):
```
| Parameter | Type |
|-|-|
| `c` | `typing.Union[LegacyConfigEntry, YamlConfigEntry]` |
