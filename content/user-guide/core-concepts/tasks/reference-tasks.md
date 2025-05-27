---
title: Reference tasks
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Reference tasks

A reference_task references tasks that have already been defined, serialized, and registered. You can reference tasks from other projects and create workflows that use tasks declared by others. These tasks can be in their own containers, python runtimes, flytekit versions, and even different languages.

> [!NOTE]
> Reference tasks cannot be run locally. To test locally, mock them out.

## Example

1. Create a file called `task.py` and insert this content into it:

    ```python
    import {{< key kit_import >}}

    @{{< key kit_as >}}.task
    def add_two_numbers(a: int, b: int) -> int:
        return a + b
    ```

2. Register the task:

   ```shell
   $ {{< key cli >}} register --project flytesnacks --domain development --version v1 task.py
   ```

3. Create a separate file `wf_ref_task.py` and copy the following code into it:

   ```python
   from flytekit import reference_task

   @reference_task(
       project="flytesnacks",
       domain="development",
       name="task.add_two_numbers",
       version="v1",
   )
   def add_two_numbers(a: int, b: int) -> int:
       ...

   @{{< key kit_as >}}.workflow
   def wf(a: int, b: int) -> int:
       return add_two_numbers(a, b)
   ```

4. Register the `wf` workflow:

    ```shell
    $ {{< key cli >}} register --project flytesnacks --domain development wf_ref_task.py
    ```

5. In the {{< key product_name >}} UI, run the workflow `wf_ref_task.wf`.
