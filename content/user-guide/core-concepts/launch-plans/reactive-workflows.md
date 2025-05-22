---
title: Reactive workflows
weight: 9
variants: -flyte +serverless +byoc +selfmanaged
---

# Reactive workflows

Reactive workflows leverage [artifacts](../artifacts) as the medium of exchange between workflows, such that when an upstream workflow emits an artifact, an artifact-driven trigger in a downstream workflow passes the artifact to a new downstream workflow execution.

A trigger is a rule defined in a launch plan that specifies that when a certain event occurs -- for instance, a new version of a particular artifact is materialized -- a particular launch plan will be executed. Triggers allow downstream data consumers, such as machine learning engineers, to automate their workflows to react to the output of upstream data producers, such as data engineers, while maintaining separation of concerns and eliminating the need for staggered schedules and manual executions.

Updating any trigger associated with a launch plan will create a new version of the launch plan, similar to how schedules are handled today. This means that multiple launch plans, each with different triggers, can be created to act on the same underlying workflow. Launch plans with triggers must be activated in order for the trigger to work.

> [!NOTE]
> Currently, there are only artifact event-based triggers, but in the future, triggers will be expanded to include other event-based workflow triggering mechanisms.

## Scope

Since a trigger is part of a launch plan, it is scoped as follows:
* Project
* Domain
* Launch plan name
* Launch plan version

## Trigger types

### Artifact events

An artifact event definition contains the following:
* Exactly one artifact that will activate the trigger when a new version of the artifact is created
* A workflow that is the target of the trigger
* (Optionally) Inputs to the workflow that will be executed by the trigger. It is possible to pass information from the source artifact, the source artifact itself, and other artifacts to the workflow that will be triggered.

For more information, see [Connecting workflows with artifact event triggers](../artifacts/connecting-workflows-with-artifact-event-triggers).
