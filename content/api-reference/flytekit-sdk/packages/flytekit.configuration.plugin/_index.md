---
title: flytekit.configuration.plugin
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration.plugin

Defines a plugin API allowing other libraries to modify the behavior of flytekit.

Libraries can register by defining an object that follows the same API as FlytekitPlugin
and providing an entrypoint with the group name "flytekit.plugin". In `setuptools`,
you can specific them with:

```python
setup(entry_points={
    "flytekit.configuration.plugin": ["my_plugin=my_module:MyCustomPlugin"]
})
```

or in pyproject.toml:

```toml
[project.entry-points."flytekit.configuration.plugin"]
my_plugin = "my_module:MyCustomPlugin"
```

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytekitPlugin`](../flytekit.configuration.plugin/flytekitplugin) |  |

### Protocols

| Protocol | Description |
|-|-|
| [`FlytekitPluginProtocol`](../flytekit.configuration.plugin/flytekitpluginprotocol) |  |

### Methods

| Method | Description |
|-|-|
| [`get_plugin()`](#get_plugin) | Get current plugin. |


## Methods

#### get_plugin()

```python
def get_plugin()
```
Get current plugin


