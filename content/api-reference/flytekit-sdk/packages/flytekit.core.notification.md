---
title: flytekit.core.notification
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.notification


Notifications are primarily used when defining Launch Plans (also can be used when launching executions) and will trigger
the Flyte platform to send emails when a workflow run reaches certain stages (fails or succeeds, etc.).

> [!NOTE]
> Notifications require some setup and configuration on the Flyte platform side. Please contact your Flyte platform
    admins to get this feature enabled. See :std:ref:`cookbook:setting up workflow notifications`

Each notification type takes a list of {{< py_class_ref flytekit.models.core.execution.WorkflowExecutionPhase >}} and a list of
emails. Even though there are different notification classes in this module, they all just send email. The differentiation
offers semantic meaning to the end-user but do not functionally behave differently. Successful integration with Slack
and Pagerduty is incumbent on those email API being set-up correctly.

.. autoclass:: flytekit.core.notification.Notification


## Directory

### Classes

| Class | Description |
|-|-|
| [`Email`](.././flytekit.core.notification#flytekitcorenotificationemail) | This notification should be used when sending regular emails to people. |
| [`Notification`](.././flytekit.core.notification#flytekitcorenotificationnotification) |  |
| [`PagerDuty`](.././flytekit.core.notification#flytekitcorenotificationpagerduty) | This notification should be used when sending emails to the PagerDuty service. |
| [`Slack`](.././flytekit.core.notification#flytekitcorenotificationslack) | This notification should be used when sending emails to the Slack. |

## flytekit.core.notification.Email

This notification should be used when sending regular emails to people.

```python
from flytekit.models.core.execution import WorkflowExecutionPhase

Email(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])
```


```python
class Email(
    phases: typing.List[int],
    recipients_email: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
| `recipients_email` | `typing.List[str]` |

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

## flytekit.core.notification.Notification

```python
class Notification(
    phases: typing.List[int],
    email: flytekit.models.common.EmailNotification,
    pager_duty: flytekit.models.common.PagerDutyNotification,
    slack: flytekit.models.common.SlackNotification,
)
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
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

## flytekit.core.notification.PagerDuty

This notification should be used when sending emails to the PagerDuty service.

```python
from flytekit.models.core.execution import WorkflowExecutionPhase

PagerDuty(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])
```


```python
class PagerDuty(
    phases: typing.List[int],
    recipients_email: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
| `recipients_email` | `typing.List[str]` |

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

## flytekit.core.notification.Slack

This notification should be used when sending emails to the Slack.

```python
from flytekit.models.core.execution import WorkflowExecutionPhase

Slack(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])
```


```python
class Slack(
    phases: typing.List[int],
    recipients_email: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
| `recipients_email` | `typing.List[str]` |

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

