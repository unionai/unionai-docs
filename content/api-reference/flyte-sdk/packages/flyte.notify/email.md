---
title: Email
version: 2.5.9
variants: +flyte +union
layout: py_api
---

# Email

**Package:** `flyte.notify`

Send email notifications.



## Parameters

```python
class Email(
    on_phase: typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]],
    recipients: typing.Tuple[str, ...],
    cc: typing.Tuple[str, ...],
    bcc: typing.Tuple[str, ...],
    subject: str,
    body: str,
    html_body: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | ActionPhase(s) to trigger notification (e.g., ActionPhase.FAILED or (ActionPhase.FAILED, ActionPhase.TIMED_OUT)) |
| `recipients` | `typing.Tuple[str, ...]` | Email addresses for the "to" field. |
| `cc` | `typing.Tuple[str, ...]` | Optional email addresses for the "cc" field. |
| `bcc` | `typing.Tuple[str, ...]` | Optional email addresses for the "bcc" field. |
| `subject` | `str` | Email subject template (supports template variables). |
| `body` | `str` | Plain text body template (supports template variables). |
| `html_body` | `typing.Optional[str]` | Optional HTML body template (supports template variables). When provided, the email is sent as multipart with both plain text and HTML. |

