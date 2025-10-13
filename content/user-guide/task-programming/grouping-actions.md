---
title: Grouping actions
weight: 150
variants: +flyte +serverless +byoc +selfmanaged
---

# Grouping actions

Groups are an organizational feature in Flyte that allow you to logically cluster related task invocations (called "actions") for better visualization and management in the UI.
Groups help you organize task executions into manageable, hierarchical structures regardless of whether you're working with large fanouts or smaller, logically-related sets of operations.

## What are groups?

Groups provide a way to organize task invocations into logical units in the Flyte UI.
When you have multiple task executions—whether from large [fanouts](fanout.md), sequential operations, or any combination of tasks—groups help organize them into manageable units.

### The problem groups solve

Without groups, complex workflows can become visually overwhelming in the Flyte UI:
- Multiple task executions appear as separate nodes, making it hard to see the high-level structure
- Related operations are scattered throughout the workflow graph
- Debugging and monitoring becomes difficult when dealing with many individual task executions

Groups solve this by:
- **Organizing actions**: Multiple task executions within a group are presented as a hierarchical "folder" structure
- **Improving UI visualization**: Instead of many individual nodes cluttering the view, you see logical groups that can be collapsed or expanded
- **Aggregating status information**: Groups show aggregated run status (success/failure) of their contained actions when you hover over them in the UI
- **Maintaining execution parallelism**: Tasks still run concurrently as normal, but are organized for display

### How groups work

Groups are declared using the [`flyte.group`](../../api-reference/flyte-sdk/packages/flyte#group) context manager.
Any task invocations that occur within the `with flyte.group()` block are automatically associated with that group:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="simple" lang="python" >}}

The key points about groups:

1. **Context-based**: Use the `with flyte.group("name"):` context manager.
2. **Organizational tool**: Task invocations within the context are grouped together in the UI.
3. **UI folders**: Groups appear as collapsible/expandable folders in the Flyte UI run tree.
4. **Status aggregation**: Hover over a group in the UI to see aggregated success/failure information.
5. **Execution unchanged**: Tasks still execute in parallel as normal; groups only affect organization and visualization.

**Important**: Groups do not aggregate outputs. Each task execution still produces its own individual outputs. Groups are purely for organization and UI presentation.

## Common grouping patterns

### Sequential operations

Group related sequential operations that logically belong together:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="sequential" lang="python" >}}

### Parallel processing with groups

Groups work well with parallel execution patterns:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="parallel" lang="python" >}}

### Multi-phase workflows

Use groups to organize different phases of complex workflows:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="multi" lang="python" >}}

### Nested groups

Groups can be nested to create hierarchical organization:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="nested" lang="python" >}}

### Conditional grouping

Groups can be used with conditional logic:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="conditional" lang="python" >}}

## Best practices for groups

1. **Meaningful names**: Use descriptive group names that indicate the purpose or phase

   {{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="meaningful" lang="python" >}}

2. **Logical boundaries**: Group related operations together, but don't make groups too large

   {{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="logical" lang="python" >}}

3. **Consistent patterns**: Use consistent naming conventions across your workflows

   {{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="consistent" lang="python" >}}

4. **Appropriate granularity**: Balance between too many small groups and too few large groups

   {{< code file="/external/unionai-examples/v2/user-guide/task-programming/grouping-actions/grouping.py" fragment="granularity" lang="python" >}}

5. **UI consideration**: Remember that groups are primarily for organization and visualization—they don't affect execution performance

## When to use groups

Groups are particularly valuable when you have:

- **Multi-phase workflows**: Different stages that should be visually separated
- **Large-scale parallel processing**: Hundreds or thousands of task invocations from [fanouts](fanout.md)
- **Complex business logic**: Multiple related operations that form logical units
- **Iterative processes**: Multiple rounds of similar operations
- **A/B testing scenarios**: Multiple experimental conditions running in parallel
- **Data pipelines**: ETL operations with distinct phases
- **Machine learning workflows**: Data prep, training, validation, and deployment phases

## Key insights

Groups are primarily an organizational and UI visualization tool—they don't change how your tasks execute or aggregate their outputs, but they help organize related task invocations (actions) into collapsible folder-like structures for better workflow management and display. The aggregated status information (success/failure rates) is visible when hovering over group folders in the UI.

Groups make your Flyte workflows more maintainable and easier to understand, especially when working with complex workflows that involve multiple logical phases or large numbers of task executions. They serve as organizational "folders" in the UI's call stack tree, allowing you to collapse sections to reduce visual distraction while still seeing aggregated status information on hover.
