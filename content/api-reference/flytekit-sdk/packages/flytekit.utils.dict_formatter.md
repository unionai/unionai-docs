---
title: flytekit.utils.dict_formatter
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.utils.dict_formatter

## Directory

### Methods

| Method | Description |
|-|-|
| [`format_dict()`](#format_dict) | Recursively update a dictionary with format strings with values from another dictionary where the keys match. |
| [`get_nested_value()`](#get_nested_value) | Retrieve the nested value from a dictionary based on a list of keys. |
| [`replace_placeholder()`](#replace_placeholder) | Replace a placeholder in the original string and handle the specific logic for the sagemaker service and idempotence token. |


## Methods

#### format_dict()

```python
def format_dict(
    service: str,
    original_dict: typing.Any,
    update_dict: typing.Dict[str, typing.Any],
    idempotence_token: typing.Optional[str],
) -> n: The updated dictionary
```
Recursively update a dictionary with format strings with values from another dictionary where the keys match
the format string. This goes a little beyond regular python string formatting and uses `.` to denote nested keys.

For example, if original_dict is {"EndpointConfigName": "{endpoint_config_name}"},
and update_dict is {"endpoint_config_name": "my-endpoint-config"},
then the result will be {"EndpointConfigName": "my-endpoint-config"}.

For nested keys if the original_dict is {"EndpointConfigName": "{inputs.endpoint_config_name}"},
and update_dict is {"inputs": {"endpoint_config_name": "my-endpoint-config"}},
then the result will be {"EndpointConfigName": "my-endpoint-config"}.



| Parameter | Type |
|-|-|
| `service` | `str` |
| `original_dict` | `typing.Any` |
| `update_dict` | `typing.Dict[str, typing.Any]` |
| `idempotence_token` | `typing.Optional[str]` |

#### get_nested_value()

```python
def get_nested_value(
    d: typing.Dict[str, typing.Any],
    keys: list[str],
) -> typing.Any
```
Retrieve the nested value from a dictionary based on a list of keys.


| Parameter | Type |
|-|-|
| `d` | `typing.Dict[str, typing.Any]` |
| `keys` | `list[str]` |

#### replace_placeholder()

```python
def replace_placeholder(
    service: str,
    original_dict: str,
    placeholder: str,
    replacement: str,
) -> str
```
Replace a placeholder in the original string and handle the specific logic for the sagemaker service and idempotence token.


| Parameter | Type |
|-|-|
| `service` | `str` |
| `original_dict` | `str` |
| `placeholder` | `str` |
| `replacement` | `str` |

