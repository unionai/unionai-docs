---
title: Defining launch plans
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Defining launch plans

You can define a launch plan with the [`LaunchPlan` class](../../../api-reference/flytekit-sdk/packages/flytekit.core.launch_plan).

This is a simple example of defining a launch plan:

```python
import {{< key kit_import >}}

@{{< key kit_as >}}.workflow
def my_workflow(a: int, b: str) -> str:
    return f"Result: {a} and {b}"

# Create a default launch plan
default_lp = @{{< key kit_as >}}.LaunchPlan.get_or_create(workflow=my_workflow)

# Create a named launch plan
named_lp = @{{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="my_custom_launch_plan"
)
```

## Default and Fixed Inputs

Default inputs can be overridden at execution time, while fixed inputs cannot be changed.

```python
import {{< key kit_import >}}

# Launch plan with default inputs
lp_with_defaults = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="with_defaults",
    default_inputs={"a": 42, "b": "default_value"}
)

# Launch plan with fixed inputs
lp_with_fixed = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="with_fixed",
    fixed_inputs={"a": 100}  # 'a' will always be 100, only 'b' can be specified
)

# Combining default and fixed inputs
lp_combined = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="combined_inputs",
    default_inputs={"b": "default_string"},
    fixed_inputs={"a": 200}
)
```

## Scheduled Execution

```python
import {{< key kit_as >}}
from datetime import timedelta
from flytekit.core.schedule import CronSchedule, FixedRate

# Using a cron schedule (runs at 10:00 AM UTC every Monday)
cron_lp = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="weekly_monday",
    default_inputs={"a": 1, "b": "weekly"},
    schedule=CronSchedule(
        schedule="0 10 * * 1",  # Cron expression: minute hour day-of-month month day-of-week
        kickoff_time_input_arg=None
    )
)

# Using a fixed rate schedule (runs every 6 hours)
fixed_rate_lp = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="every_six_hours",
    default_inputs={"a": 1, "b": "periodic"},
    schedule=FixedRate(
        duration=timedelta(hours=6)
    )
)
```

## Labels and Annotations

Labels and annotations help with organization and can be used for filtering or adding metadata.

```python
import {{< key kit_as >}}
from flytekit.models.common import Labels, Annotations

# Adding labels and annotations
lp_with_metadata = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="with_metadata",
    default_inputs={"a": 1, "b": "metadata"},
    labels=Labels({"team": "data-science", "env": "staging"}),
    annotations=Annotations({"description": "Launch plan for testing", "owner": "jane.doe"})
)
```

## Execution Parameters

```python
import {{< key kit_as >}}

# Setting max parallelism to limit concurrent task execution
lp_with_parallelism = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="with_parallelism",
    default_inputs={"a": 1, "b": "parallel"},
    max_parallelism=10  # Only 10 task nodes can run concurrently
)

# Disable caching for this launch plan's executions
lp_no_cache = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="no_cache",
    default_inputs={"a": 1, "b": "fresh"},
    overwrite_cache=True  # Always execute fresh, ignoring cached results
)

# Auto-activate on registration
lp_auto_activate = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="auto_active",
    default_inputs={"a": 1, "b": "active"},
    auto_activate=True  # Launch plan will be active immediately after registration
)
```

## Security and Authentication

We can also override the auth role (either an iam role or a kubernetes service account) used to execute a launch plan.

```python
import {{< key kit_as >}}
from flytekit.models.common import AuthRole
from flytekit import SecurityContext

# Setting auth role for the launch plan
lp_with_auth = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="with_auth",
    default_inputs={"a": 1, "b": "secure"},
    auth_role=AuthRole(
        assumable_iam_role="arn:aws:iam::12345678:role/my-execution-role"
    )
)

# Setting security context
lp_with_security = {{< key kit_as >}}.LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="with_security",
    default_inputs={"a": 1, "b": "context"},
    security_context=SecurityContext(
        run_as=SecurityContext.K8sServiceAccount(name="my-service-account")
    )
)
```

## Raw Output Data Configuration

```python
from flytekit.models.common import RawOutputDataConfig

# Configure where large outputs should be stored
lp_with_output_config = LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="with_output_config",
    default_inputs={"a": 1, "b": "output"},
    raw_output_data_config=RawOutputDataConfig(
        output_location_prefix="s3://my-bucket/workflow-outputs/"
    )
)
```

## Putting It All Together

A pretty comprehensive example follows below. This custom launch plan has d

```python
comprehensive_lp = LaunchPlan.get_or_create(
    workflow=my_workflow,
    name="comprehensive_example",
    default_inputs={"b": "configurable"},
    fixed_inputs={"a": 42},
    schedule=CronSchedule(schedule="0 9 * * *"),  # Daily at 9 AM UTC
    notifications=[
        Notification(
            phases=["SUCCEEDED", "FAILED"],
            email=EmailNotification(recipients_email=["team@example.com"])
        )
    ],
    labels=Labels({"env": "production", "team": "data"}),
    annotations=Annotations({"description": "Daily data processing"}),
    max_parallelism=20,
    overwrite_cache=False,
    auto_activate=True,
    auth_role=AuthRole(assumable_iam_role="arn:aws:iam::12345678:role/workflow-role"),
    raw_output_data_config=RawOutputDataConfig(
        output_location_prefix="s3://results-bucket/daily-run/"
    )
)
```

These examples demonstrate the flexibility of Launch Plans in Flyte, allowing you to customize execution parameters, inputs, schedules, and more to suit your workflow requirements.
