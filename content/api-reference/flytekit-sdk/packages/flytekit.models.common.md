---
title: flytekit.models.common
version: 0.1.dev2192+g7c539c3.d20250403
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
| [`FlyteABCMeta`](.././flytekit.models.common#flytekitmodelscommonflyteabcmeta) | Metaclass for defining Abstract Base Classes (ABCs). |
| [`FlyteCustomIdlEntity`](.././flytekit.models.common#flytekitmodelscommonflytecustomidlentity) |  |
| [`FlyteIdlEntity`](.././flytekit.models.common#flytekitmodelscommonflyteidlentity) |  |
| [`FlyteType`](.././flytekit.models.common#flytekitmodelscommonflytetype) | Metaclass for defining Abstract Base Classes (ABCs). |
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



| Parameter | Type |
|-|-|
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: _common_pb2. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Annotations
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `values` |  |  |

## flytekit.models.common.AuthRole

```python
class AuthRole(
    assumable_iam_role,
    kubernetes_service_account,
)
```
Auth configuration for IAM or K8s service account.

Either one or both of the assumable IAM role and/or the K8s service account can be set.



| Parameter | Type |
|-|-|
| `assumable_iam_role` |  |
| `kubernetes_service_account` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Auth
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `assumable_iam_role` |  | {{< multiline >}}The IAM role to execute the workflow with
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `kubernetes_service_account` |  | {{< multiline >}}The kubernetes service account to execute the workflow with
:rtype: Text
{{< /multiline >}} |

## flytekit.models.common.EmailNotification

```python
class EmailNotification(
    recipients_email,
)
```
| Parameter | Type |
|-|-|
| `recipients_email` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: EmailNotification
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `recipients_email` |  | {{< multiline >}}:rtype: list[Text]
{{< /multiline >}} |

## flytekit.models.common.Envs

```python
class Envs(
    envs: typing.Dict[str, str],
)
```
| Parameter | Type |
|-|-|
| `envs` | `typing.Dict[str, str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2: flyteidl.admin.common_pb2.Envs,
) -> flyteidl.admin.common_pb2.Envs
```
| Parameter | Type |
|-|-|
| `pb2` | `flyteidl.admin.common_pb2.Envs` |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `envs` |  |  |
| `is_empty` |  |  |

## flytekit.models.common.FlyteABCMeta

Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).


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


| Parameter | Type |
|-|-|
| `cls` |  |
| `subclass` |  |

## flytekit.models.common.FlyteCustomIdlEntity

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_dict()`](#to_dict) | Converts self to a dictionary. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_dict()

```python
def from_dict(
    idl_dict,
)
```
| Parameter | Type |
|-|-|
| `idl_dict` |  |

#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
) -> n: FlyteCustomIdlEntity
```
| Parameter | Type |
|-|-|
| `idl_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.common.FlyteIdlEntity

### Methods

| Method | Description |
|-|-|
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


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
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |

## flytekit.models.common.FlyteType

Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).


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
| Parameter | Type |
|-|-|
| `cls` |  |
| `idl_object` |  |

#### register()

```python
def register(
    cls,
    subclass,
)
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type |
|-|-|
| `cls` |  |
| `subclass` |  |

#### short_class_string()

```python
def short_class_string(
    cls,
) -> e: Text
```
:rtype: Text


| Parameter | Type |
|-|-|
| `cls` |  |

#### verbose_class_string()

```python
def verbose_class_string(
    cls,
) -> e: Text
```
:rtype: Text


| Parameter | Type |
|-|-|
| `cls` |  |

## flytekit.models.common.Labels

```python
class Labels(
    values,
)
```
Label values to be applied to a workflow execution resource.



| Parameter | Type |
|-|-|
| `values` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: dict[Text, Text]. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Labels
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `values` |  |  |

## flytekit.models.common.NamedEntityIdentifier

```python
class NamedEntityIdentifier(
    project,
    domain,
    name,
)
```
| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | Stores object to a Flyte-IDL defined protobuf. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
) -> e: NamedEntityIdentifier
```
| Parameter | Type |
|-|-|
| `idl_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  | {{< multiline >}}The name of the domain within the project.
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}The name of the entity within the namespace of the project and domain.
:rtype: Text
{{< /multiline >}} |
| `project` |  | {{< multiline >}}The name of the project in which this entity lives.
:rtype: Text
{{< /multiline >}} |

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



| Parameter | Type |
|-|-|
| `phases` |  |
| `email` | `flytekit.models.common.EmailNotification` |
| `pager_duty` | `flytekit.models.common.PagerDutyNotification` |
| `slack` | `flytekit.models.common.SlackNotification` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> e: Notification
```
| Parameter | Type |
|-|-|
| `p` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `email` |  | {{< multiline >}}:rtype: EmailNotification
{{< /multiline >}} |
| `is_empty` |  |  |
| `pager_duty` |  | {{< multiline >}}:rtype: PagerDutyNotification
{{< /multiline >}} |
| `phases` |  | {{< multiline >}}A list of phases to which users can associate the notifications.
:rtype: list[int]
{{< /multiline >}} |
| `slack` |  | {{< multiline >}}:rtype: SlackNotification
{{< /multiline >}} |

## flytekit.models.common.PagerDutyNotification

```python
class PagerDutyNotification(
    recipients_email,
)
```
| Parameter | Type |
|-|-|
| `recipients_email` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: EmailNotification
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `recipients_email` |  | {{< multiline >}}:rtype: list[Text]
{{< /multiline >}} |

## flytekit.models.common.RawOutputDataConfig

```python
class RawOutputDataConfig(
    output_location_prefix,
)
```
| Parameter | Type |
|-|-|
| `output_location_prefix` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2,
)
```
| Parameter | Type |
|-|-|
| `pb2` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `output_location_prefix` |  |  |

## flytekit.models.common.SlackNotification

```python
class SlackNotification(
    recipients_email,
)
```
| Parameter | Type |
|-|-|
| `recipients_email` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: EmailNotification
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `recipients_email` |  | {{< multiline >}}:rtype: list[Text]
{{< /multiline >}} |

## flytekit.models.common.UrlBlob

```python
class UrlBlob(
    url,
    bytes,
)
```
| Parameter | Type |
|-|-|
| `url` |  |
| `bytes` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb,
) -> e: UrlBlob
```
| Parameter | Type |
|-|-|
| `pb` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `bytes` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `is_empty` |  |  |
| `url` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

