# Flytekit SDK

[Flytekit Python](https://github.com/flyteorg/flytekit) is the Python Library for easily authoring, testing, deploying, and interacting with Flyte tasks, workflows, and launch plans.

```{list-table}
:header-rows: 0
:widths: 20 30

* - {doc}`Design <design/index>`
  - An overview of the design of the Flytekit SDK.
* - {doc}`Core Flytekit <core-flytekit/index>`
  - Contains all of the most common abstractions needed to write Flyte workflows and extend Flytekit.
* - {doc}`Configuration <configuration/index>`
  - A comprehensive look at the ways to configure Flytekit settings.
* - {doc}`ImageSpec <image-spec>`
  - Contains the ImageSpec class parameters and methods.
* - {doc}`Clients <clients>`
  - This module provides lower level access to a Union or Flyte backend.
* - {doc}`Unit testing <unit-testing>`
  - The imports exposed in this package will help you unit test your Flyte tasks.
* - {doc}`Specifying accelerators <specifying-accelerators>`
  - Used to specify accelerators in the task decorator and configure the Flyte backend to use your preferred accelerators.
* - {doc}`Extending Flytekit <extending-flytekit>`
  - Contains useful classes and methods for extending Flytekit.
* - {doc}`Flyte Deck <flyte-deck>`
  - Contains Deck renderers provided by Flytekit.
{@@ if byoc @@}
* - {doc}`Agent API reference  <agent-api-reference>`
  - Contains documentation on agent classes and methods.
{@@ endif @@}
* - {doc}`Custom tasks <custom-tasks/index>`
  - Flytekit ships with an extensible task system to make it easy for anyone to extend and add new task types.
* - {doc}`Custom types <custom-types/index>`
  - Flytekit ships with an extensible type system to make it easy for anyone to extend and add new types.
* - {doc}`Experimental features <experimental-features>`
  - Contains experimental constructs. Subject to breaking changes.
```
