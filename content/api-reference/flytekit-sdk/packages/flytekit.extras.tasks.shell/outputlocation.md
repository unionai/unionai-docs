---
title: OutputLocation
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OutputLocation

**Package:** `flytekit.extras.tasks.shell`

```python
class OutputLocation(
    var: str,
    var_type: typing.Type,
    location: typing.Union[os.PathLike, str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `var` | `str` | str The name of the output variable |
| `var_type` | `typing.Type` | typing.Type The type of output variable |
| `location` | `typing.Union[os.PathLike, str]` | os.PathLike The location where this output variable will be written to or a regex that accepts input vars and generates the path. Of the form ``"{{ .inputs.v }}.tmp.md"``. This example for a given input v, at path `/tmp/abc.csv` will resolve to `/tmp/abc.csv.tmp.md` |

