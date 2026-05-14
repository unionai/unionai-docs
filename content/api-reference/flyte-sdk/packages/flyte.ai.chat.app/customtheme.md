---
title: CustomTheme
version: 2.3.1
variants: +flyte +union
layout: py_api
---

# CustomTheme

**Package:** `flyte.ai.chat.app`

Declarative color theme for the Agent Chat UI.

All colors should be CSS hex strings (e.g. ``"#E6A71F"``).

Parameters
----------
accent_color:
    Primary brand color used for links, highlights, active
    indicators, and solid-background buttons.  Defaults to the
    built-in purple (``"#6F2AEF"``).
accent_hover_color:
    Lighter variant shown on hover states for accent-colored
    elements.  Defaults to ``"#8B52F2"``.
button_text_color:
    Text color rendered *on top of* accent-colored buttons.
    Should contrast well with *accent_color*.  Defaults to
    ``"#f3f4f6"`` (near-white).


## Parameters

```python
class CustomTheme(
    accent_color: str,
    accent_hover_color: str,
    button_text_color: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `accent_color` | `str` | |
| `accent_hover_color` | `str` | |
| `button_text_color` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`to_css()`](#to_css) | Generate a CSS override string from the theme colors. |


### to_css()

```python
def to_css()
```
Generate a CSS override string from the theme colors.


