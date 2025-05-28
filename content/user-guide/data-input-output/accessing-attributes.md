---
title: Accessing attributes
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Accessing attributes

You can directly access attributes on output promises for lists, dictionaries, dataclasses, and combinations of these types in {{< key product_name >}}.
Note that while this functionality may appear to be the normal behavior of Python, code in `@workflow` functions is not actually Python, but rather a Python-like DSL that is compiled by {{< key product_name >}}.
Consequently, accessing attributes in this manner is, in fact, a specially implemented feature.
This functionality facilitates the direct passing of output attributes within workflows, enhancing the convenience of working with complex data structures.

{{< variant flyte >}}
{{< markdown >}}

<!-- TODO: remove mention of flytesnacks -->
> [!NOTE]
> Flytekit version >= v1.14.0 supports Pydantic BaseModel V2, you can do attribute access on Pydantic BaseModel V2 as well.
>
> To clone and run the example code on this page, see the [Flytesnacks repo](https://github.com/flyteorg/flytesnacks/tree/master/examples/data_types_and_io/).

{{< /markdown >}}
{{< /variant >}}

To begin, import the required dependencies and define a common task for subsequent use:

```python
from dataclasses import dataclass
import {{< key kit_import >}}


@{{< key kit_as >}}.task
def print_message(message: str):
    print(message)
    return
```

## List
You can access an output list using index notation.

> [!NOTE]
> {{< key product_name >}} currently does not support output promise access through list slicing.

```python
@{{< key kit_as >}}.task
def list_task() -> list[str]:
    return ["apple", "banana"]


@{{< key kit_as >}}.workflow
def list_wf():
    items = list_task()
    first_item = items[0]
    print_message(message=first_item)
```

## Dictionary
Access the output dictionary by specifying the key.

```python
@{{< key kit_as >}}.task
def dict_task() -> dict[str, str]:
    return {"fruit": "banana"}


@{{< key kit_as >}}.workflow
def dict_wf():
    fruit_dict = dict_task()
    print_message(message=fruit_dict["fruit"])
```

## Data class
Directly access an attribute of a dataclass.

```python
@dataclass
class Fruit:
    name: str

@{{< key kit_as >}}.task
def dataclass_task() -> Fruit:
    return Fruit(name="banana")

@{{< key kit_as >}}.workflow
def dataclass_wf():
    fruit_instance = dataclass_task()
    print_message(message=fruit_instance.name)
```

## Complex type
Combinations of list, dict and dataclass also work effectively.

```python
@{{< key kit_as >}}.task
def advance_task() -> (dict[str, list[str]], list[dict[str, str]], dict[str, Fruit]):
    return {"fruits": ["banana"]}, [{"fruit": "banana"}], {"fruit": Fruit(name="banana")}

@{{< key kit_as >}}.task
def print_list(fruits: list[str]):
    print(fruits)

@{{< key kit_as >}}.task
def print_dict(fruit_dict: dict[str, str]):
    print(fruit_dict)

@{{< key kit_as >}}.workflow
def advanced_workflow():
    dictionary_list, list_dict, dict_dataclass = advance_task()
    print_message(message=dictionary_list["fruits"][0])
    print_message(message=list_dict[0]["fruit"])
    print_message(message=dict_dataclass["fruit"].name)

    print_list(fruits=dictionary_list["fruits"])
    print_dict(fruit_dict=list_dict[0])
```

You can run all the workflows locally as follows:

```python
if __name__ == "__main__":
    list_wf()
    dict_wf()
    dataclass_wf()
    advanced_workflow()
```

## Failure scenario
The following workflow fails because it attempts to access indices and keys that are out of range:

```python
from flytekit import WorkflowFailurePolicy


@{{< key kit_as >}}.task
def failed_task() -> (list[str], dict[str, str], Fruit):
    return ["apple", "banana"], {"fruit": "banana"}, Fruit(name="banana")


@{{< key kit_as >}}.workflow(
    # The workflow remains unaffected if one of the nodes encounters an error, as long as other executable nodes are still available
    failure_policy=WorkflowFailurePolicy.FAIL_AFTER_EXECUTABLE_NODES_COMPLETE
)
def failed_workflow():
    fruits_list, fruit_dict, fruit_instance = failed_task()
    print_message(message=fruits_list[100])  # Accessing an index that doesn't exist
    print_message(message=fruit_dict["fruits"])  # Accessing a non-existent key
    print_message(message=fruit_instance.fruit)  # Accessing a non-existent param
```
