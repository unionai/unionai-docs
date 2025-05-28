---
title: Dynamic workflows
weight: 3
variants: +flyte +serverless +byoc +selfmanaged
---

# Dynamic workflows

A workflow whose directed acyclic graph (DAG) is computed at run-time is a [`dynamic`]() workflow. <!-- TODO: add link to API -->

The tasks in a dynamic workflow are executed at runtime using dynamic inputs. A dynamic workflow shares similarities with the [`workflow`]()<!-- TODO: add link to API -->, as it uses a Python-esque domain-specific language to declare dependencies between the tasks or define new workflows.

A key distinction lies in the dynamic workflow being assessed at runtime. This means that the inputs are initially materialized and forwarded to the dynamic workflow, resembling the behavior of a task. However, the return value from a dynamic workflow is a [`Promise`]() <!-- TODO: add link to API --> object, which can be materialized by the subsequent tasks.

Think of a dynamic workflow as a combination of a task and a workflow. It is used to dynamically decide the parameters of a workflow at runtime and is both compiled and executed at run-time.

Dynamic workflows become essential when you need to do the following:
- Handle conditional logic
- Modify the logic of the code at runtime
- Change or decide on feature extraction parameters on the fly

## Defining a dynamic workflow

You can define a dynamic workflow using the `@{{< key kit_as >}}.dynamic` decorator.

Within the `@{{< key kit_as >}}.dynamic` context, each invocation of a [`task`]() <!-- TODO: add link to API --> or a derivative of the [`Task`]() <!-- TODO: add link to API --> class leads to deferred evaluation using a Promise, rather than the immediate materialization of the actual value. While nesting other `@{{< key kit_as >}}.dynamic` and `@{{< key kit_as >}}.workflow` constructs within this task is possible, direct interaction with the outputs of a task/workflow is limited, as they are lazily evaluated. If you need to interact with the outputs, we recommend separating the logic in a dynamic workflow and creating a new task to read and resolve the outputs.

The example below uses a dynamic workflow to count the common characters between any two strings.

We define a task that returns the index of a character, where A-Z/a-z is equivalent to 0-25:

```python
import {{< key kit_import >}}

@{{< key kit_as >}}.task
def return_index(character: str) -> int:
    if character.islower():
        return ord(character) - ord("a")
    else:
        return ord(character) - ord("A")
```

We also create a task that prepares a list of 26 characters by populating the frequency of each character:

```python
@{{< key kit_as >}}.task
def update_list(freq_list: list[int], list_index: int) -> list[int]:
    freq_list[list_index] += 1
    return freq_list
```

We define a task to calculate the number of common characters between the two strings:

```python
@{{< key kit_as >}}.task
def derive_count(freq1: list[int], freq2: list[int]) -> int:
    count = 0
    for i in range(26):
        count += min(freq1[i], freq2[i])
    return count
```

We define a dynamic workflow to accomplish the following:

1. Initialize an empty 26-character list to be passed to the `update_list` task.
2. Iterate through each character of the first string (`s1`) and populate the frequency list.
3. Iterate through each character of the second string (`s2`) and populate the frequency list.
4. Determine the number of common characters by comparing the two frequency lists.

The looping process depends on the number of characters in both strings, which is unknown until runtime:

```python
@{{< key kit_as >}}.dynamic
def count_characters(s1: str, s2: str) -> int:
    # s1 and s2 should be accessible

    # Initialize empty lists with 26 slots each, corresponding to every alphabet (lower and upper case)
    freq1 = [0] * 26
    freq2 = [0] * 26

    # Loop through characters in s1
    for i in range(len(s1)):
        # Calculate the index for the current character in the alphabet
        index = return_index(character=s1[i])
        # Update the frequency list for s1
        freq1 = update_list(freq_list=freq1, list_index=index)
        # index and freq1 are not accessible as they are promises

    # looping through the string s2
    for i in range(len(s2)):
        # Calculate the index for the current character in the alphabet
        index = return_index(character=s2[i])
        # Update the frequency list for s2
        freq2 = update_list(freq_list=freq2, list_index=index)
        # index and freq2 are not accessible as they are promises

    # Count the common characters between s1 and s2
    return derive_count(freq1=freq1, freq2=freq2)
```

A dynamic workflow is modeled as a task in the {{< key product_name >}} backend, but the body of the function is executed to produce a workflow at runtime. In both dynamic and static workflows, the output of tasks are Promise objects.

{{< key product_name >}} executes the dynamic workflow within its container, resulting in a compiled DAG, which is then accessible in the UI. It uses the information acquired during the dynamic task's execution to schedule and execute each task within the dynamic workflow. Visualization of the dynamic workflow's graph in the UI is only available after it has completed its execution.

When a dynamic workflow is executed, it generates the entire workflow structure as its output, termed the *futures file*.
This name reflects the fact that the workflow has yet to be executed, so all subsequent outputs are considered futures.

> [!NOTE]
> Local execution works when a `@{{< key kit_as >}}.dynamic` decorator is used because {{< key kit_name >}} treats it as a task that runs with native Python inputs.

Finally, we define a standard workflow that triggers the dynamic workflow:

```python
@{{< key kit_as >}}.workflow
def start_wf(s1: str, s2: str) -> int:
    return count_characters(s1=s1, s2=s2)
```

You can run the workflow locally as follows:

```python
if __name__ == "__main__":
    print(start_wf(s1="Pear", s2="Earth"))
```

## Advantages of dynamic workflows

### Flexibility

Dynamic workflows streamline the process of building pipelines, offering the flexibility to design workflows
according to the unique requirements of your project. This level of adaptability is not achievable with static workflows.

### Lower pressure on `etcd`

The workflow Custom Resource Definition (CRD) and the states associated with static workflows are stored in `etcd`,
the Kubernetes database. This database maintains {{< key product_name >}} workflow CRDs as key-value pairs, tracking the status of each node's execution.

However, `etcd` has a hard limit on data size, encompassing the workflow and node status sizes, so it is important to ensure that static workflows don't excessively consume memory.

In contrast, dynamic workflows offload the workflow specification (including node/task definitions and connections) to the object store. Still, the statuses of nodes are stored in the workflow CRD within `etcd`.

Dynamic workflows help alleviate some pressure on `etcd` storage space, providing a solution to mitigate storage constraints.

## Dynamic workflows vs. map tasks

Dynamic tasks come with overhead for large fan-out tasks as they store metadata for the entire workflow.
In contrast, [map tasks](../tasks/task-types#map-tasks) prove efficient for such extensive fan-out scenarios since they refrain from storing metadata, resulting in less noticeable overhead.

## Using dynamic workflows to achieve recursion

Merge sort is a perfect example to showcase how to seamlessly achieve recursion using dynamic workflows.
{{< key product_name >}} imposes limitations on the depth of recursion to prevent misuse and potential impacts on the overall stability of the system.

```python
from typing import Tuple

import {{< key kit_import >}}

@{{< key kit_as >}}.task
def split(numbers: list[int]) -> tuple[list[int], list[int]]:

    length = len(numbers)

    return (
        numbers[0 : int(length / 2)],
        numbers[int(length / 2) :]
    )


@{{< key kit_as >}}.task
def merge(sorted_list1: list[int], sorted_list2: list[int]) -> list[int]:
    result = []
    while len(sorted_list1) > 0 and len(sorted_list2) > 0:
        # Compare the current element of the first array with the current element of the second array.
        # If the element in the first array is smaller, append it to the result and increment the first array index.
        # Otherwise, do the same with the second array.
        if sorted_list1[0] < sorted_list2[0]:
            result.append(sorted_list1.pop(0))
        else:
            result.append(sorted_list2.pop(0))

    # Extend the result with the remaining elements from both arrays
    result.extend(sorted_list1)
    result.extend(sorted_list2)

    return result


@{{< key kit_as >}}.task
def sort_locally(numbers: list[int]) -> list[int]:
    return sorted(numbers)


@{{< key kit_as >}}.dynamic
def merge_sort_remotely(numbers: list[int], threshold: int) -> list[int]:
    split1, split2 = split(numbers=numbers)
    sorted1 = merge_sort(numbers=split1, threshold=threshold)
    sorted2 = merge_sort(numbers=split2, threshold=threshold)
    return merge(sorted_list1=sorted1, sorted_list2=sorted2)


@{{< key kit_as >}}.dynamic
def merge_sort(numbers: list[int], threshold: int=5) -> list[int]:

    if len(numbers) <= threshold:
        return sort_locally(numbers=numbers)
    else:
        return merge_sort_remotely(numbers=numbers, threshold=threshold)
```

By simply adding the `@{{< key kit_as >}}.dynamic` annotation, the `merge_sort_remotely` function transforms into a plan of execution,
generating a workflow with four distinct nodes. These nodes run remotely on potentially different hosts,
with {{< key product_name >}} ensuring proper data reference passing and maintaining execution order with maximum possible parallelism.

`@{{< key kit_as >}}.dynamic` is essential in this context because the number of times `merge_sort` needs to be triggered is unknown at compile time. The dynamic workflow calls a static workflow, which subsequently calls the dynamic workflow again,
creating a recursive and flexible execution structure.