---
title: Email
version: 2.1.2
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Email

**Package:** `flyte.notify`

Send email notifications.

    Example:
        ```python
        Email(
            on_phase=ActionPhase.FAILED,
            recipients=["oncall@example.com"],
            subject="Alert: Task {task.name} failed",
            body="Error: {run.error}
Details: {run.url}"
        )
        ```

    Args:
        on_phase: ActionPhase(s) to trigger notification
            (e.g., ActionPhase.FAILED or (ActionPhase.FAILED, ActionPhase.TIMED_OUT))
        recipients: Email addresses for the "to" field.
        cc: Optional email addresses for the "cc" field.
        bcc: Optional email addresses for the "bcc" field.
        subject: Email subject template (supports template variables).
        body: Plain text body template (supports template variables).
        html_body: Optional HTML body template (supports template variables).
            When provided, the email is sent as multipart with both plain text and HTML.
    


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
| `on_phase` | `typing.Union[flyte.models.ActionPhase, typing.Tuple[flyte.models.ActionPhase, ...]]` | |
| `recipients` | `typing.Tuple[str, ...]` | |
| `cc` | `typing.Tuple[str, ...]` | |
| `bcc` | `typing.Tuple[str, ...]` | |
| `subject` | `str` | |
| `body` | `str` | |
| `html_body` | `typing.Optional[str]` | |

