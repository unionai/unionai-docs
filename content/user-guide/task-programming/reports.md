---
title: Reports
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Reports

The reports feature allows you to display and update custom output in the UI during task execution.

First, you set the `report=True` flag in the task decorator. This enables the reporting feature for that task.
Within a task with reporting enabled, a [`flyte.report.Report`](../../api-reference/flyte-sdk/packages/flyte.report/report) object is created automatically.

A `Report` object contains one or more tabs, each of which contains HTML.
You can write HTML to an existing tab and create new tabs to organize your content.
Initially, the `Report` object has one tab (the default tab) with no content.

To write content:

- [`flyte.report.log()`](../../api-reference/flyte-sdk/packages/flyte.report#log) appends HTML content directly to the default tab.
- [`flyte.report.replace()`](../../api-reference/flyte-sdk/packages/flyte.report#replace) replaces the content of the default tab with new HTML.

To get or create a new tab:

- [`flyte.report.get_tab()`](../../api-reference/flyte-sdk/packages/flyte.report#get_tab) allows you to specify a unique name for the tab, and it will return the existing tab if it already exists or create a new one if it doesn't.
  It returns a `flyte.report._report.Tab`

You can `log()` or `replace()` HTML on the `Tab` object just as you can directly on the `Report` object.

Finally, you send the report to the Flyte server and make it visible in the UI:

- [`flyte.report.flush()`](../../api-reference/flyte-sdk/packages/flyte.report#flush) dispatches the report.
  **It is important to call this method to ensure that the data is sent**.

<!-- TODO:
Check (test) if implicit flush is performed at the end of the task execution.
-->

## A simple example

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/reports/simple.py" lang="python" >}}

Here we define a task `task1` that logs some HTML content to the default tab and creates a new tab named "Tab 2" where it logs additional HTML content.
The `flush` method is called to send the report to the backend.

## A more complex example

Here is another example.
We import the necessary modules, set up the task environment, define the main task with reporting enabled and define the data generation function:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/reports/globe_visualization.py" fragment="section-1" lang="python" >}}

We then define the HTML content for the report:

```python
def get_html_content():
    data_points = generate_globe_data()

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    ...
    </html>
    return html_content
"""
```

(We exclude it here due to length. You can find it in the [source file](https://github.com/unionai/unionai-examples/blob/main/v2/user-guide/task-programming/reports/globe_visualization.py)).

Finally, we run the workflow:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/reports/globe_visualization.py" fragment="section-2" lang="python" >}}

When the workflow runs, the report will be visible in the UI:

![Globe visualization](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/globe_visualization.png)

## Streaming example

Above we demonstrated reports that are sent to the UI once, at the end of the task execution.
But, you can also stream updates to the report during task execution and see the display update in real-time.

You do this by calling `flyte.report.flush()` (or specifying `do_flush=True` in `flyte.report.log()`) periodically during the task execution, instead of just at the end of the task execution

> [!NOTE]
> In the above examples we explicitly call `flyte.report.flush()` to send the report to the UI.
> In fact, this is optional since flush will be called automatically at the end of the task execution.
> For streaming reports, on the other hand, calling `flush()` periodically (or specifying `do_flush=True`
> in `flyte.report.log()`) is necessary to display the updates.

First we import the necessary modules, and set up the task environment:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/reports/streaming_reports.py" fragment="section-1" lang="python" >}}

Next we define the HTML content for the report:

```python
DATA_PROCESSING_DASHBOARD_HTML = """
...
"""
```

(We exclude it here due to length. You can find it in the [source file](
https://github.com/unionai/unionai-examples/blob/main/v2/user-guide/task-programming/reports/streaming_reports.py)).

Finally, we define the task that renders the report (`data_processing_dashboard`), the driver task of the workflow (`main`), and the run logic:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/reports/streaming_reports.py" fragment="section-2" lang="python" >}}

The key to the live update ability is the `while` loop that appends Javascript to the report. The Javascript calls execute on append to the document and update it.

When the workflow runs, you can see the report updating in real-time in the UI:

![Data Processing Dashboard](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/user-guide/data_processing_dashboard.png)
