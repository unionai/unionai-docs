---
title: flyte.ai.chat
version: 2.5.11
variants: +flyte +union
layout: py_api
---

# flyte.ai.chat

flyte.ai.chat — FastAPI chat UI and HTML/CSS assets for Flyte agents.
## Directory

### Classes

| Class | Description |
|-|-|
| [`AgentChatAppEnvironment`](../flyte.ai.chat/agentchatappenvironment) | An :class:`~flyte. |
| [`CustomTheme`](../flyte.ai.chat/customtheme) | Declarative color theme for the Agent Chat UI. |

### Methods

| Method | Description |
|-|-|
| [`build_chat_html()`](#build_chat_html) | Build the full chat HTML with the given *title* and optional *custom_css*. |


### Variables

| Property | Type | Description |
|-|-|-|
| `CHAT_HTML_TEMPLATE` | `str` |  |
| `CUSTOM_THEME_CSS_TEMPLATE` | `str` |  |
| `DEFAULT_CSS` | `str` |  |

## Methods

#### build_chat_html()

```python
def build_chat_html(
    title: str,
    custom_css: str,
    logo_url: str | None,
    additional_buttons: list[dict[str, str]] | None,
    subtitle: str | None,
) -> str
```
Build the full chat HTML with the given *title* and optional *custom_css*.

The *custom_css* string is injected **after** the default styles, so it
can override any default rule.  *logo_url*, when provided, renders an
``&lt;img&gt;`` to the left of the title in the header bar.

*subtitle*, when provided, renders a subtitle paragraph below the
header bar.

*additional_buttons* is an optional list of ``{"button_text": ...,
"button_url": ...}`` dicts.  The first entry becomes the primary
(prominent) button; the rest appear in a drop-up menu behind a chevron.


| Parameter | Type | Description |
|-|-|-|
| `title` | `str` | |
| `custom_css` | `str` | |
| `logo_url` | `str \| None` | |
| `additional_buttons` | `list[dict[str, str]] \| None` | |
| `subtitle` | `str \| None` | |

