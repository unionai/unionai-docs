---
title: TaskPlugins
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# TaskPlugins

**Package:** `flytekit.core.task`

This is the TaskPlugins factory for task types that are derivative of PythonFunctionTask.
Every task that the user wishes to use should be available in this factory.
Usage

```python
TaskPlugins.register_pythontask_plugin(config_object_type, plugin_object_type)
# config_object_type is any class that will be passed to the plugin_object as task_config
# Plugin_object_type is a derivative of ``PythonFunctionTask``
```
Examples of available task plugins include different query-based plugins such as
{{< py_class_ref flytekitplugins.athena.task.AthenaTask >}} and {{< py_class_ref flytekitplugins.hive.task.HiveTask >}}, kubeflow
operators like {{< py_class_ref plugins.kfpytorch.flytekitplugins.kfpytorch.task.PyTorchFunctionTask >}} and
{{< py_class_ref plugins.kftensorflow.flytekitplugins.kftensorflow.task.TensorflowFunctionTask >}}, and generic plugins like
{{< py_class_ref flytekitplugins.pod.task.PodFunctionTask >}} which doesn't integrate with third party tools or services.

The `task_config` is different for every task plugin type. This is filled out by users when they define a task to
specify plugin-specific behavior and features.  For example, with a query type task plugin, the config might store
information related to which database to query.

The `plugin_object_type` can be used to customize execution behavior and task serialization properties in tandem
with the `task_config`.


## Methods

| Method | Description |
|-|-|
| [`find_pythontask_plugin()`](#find_pythontask_plugin) | Returns a PluginObjectType if found or returns the base PythonFunctionTask. |
| [`register_pythontask_plugin()`](#register_pythontask_plugin) | Use this method to register a new plugin into Flytekit. |


### find_pythontask_plugin()

```python
def find_pythontask_plugin(
    plugin_config_type: type,
) -> Type[PythonFunctionTask]
```
Returns a PluginObjectType if found or returns the base PythonFunctionTask


| Parameter | Type | Description |
|-|-|-|
| `plugin_config_type` | `type` | |

### register_pythontask_plugin()

```python
def register_pythontask_plugin(
    plugin_config_type: type,
    plugin: Type[PythonFunctionTask],
)
```
Use this method to register a new plugin into Flytekit. Usage ::

```python
TaskPlugins.register_pythontask_plugin(config_object_type, plugin_object_type)
# config_object_type is any class that will be passed to the plugin_object as task_config
# Plugin_object_type is a derivative of ``PythonFunctionTask``
```


| Parameter | Type | Description |
|-|-|-|
| `plugin_config_type` | `type` | |
| `plugin` | `Type[PythonFunctionTask]` | |

