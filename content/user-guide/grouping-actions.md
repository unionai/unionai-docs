---
title: Grouping actions
weight: 120
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

Groups are declared using the [`flyte.group`](../api-reference/flyte-sdk/packages/flyte#group) context manager.
Any task invocations that occur within the `with flyte.group()` block are automatically associated with that group:

```python
with flyte.group("my-group-name"):
    # All task invocations here belong to "my-group-name"
    result1 = await task_a(data)
    result2 = await task_b(data)
    result3 = await task_c(data)
```

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

```python
@env.task
async def data_pipeline(raw_data: str) -> str:
    with flyte.group("data-validation"):
        validated_data = await validate_schema(raw_data)
        validated_data = await check_data_quality(validated_data)
        validated_data = await remove_duplicates(validated_data)

    with flyte.group("feature-engineering"):
        features = await extract_features(validated_data)
        features = await normalize_features(features)
        features = await select_features(features)

    with flyte.group("model-training"):
        model = await train_model(features)
        model = await validate_model(model)
        final_model = await save_model(model)

    return final_model
```

### Parallel processing with groups

Groups work well with parallel execution patterns:

```python
@env.task
async def parallel_processing_example(n: int) -> List[str]:
    results = []

    with flyte.group("parallel-processing"):
        # Collect all task invocations first
        for i in range(n):
            results.append(my_async_task(i))

        # Execute all tasks in parallel
        final_results = await asyncio.gather(*results)

    return final_results
```

### Multi-phase workflows

Use groups to organize different phases of complex workflows:

```python
@env.task
async def multi_phase_workflow(data_size: int) -> List[int]:
    # First phase: data preprocessing
    preprocessed = []
    with flyte.group("preprocessing"):
        for i in range(data_size):
            preprocessed.append(preprocess_task(i))
        phase1_results = await asyncio.gather(*preprocessed)

    # Second phase: main processing
    processed = []
    with flyte.group("main-processing"):
        for result in phase1_results:
            processed.append(process_task(result))
        phase2_results = await asyncio.gather(*processed)

    # Third phase: postprocessing
    postprocessed = []
    with flyte.group("postprocessing"):
        for result in phase2_results:
            postprocessed.append(postprocess_task(result))
        final_results = await asyncio.gather(*postprocessed)

    return final_results
```

### Nested groups

Groups can be nested to create hierarchical organization:

```python
@env.task
async def hierarchical_example():
    with flyte.group("machine-learning-pipeline"):
        with flyte.group("data-preparation"):
            cleaned_data = await clean_data(raw_data)
            split_data = await split_dataset(cleaned_data)

        with flyte.group("model-experiments"):
            with flyte.group("hyperparameter-tuning"):
                best_params = await tune_hyperparameters(split_data)

            with flyte.group("model-training"):
                model = await train_final_model(split_data, best_params)
```

### Conditional grouping

Groups can be used with conditional logic:

```python
@env.task
async def conditional_processing(use_advanced_features: bool):
    base_result = await basic_processing()

    if use_advanced_features:
        with flyte.group("advanced-features"):
            enhanced_result = await advanced_processing(base_result)
            optimized_result = await optimize_result(enhanced_result)
            return optimized_result
    else:
        with flyte.group("basic-features"):
            simple_result = await simple_processing(base_result)
            return simple_result
```

## Best practices for groups

1. **Meaningful names**: Use descriptive group names that indicate the purpose or phase
   ```python
   with flyte.group("feature-extraction"):
   with flyte.group("model-training"):
   with flyte.group("hyperparameter-sweep"):
   ```

2. **Logical boundaries**: Group related operations together, but don't make groups too large
   ```python
   # Good: Group by logical phase
   with flyte.group("data-validation"):
       # All validation tasks

   with flyte.group("feature-engineering"):
       # All feature engineering tasks
   ```

3. **Consistent patterns**: Use consistent naming conventions across your workflows
   ```python
   # Use consistent prefixes or patterns
   with flyte.group("phase-1-preprocessing"):
   with flyte.group("phase-2-training"):
   with flyte.group("phase-3-evaluation"):
   ```

4. **Appropriate granularity**: Balance between too many small groups and too few large groups
   ```python
   # Too granular - avoid
   with flyte.group("step-1"):
       task_a()
   with flyte.group("step-2"):
       task_b()

   # Better - logical grouping
   with flyte.group("data-preparation"):
       task_a()
       task_b()
       task_c()
   ```

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
