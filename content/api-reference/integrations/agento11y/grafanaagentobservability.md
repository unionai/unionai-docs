---
title: GrafanaAgentObservability
description: "A link to this run's conversation in Grafana Agent Observability."
icon: braces
version: 2.11.1.dev2+g6d3d72b81
variants: +flyte +union
layout: py_api
---

# GrafanaAgentObservability

**Package:** `flyteplugins.agento11y`

A link to this run's conversation in Grafana Agent Observability.

Opens the conversation itself rather than the filtered list, since the run maps one to one
onto a conversation and the list is an extra click. `return_to` fills the app's back
navigation with the list filtered to the same run, which is what the app itself does.

This resolves whenever the run really is the conversation id, which every framework this
plugin instruments now arranges. `by_run=False` remains for anything that names
conversations itself — a framework added later, or an agent whose conversations
deliberately span several runs — and lands on the conversations list rather than a URL
that resolves to nothing.



## Parameters

```python
class GrafanaAgentObservability(
    host: str,
    name: str = 'Grafana Agent Observability',
    icon_uri: Optional[str] = '',
    app_id: str = 'grafana-agento11y-app',
    conversation_path: str = 'conversations/{conversation_id}/explore',
    list_path: str = 'conversations',
    return_to: bool = True,
    by_run: bool = True,
)
```
| Parameter | Type | Description |
|-|-|-|
| `host` | `str` | Stack URL, e.g. `https://myorg.grafana.net`. |
| `name` | `str` | Label shown in the Flyte UI. |
| `icon_uri` | `Optional[str]` | |
| `app_id` | `str` | Grafana app plugin id. The app moved from `grafana-sigil-app` to `grafana-agento11y-app`; the old id still resolves but is deprecated. |
| `conversation_path` | `str` | Path template within the app, given the conversation id. |
| `list_path` | `str` | Path of the conversations list, used for the back navigation. |
| `return_to` | `bool` | Include the back-navigation parameter. Set False for a bare link. |
| `by_run` | `bool` | Address the conversation by the Flyte run. Set False when something else owns the conversation id, so the link goes to the list rather than a dead conversation. |

## Methods

| Method | Description |
|-|-|
| [`get_link()`](#get_link) | Returns a task log link given the action. |


### get_link()

```python
def get_link(
    run_name: str,
    project: str,
    domain: str,
    context: Dict[str, str],
    parent_action_name: str,
    action_name: str,
    pod_name: str,
    **kwargs,
) -> str
```
Returns a task log link given the action.
Link can have template variables that are replaced by the backend.



| Parameter | Type | Description |
|-|-|-|
| `run_name` | `str` | The name of the run. |
| `project` | `str` | The project name. |
| `domain` | `str` | The domain name. |
| `context` | `Dict[str, str]` | Additional context for generating the link. |
| `parent_action_name` | `str` | The name of the parent action. |
| `action_name` | `str` | The name of the action. |
| `pod_name` | `str` | The name of the pod. |
| `**kwargs` |  | Additional keyword arguments. |

**Returns:** The generated link.

