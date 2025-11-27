---
title: ImageConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ImageConfig

**Package:** `flytekit.configuration`

We recommend you to use ImageConfig.auto(img_name=None) to create an ImageConfig.
For example, ImageConfig.auto(img_name=""ghcr.io/flyteorg/flytecookbook:v1.0.0"") will create an ImageConfig.

ImageConfig holds available images which can be used at registration time. A default image can be specified
along with optional additional images. Each image in the config must have a unique name.

Attributes:
    default_image (Optional[Image]): The default image to be used as a container for task serialization.
    images (List[Image]): Optional, additional images which can be used in task container definitions.


```python
class ImageConfig(
    default_image: Optional[Image],
    images: Optional[List[Image]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `default_image` | `Optional[Image]` | |
| `images` | `Optional[List[Image]]` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from config file or from img_name. |
| [`auto_default_image()`](#auto_default_image) |  |
| [`create_from()`](#create_from) |  |
| [`find_image()`](#find_image) | Return an image, by name, if it exists. |
| [`from_dict()`](#from_dict) |  |
| [`from_images()`](#from_images) | Allows you to programmatically create an ImageConfig. |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |
| [`validate_image()`](#validate_image) | Validates the image to match the standard format. |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
    img_name: Optional[str],
) -> ImageConfig
```
Reads from config file or from img_name
Note that this function does not take into account the flytekit default images (see the Dockerfiles at the
base of this repo). To pick those up, see the auto_default_image function..



| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` | |
| `img_name` | `Optional[str]` | :return: |

### auto_default_image()

```python
def auto_default_image()
```
### create_from()

```python
def create_from(
    default_image: Optional[Image],
    other_images: typing.Optional[typing.List[Image]],
) -> ImageConfig
```
| Parameter | Type | Description |
|-|-|-|
| `default_image` | `Optional[Image]` | |
| `other_images` | `typing.Optional[typing.List[Image]]` | |

### find_image()

```python
def find_image(
    name,
) -> Optional[Image]
```
Return an image, by name, if it exists.


| Parameter | Type | Description |
|-|-|-|
| `name` |  | |

### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` | |
| `infer_missing` |  | |

### from_images()

```python
def from_images(
    default_image: str,
    m: typing.Optional[typing.Dict[str, str]],
)
```
Allows you to programmatically create an ImageConfig. Usually only the default_image is required, unless
your workflow uses multiple images

```python
ImageConfig.from_dict(
    "ghcr.io/flyteorg/flytecookbook:v1.0.0",
    {
        "spark": "ghcr.io/flyteorg/myspark:...",
        "other": "...",
    }
)
```

urn:


| Parameter | Type | Description |
|-|-|-|
| `default_image` | `str` | |
| `m` | `typing.Optional[typing.Dict[str, str]]` | |

### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type | Description |
|-|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` | |
| `parse_float` |  | |
| `parse_int` |  | |
| `parse_constant` |  | |
| `infer_missing` |  | |
| `kw` |  | |

### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type | Description |
|-|-|-|
| `infer_missing` | `bool` | |
| `only` |  | |
| `exclude` |  | |
| `many` | `bool` | |
| `context` |  | |
| `load_only` |  | |
| `dump_only` |  | |
| `partial` | `bool` | |
| `unknown` |  | |

### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type | Description |
|-|-|-|
| `encode_json` |  | |

### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `skipkeys` | `bool` | |
| `ensure_ascii` | `bool` | |
| `check_circular` | `bool` | |
| `allow_nan` | `bool` | |
| `indent` | `typing.Union[int, str, NoneType]` | |
| `separators` | `typing.Tuple[str, str]` | |
| `default` | `typing.Callable` | |
| `sort_keys` | `bool` | |
| `kw` |  | |

### validate_image()

```python
def validate_image(
    _: typing.Any,
    param: str,
    values: tuple,
) -> ImageConfig
```
Validates the image to match the standard format. Also validates that only one default image
is provided. a default image, is one that is specified as ``default=<image_uri>`` or just ``<image_uri>``. All
other images should be provided with a name, in the format ``name=<image_uri>`` This method can be used with the
CLI



| Parameter | Type | Description |
|-|-|-|
| `_` | `typing.Any` | click argument, ignored here. |
| `param` | `str` | the click argument, here should be "image" |
| `values` | `tuple` | user-supplied images :return: |

