---
title: Release Notes
weight: 6
variants: +serverless +byoc +selfmanaged
top_menu: true
sidebar_expanded: true
---

# Release Notes

{{< variant serverless byoc selfmanaged >}}
{{< markdown >}}

## October 2025

### Larger fanouts
You can now run up to 50,000 actions within a run and up to 1,000 actions concurrently. 
To enable observability across so many actions, we added group and sub-actions UI views, which show summary statistics about the actions which were spawned within a group or action.
You can use these summary views (as well as the action status filter) to spot check long-running or failed actions.

![50k Fanout Visualization](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_50k_fanout.gif)

This is a big milestone on our way to supporting million-task fanouts.

### Remote debugging for Ray head nodes
Rather than locally reproducing errors, sometimes you just want to zoom into the remote execution and see what's happening.
We directly enable this with the debug button.
When you click "Debug action" from an action in a run, we spin up that action's environment, code, and input data, and attach a live VS Code debugger.
Previously, this was only possible with vanilla Python tasks.
Now, you can debug multi-node distributed computations on Ray directly.

![Debugging Ray Head Node](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_ray_head_debug.gif)

### Triggers and audit history
[Triggers](../user-guide/task-configuration/triggers.md) let you templatize and set schedules for your workflows, similar to Launch Plans in Flyte 1.0.

```python
@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"
```

Upon deploy, it's possible to see all the triggers which are associated with a task:

-> show Task Details "triggers" tab
![Triggers for a Task](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_triggers_for_task.png)

We also maintain an audit history of every deploy, activation, and deactivation event, so you can get a sense of who's touched an automation.

-> show activity log GIF
[Triggers Activity Log](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_trigger_activity_log.gif)

### Deployed tasks and input passing

You can see the runs, task spec, and triggers associated with any deployed task, and launch it from the UI. We've converted the launch forms to a convenient JSON Schema syntax, so you can easily copy-paste the inputs from a previous run into a new run for any task.

[Deployed Tasks and Input Passing](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_tasks_and_input_passing.gif)


{{< /markdown >}}
{{< /variant >}}