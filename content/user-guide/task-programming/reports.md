---
title: Reports
weight: 10
variants: +flyte +union
---

# Reports

The reports feature allows you to display and update custom output in the UI during task execution.

{{< note >}}
Reports are the Flyte 2 successor to **Decks** in Flyte 1. Where Flyte 1 used `enable_deck=True` and the `flytekit.Deck` API, Flyte 2 uses `report=True` and the `flyte.report` API described below.
{{< /note >}}

First, you set the `report=True` flag in the task decorator. This enables the reporting feature for that task.
Within a task with reporting enabled, a `flyte.report.Report` object is created automatically.

> [!NOTE] Import `flyte.report` explicitly
> `flyte.report` is a submodule that `import flyte` does **not** import automatically.
> You must import it explicitly:
>
> ```python
> import flyte.report
> ```
>
> Without this, calls like `flyte.report.replace()` or `flyte.report.flush()` raise
> `AttributeError: module 'flyte' has no attribute 'report'`, most commonly hit in local or
> notebook runs. This applies to all `flyte.*` submodules: import the specific submodule you use,
> not just the top-level `flyte` package.

A `Report` object contains one or more tabs, each of which contains HTML.
You can write HTML to an existing tab and create new tabs to organize your content.
Initially, the `Report` object has one tab (the default tab, named `main`) with no content.

To write content:

- `flyte.report.log()` appends HTML content directly to the default tab.
- `flyte.report.replace()` replaces the content of the default tab with new HTML.

To get or create a new tab:

- `flyte.report.get_tab()` allows you to specify a unique name for the tab, and it will return the existing tab if it already exists or create a new one if it doesn't.
  It returns a `flyte.report._report.Tab`

You can `log()` or `replace()` HTML on the `Tab` object just as you can directly on the `Report` object.

To access the current `Report` object directly — for example, to enumerate its tabs or assemble the final HTML — call `flyte.report.current_report()`.

Finally, you send the report to the Flyte backend and make it visible in the UI:

- `flyte.report.flush()` dispatches the report (in its current state) to the backend.

You do **not** have to call `flyte.report.flush()` explicitly at the end of a task: when a task with `report=True` finishes, Flyte automatically performs a final flush for you.
Calling `flyte.report.flush()` yourself is only necessary when you want to *stream* updates to the UI while the task is still running (see [Streaming example](#streaming-example) below).

## A simple example

{{< code file="/unionai-examples/v2/user-guide/task-programming/reports/simple.py" lang="python" >}}

Here we define a task `task1` that uses `flyte.report.replace()` to set the content of the default tab, then creates a new tab named "Tab 2" with `flyte.report.get_tab()` and logs additional HTML content to it.
Finally, `flyte.report.flush()` is called to send the report to the backend.

## A more complex example

Here is another example.
We import the necessary modules, set up the task environment, define the main task with reporting enabled and define the data generation function:

{{< code file="/unionai-examples/v2/user-guide/task-programming/reports/globe_visualization.py" fragment="section-1" lang="python" >}}

We then define the HTML content for the report:

```python
def get_html_content():
    data_points = generate_globe_data()
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    ...
    </html>
    """
    return html_content
```

(We exclude it here due to length. You can find it in the [source file](https://github.com/unionai/unionai-examples/blob/main/v2/user-guide/task-programming/reports/globe_visualization.py)).

Finally, we run the workflow:

{{< code file="/unionai-examples/v2/user-guide/task-programming/reports/globe_visualization.py" fragment="section-2" lang="python" >}}

When the workflow runs, the report will be visible in the UI:

![Globe visualization](../../_static/images/user-guide/globe_visualization.png)

## Streaming example

Above we demonstrated reports that are sent to the UI once, at the end of the task execution.
But, you can also stream updates to the report during task execution and see the display update in real-time.

You do this by calling `flyte.report.flush()` periodically during task execution, instead of just at the end.
As a shortcut, you can also pass `do_flush=True` to `flyte.report.log()` or `flyte.report.replace()` to flush immediately after writing the content.

> [!NOTE]
> In the earlier examples we explicitly call `flyte.report.flush()` to send the report to the UI.
> As noted above, that final flush is optional: it happens automatically when the task completes.
> For streaming reports, on the other hand, calling `flyte.report.flush()` periodically (or passing `do_flush=True`
> to `flyte.report.log()` / `flyte.report.replace()`) is what makes the intermediate updates appear.

First we import the necessary modules, and set up the task environment:

{{< code file="/unionai-examples/v2/user-guide/task-programming/reports/streaming_reports.py" fragment="section-1" lang="python" >}}

Next we define the HTML content for the report:

```python
DATA_PROCESSING_DASHBOARD_HTML = """
...
"""
```

(We exclude it here due to length. You can find it in the [source file](
https://github.com/unionai/unionai-examples/blob/main/v2/user-guide/task-programming/reports/streaming_reports.py)).

Finally, we define the task that renders the report (`data_processing_dashboard`), the driver task of the workflow (`main`), and the run logic:

{{< code file="/unionai-examples/v2/user-guide/task-programming/reports/streaming_reports.py" fragment="section-2" lang="python" >}}

The key to the live update ability is the `while` loop that appends Javascript to the report. The Javascript calls execute on append to the document and update it.

When the workflow runs, you can see the report updating in real-time in the UI:

![Data Processing Dashboard](../../_static/images/user-guide/data_processing_dashboard.png)
