---
title: flytekit.models.common
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.common

## Directory

### Classes

| Class | Description |
|-|-|
| [`Annotations`](.././flytekit.models.common#flytekitmodelscommonannotations) |  |
| [`AuthRole`](.././flytekit.models.common#flytekitmodelscommonauthrole) |  |
| [`EmailNotification`](.././flytekit.models.common#flytekitmodelscommonemailnotification) |  |
| [`Envs`](.././flytekit.models.common#flytekitmodelscommonenvs) |  |
| [`FlyteABCMeta`](.././flytekit.models.common#flytekitmodelscommonflyteabcmeta) |  |
| [`FlyteCustomIdlEntity`](.././flytekit.models.common#flytekitmodelscommonflytecustomidlentity) |  |
| [`FlyteIdlEntity`](.././flytekit.models.common#flytekitmodelscommonflyteidlentity) |  |
| [`FlyteType`](.././flytekit.models.common#flytekitmodelscommonflytetype) |  |
| [`Labels`](.././flytekit.models.common#flytekitmodelscommonlabels) |  |
| [`NamedEntityIdentifier`](.././flytekit.models.common#flytekitmodelscommonnamedentityidentifier) |  |
| [`Notification`](.././flytekit.models.common#flytekitmodelscommonnotification) |  |
| [`PagerDutyNotification`](.././flytekit.models.common#flytekitmodelscommonpagerdutynotification) |  |
| [`RawOutputDataConfig`](.././flytekit.models.common#flytekitmodelscommonrawoutputdataconfig) |  |
| [`SlackNotification`](.././flytekit.models.common#flytekitmodelscommonslacknotification) |  |
| [`UrlBlob`](.././flytekit.models.common#flytekitmodelscommonurlblob) |  |

## flytekit.models.common.Annotations

```python
class Annotations(
    values,
)
```
Annotation values to be applied to a workflow execution resource.



| Parameter | Type | Description |
|-|-|-|
| `values` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `values` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _common_pb2. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: _common_pb2.Annotations


## flytekit.models.common.AuthRole

```python
class AuthRole(
    assumable_iam_role,
    kubernetes_service_account,
)
```
Auth configuration for IAM or K8s service account.

Either one or both of the assumable IAM role and/or the K8s service account can be set.



| Parameter | Type | Description |
|-|-|-|
| `assumable_iam_role` |  | |
| `kubernetes_service_account` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `assumable_iam_role` | `None` | The IAM role to execute the workflow with :rtype: Text |
| `is_empty` | `None` |  |
| `kubernetes_service_account` | `None` | The kubernetes service account to execute the workflow with :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.launch_plan_pb2.Auth


## flytekit.models.common.EmailNotification

```python
class EmailNotification(
    recipients_email,
)
```
| Parameter | Type | Description |
|-|-|-|
| `recipients_email` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `recipients_email` | `None` | :rtype: list[Text] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.EmailNotification


## flytekit.models.common.Envs

```python
class Envs(
    envs: typing.Dict[str, str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `envs` | `typing.Dict[str, str]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `envs` | `None` |  |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2: flyteidl.admin.common_pb2.Envs,
) -> flyteidl.admin.common_pb2.Envs
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `flyteidl.admin.common_pb2.Envs` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.common.FlyteABCMeta

### Methods

| Method | Description |
|-|-|
| [`register()`](#register) | Register a virtual subclass of an ABC. |


#### register()

```python
def register(
    cls,
    subclass,
)
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `subclass` |  | |

## flytekit.models.common.FlyteCustomIdlEntity

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_dict()`](#to_dict) | Converts self to a dictionary. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_dict()

```python
def from_dict(
    idl_dict,
)
```
| Parameter | Type | Description |
|-|-|-|
| `idl_dict` |  | |

#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `idl_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_dict()

```python
def to_dict()
```
Converts self to a dictionary.
:rtype: dict[Text, T]


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.common.FlyteIdlEntity

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.common.FlyteType

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`register()`](#register) | Register a virtual subclass of an ABC. |
| [`short_class_string()`](#short_class_string) | :rtype: Text. |
| [`verbose_class_string()`](#verbose_class_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    cls,
    idl_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `idl_object` |  | |

#### register()

```python
def register(
    cls,
    subclass,
)
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `subclass` |  | |

#### short_class_string()

```python
def short_class_string(
    cls,
)
```
:rtype: Text


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |

#### verbose_class_string()

```python
def verbose_class_string(
    cls,
)
```
:rtype: Text


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |

## flytekit.models.common.Labels

```python
class Labels(
    values,
)
```
Label values to be applied to a workflow execution resource.



| Parameter | Type | Description |
|-|-|-|
| `values` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `values` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: dict[Text, Text]. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: dict[Text, Text]


## flytekit.models.common.NamedEntityIdentifier

```python
class NamedEntityIdentifier(
    project,
    domain,
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` |  | |
| `domain` |  | |
| `name` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `domain` | `None` | The name of the domain within the project. :rtype: Text |
| `is_empty` | `None` |  |
| `name` | `None` | The name of the entity within the namespace of the project and domain. :rtype: Text |
| `project` | `None` | The name of the project in which this entity lives. :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | Stores object to a Flyte-IDL defined protobuf. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `idl_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
Stores object to a Flyte-IDL defined protobuf.
:rtype: flyteidl.admin.common_pb2.NamedEntityIdentifier


## flytekit.models.common.Notification

```python
class Notification(
    phases,
    email: flytekit.models.common.EmailNotification,
    pager_duty: flytekit.models.common.PagerDutyNotification,
    slack: flytekit.models.common.SlackNotification,
)
```
Represents a structure for notifications based on execution status.



| Parameter | Type | Description |
|-|-|-|
| `phases` |  | |
| `email` | `flytekit.models.common.EmailNotification` | |
| `pager_duty` | `flytekit.models.common.PagerDutyNotification` | |
| `slack` | `flytekit.models.common.SlackNotification` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `email` | `None` | :rtype: EmailNotification |
| `is_empty` | `None` |  |
| `pager_duty` | `None` | :rtype: PagerDutyNotification |
| `phases` | `None` | A list of phases to which users can associate the notifications. :rtype: list[int] |
| `slack` | `None` | :rtype: SlackNotification |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.Notification


## flytekit.models.common.PagerDutyNotification

```python
class PagerDutyNotification(
    recipients_email,
)
```
| Parameter | Type | Description |
|-|-|-|
| `recipients_email` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `recipients_email` | `None` | :rtype: list[Text] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.PagerDutyNotification


## flytekit.models.common.RawOutputDataConfig

```python
class RawOutputDataConfig(
    output_location_prefix,
)
```
| Parameter | Type | Description |
|-|-|-|
| `output_location_prefix` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `output_location_prefix` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.Auth


## flytekit.models.common.SlackNotification

```python
class SlackNotification(
    recipients_email,
)
```
| Parameter | Type | Description |
|-|-|-|
| `recipients_email` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `recipients_email` | `None` | :rtype: list[Text] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.SlackNotification


## flytekit.models.common.UrlBlob

```python
class UrlBlob(
    url,
    bytes,
)
```
| Parameter | Type | Description |
|-|-|-|
| `url` |  | |
| `bytes` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `bytes` | `None` | :rtype: int |
| `is_empty` | `None` |  |
| `url` | `None` | :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.UrlBlob


