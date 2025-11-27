---
title: flytekit.core.workflow
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.workflow

## Directory

### Classes

| Class | Description |
|-|-|
| [`ImperativeWorkflow`](../flytekit.core.workflow/imperativeworkflow) | An imperative workflow is a programmatic analogue to the typical ``@workflow`` function-based workflow and is. |
| [`PythonFunctionWorkflow`](../flytekit.core.workflow/pythonfunctionworkflow) | Please read :std:ref:`flyte:divedeep-workflows` first for a high-level understanding of what workflows are in Flyte. |
| [`ReferenceWorkflow`](../flytekit.core.workflow/referenceworkflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`WorkflowBase`](../flytekit.core.workflow/workflowbase) |  |
| [`WorkflowFailurePolicy`](../flytekit.core.workflow/workflowfailurepolicy) | Defines the behavior for a workflow execution in the case of an observed node execution failure. |
| [`WorkflowMetadata`](../flytekit.core.workflow/workflowmetadata) |  |
| [`WorkflowMetadataDefaults`](../flytekit.core.workflow/workflowmetadatadefaults) | This class is similarly named to the one above. |

### Methods

| Method | Description |
|-|-|
| [`construct_input_promises()`](#construct_input_promises) |  |
| [`get_promise()`](#get_promise) | This is a helper function that will turn a binding into a Promise object, using a lookup map. |
| [`get_promise_map()`](#get_promise_map) | Local execution of imperatively defined workflows is done node by node. |
| [`reference_workflow()`](#reference_workflow) | A reference workflow is a pointer to a workflow that already exists on your Flyte installation. |
| [`workflow()`](#workflow) | This decorator declares a function to be a Flyte workflow. |


### Variables

| Property | Type | Description |
|-|-|-|
| `FuncOut` | `TypeVar` |  |
| `P` | `ParamSpec` |  |
| `T` | `TypeVar` |  |

## Methods

#### construct_input_promises()

```python
def construct_input_promises(
    inputs: List[str],
) -> Dict[str, Promise]
```
| Parameter | Type | Description |
|-|-|-|
| `inputs` | `List[str]` | |

#### get_promise()

```python
def get_promise(
    binding_data: _literal_models.BindingData,
    outputs_cache: Dict[Node, Dict[str, Promise]],
) -> Promise
```
This is a helper function that will turn a binding into a Promise object, using a lookup map. Please see
get_promise_map for the rest of the details.


| Parameter | Type | Description |
|-|-|-|
| `binding_data` | `_literal_models.BindingData` | |
| `outputs_cache` | `Dict[Node, Dict[str, Promise]]` | |

#### get_promise_map()

```python
def get_promise_map(
    bindings: List[_literal_models.Binding],
    outputs_cache: Dict[Node, Dict[str, Promise]],
) -> Dict[str, Promise]
```
Local execution of imperatively defined workflows is done node by node. This function will fill in the node's
entity's input arguments, which are specified using the bindings list, and a map of nodes to its outputs.
Basically this takes the place of propeller in resolving bindings, pulling in outputs from previously completed
nodes and filling in the necessary inputs.


| Parameter | Type | Description |
|-|-|-|
| `bindings` | `List[_literal_models.Binding]` | |
| `outputs_cache` | `Dict[Node, Dict[str, Promise]]` | |

#### reference_workflow()

```python
def reference_workflow(
    project: str,
    domain: str,
    name: str,
    version: str,
) -> Callable[[Callable[..., Any]], ReferenceWorkflow]
```
A reference workflow is a pointer to a workflow that already exists on your Flyte installation. This
object will not initiate a network call to Admin, which is why the user is asked to provide the expected interface.
If at registration time the interface provided causes an issue with compilation, an error will be returned.

Example:

<!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_references.py
   :pyobject: ref_wf1
-->
```python
@reference_workflow(project="proj", domain="development", name="wf_name", version="abc")
def ref_wf1(a: int) -> typing.Tuple[str, str]:
    ...
    return "hello", "world"
```


| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `domain` | `str` | |
| `name` | `str` | |
| `version` | `str` | |

#### workflow()

```python
def workflow(
    _workflow_function: Optional[Callable[P, FuncOut]],
    failure_policy: Optional[WorkflowFailurePolicy],
    interruptible: bool,
    on_failure: Optional[Union[WorkflowBase, Task]],
    docs: Optional[Documentation],
    pickle_untyped: bool,
    default_options: Optional[Options],
) -> Union[Callable[P, FuncOut], Callable[[Callable[P, FuncOut]], PythonFunctionWorkflow], PythonFunctionWorkflow]
```
This decorator declares a function to be a Flyte workflow. Workflows are declarative entities that construct a DAG
of tasks using the data flow between tasks.

Unlike a task, the function body of a workflow is evaluated at serialization-time (aka compile-time). This is
because while we can determine the entire structure of a task by looking at the function's signature, workflows need
to run through the function itself because the body of the function is what expresses the workflow structure. It's
also important to note that, local execution notwithstanding, it is not evaluated again when the workflow runs on
Flyte.
That is, workflows should not call non-Flyte entities since they are only run once (again, this is with respect to
the platform, local runs notwithstanding).

Example:

<!--
.. literalinclude:: ../../../tests/flytekit/unit/core/test_workflows.py
-->

```python
import os
import sys
import typing
from collections import OrderedDict
from unittest.mock import patch

import pytest
from typing_extensions import Annotated  # type: ignore

import flytekit.configuration
from flytekit import FlyteContextManager, StructuredDataset, kwtypes
from flytekit.configuration import Image, ImageConfig
from flytekit.core import context_manager
from flytekit.core.condition import conditional
from flytekit.core.task import task
from flytekit.core.workflow import WorkflowFailurePolicy, WorkflowMetadata, WorkflowMetadataDefaults, workflow
from flytekit.exceptions.user import FlyteValidationException, FlyteValueException, FlyteMissingReturnValueException
from flytekit.tools.translator import get_serializable
from flytekit.types.error.error import FlyteError

default_img = Image(name="default", fqn="test", tag="tag")
serialization_settings = flytekit.configuration.SerializationSettings(
    project="project",
    domain="domain",
    version="version",
    env=None,
    image_config=ImageConfig(default_image=default_img, images=[default_img]),
)

def test_metadata_values():
    with pytest.raises(FlyteValidationException):
        WorkflowMetadata(on_failure=0)

    wm = WorkflowMetadata(on_failure=WorkflowFailurePolicy.FAIL_IMMEDIATELY)
    assert wm.on_failure == WorkflowFailurePolicy.FAIL_IMMEDIATELY


def test_default_metadata_values():
    with pytest.raises(FlyteValidationException):
        WorkflowMetadataDefaults(3)

    wm = WorkflowMetadataDefaults(interruptible=False)
    assert wm.interruptible is False


def test_workflow_values():
    @task
    def t1(a: int) -> typing.NamedTuple("OutputsBC", [("t1_int_output", int), ("c", str)]):
        a = a + 2
        return a, "world-" + str(a)

    @workflow(interruptible=True, failure_policy=WorkflowFailurePolicy.FAIL_AFTER_EXECUTABLE_NODES_COMPLETE)
    def wf(a: int) -> typing.Tuple[str, str]:
        x, y = t1(a=a)
        _, v = t1(a=x)
        return y, v

    wf_spec = get_serializable(OrderedDict(), serialization_settings, wf)
    assert wf_spec.template.metadata_defaults.interruptible
    assert wf_spec.template.metadata.on_failure == 1

def test_default_values():
    @task
    def t() -> bool:
        return True

    @task
    def f() -> bool:
        return False

    @workflow
    def wf(a: bool = True) -> bool:
        return conditional("bool").if_(a.is_true()).then(t()).else_().then(f())  # type: ignore

    assert wf() is True
    assert wf(a=False) is False


def test_list_output_wf():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def list_output_wf() -> typing.List[int]:
        v = []
        for i in range(2):
            v.append(t1(a=i))
        return v

    x = list_output_wf()
    assert x == [5, 6]


def test_sub_wf_single_named_tuple():
    nt = typing.NamedTuple("SingleNamedOutput", [("named1", int)])

    @task
    def t1(a: int) -> nt:
        a = a + 2
        return nt(a)

    @workflow
    def subwf(a: int) -> nt:
        return t1(a=a)

    @workflow
    def wf(b: int) -> nt:
        out = subwf(a=b)
        return t1(a=out.named1)

    x = wf(b=3)
    assert x == (7,)


def test_sub_wf_multi_named_tuple():
    nt = typing.NamedTuple("Multi", [("named1", int), ("named2", int)])

    @task
    def t1(a: int) -> nt:
        a = a + 2
        return nt(a, a)

    @workflow
    def subwf(a: int) -> nt:
        return t1(a=a)

    @workflow
    def wf(b: int) -> nt:
        out = subwf(a=b)
        return t1(a=out.named1)

    x = wf(b=3)
    assert x == (7, 7)


def test_sub_wf_varying_types():
    @task
    def t1l(
        a: typing.List[typing.Dict[str, typing.List[int]]],
        b: typing.Dict[str, typing.List[int]],
        c: typing.Union[typing.List[typing.Dict[str, typing.List[int]]], typing.Dict[str, typing.List[int]], int],
        d: int,
    ) -> str:
        xx = ",".join([f"{k}:{v}" for d in a for k, v in d.items()])
        yy = ",".join([f"{k}: {i}" for k, v in b.items() for i in v])
        if isinstance(c, list):
            zz = ",".join([f"{k}:{v}" for d in c for k, v in d.items()])
        elif isinstance(c, dict):
            zz = ",".join([f"{k}: {i}" for k, v in c.items() for i in v])
        else:
            zz = str(c)
        return f"First: {xx} Second: {yy} Third: {zz} Int: {d}"

    @task
    def get_int() -> int:
        return 1

    @workflow
    def subwf(
        a: typing.List[typing.Dict[str, typing.List[int]]],
        b: typing.Dict[str, typing.List[int]],
        c: typing.Union[typing.List[typing.Dict[str, typing.List[int]]], typing.Dict[str, typing.List[int]]],
        d: int,
    ) -> str:
        return t1l(a=a, b=b, c=c, d=d)

    @workflow
    def wf() -> str:
        ds = [
            {"first_map_a": [42], "first_map_b": [get_int(), 2]},
            {
                "second_map_c": [33],
                "second_map_d": [9, 99],
            },
        ]
        ll = {
            "ll_1": [get_int(), get_int(), get_int()],
            "ll_2": [4, 5, 6],
        }
        out = subwf(a=ds, b=ll, c=ds, d=get_int())
        return out

    wf.compile()
    x = wf()
    expected = (
        "First: first_map_a:[42],first_map_b:[1, 2],second_map_c:[33],second_map_d:[9, 99] "
        "Second: ll_1: 1,ll_1: 1,ll_1: 1,ll_2: 4,ll_2: 5,ll_2: 6 "
        "Third: first_map_a:[42],first_map_b:[1, 2],second_map_c:[33],second_map_d:[9, 99] "
        "Int: 1"
    )
    assert x == expected
    wf_spec = get_serializable(OrderedDict(), serialization_settings, wf)
    assert set(wf_spec.template.nodes[5].upstream_node_ids) == {"n2", "n1", "n0", "n4", "n3"}

    @workflow
    def wf() -> str:
        ds = [
            {"first_map_a": [42], "first_map_b": [get_int(), 2]},
            {
                "second_map_c": [33],
                "second_map_d": [9, 99],
            },
        ]
        ll = {
            "ll_1": [get_int(), get_int(), get_int()],
            "ll_2": [4, 5, 6],
        }
        out = subwf(a=ds, b=ll, c=ll, d=get_int())
        return out

    x = wf()
    expected = (
        "First: first_map_a:[42],first_map_b:[1, 2],second_map_c:[33],second_map_d:[9, 99] "
        "Second: ll_1: 1,ll_1: 1,ll_1: 1,ll_2: 4,ll_2: 5,ll_2: 6 "
        "Third: ll_1: 1,ll_1: 1,ll_1: 1,ll_2: 4,ll_2: 5,ll_2: 6 "
        "Int: 1"
    )
    assert x == expected


def test_unexpected_outputs():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def no_outputs_wf():
        return t1(a=3)

    # Should raise an exception because the workflow returns something when it shouldn't
    with pytest.raises(FlyteValueException):
        no_outputs_wf()

@pytest.mark.skipif(sys.version_info < (3, 10, 10), reason="inspect module does not work correctly with Python <3.10.10. https://github.com/python/cpython/issues/102647#issuecomment-1466868212")
def test_missing_return_value():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    # Should raise an exception because it doesn't return something when it should
    with pytest.raises(FlyteMissingReturnValueException):

        @workflow
        def one_output_wf() -> int:  # type: ignore
            t1(a=3)

        one_output_wf()


def test_custom_wrapper():
    def our_task(
            _task_function: typing.Optional[typing.Callable] = None,
            **kwargs,
    ):
        def wrapped(_func: typing.Callable):
            return task(_task_function=_func)

        if _task_function:
            return wrapped(_task_function)
        else:
            return wrapped

    @our_task(
        foo={
            "bar1": lambda x: print(x),
            "bar2": lambda x: print(x),
        },
    )
    def missing_func_body() -> str:
        return "foo"


def test_wf_no_output():
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def no_outputs_wf():
        t1(a=3)

    assert no_outputs_wf() is None


def test_wf_nested_comp(exec_prefix):
    @task
    def t1(a: int) -> int:
        a = a + 5
        return a

    @workflow
    def outer() -> typing.Tuple[int, int]:
        # You should not do this. This is just here for testing.
        @workflow
        def wf2() -> int:
            return t1(a=5)

        return t1(a=3), wf2()

    assert (8, 10) == outer()
    entity_mapping = OrderedDict()

    model_wf = get_serializable(entity_mapping, serialization_settings, outer)

    assert len(model_wf.template.interface.outputs) == 2
    assert len(model_wf.template.nodes) == 2
    assert model_wf.template.nodes[1].workflow_node is not None

    sub_wf = model_wf.sub_workflows[0]
    assert len(sub_wf.nodes) == 1
    assert sub_wf.nodes[0].id == "n0"
    assert sub_wf.nodes[0].task_node.reference_id.name == f"{exec_prefix}tests.flytekit.unit.core.test_workflows.t1"


@task
def add_5(a: int) -> int:
    a = a + 5
    return a


@workflow
def simple_wf() -> int:
    return add_5(a=1)

@workflow
def my_wf_example(a: int) -> typing.Tuple[int, int]:
    '''example

    Workflows can have inputs and return outputs of simple or complex types.

    '''

    x = add_5(a=a)

    # You can use outputs of a previous task as inputs to other nodes.
    z = add_5(a=x)

    # You can call other workflows from within this workflow
    d = simple_wf()

    # You can add conditions that can run on primitive types and execute different branches
    e = conditional("bool").if_(a == 5).then(add_5(a=d)).else_().then(add_5(a=z))

    # Outputs of the workflow have to be outputs returned by prior nodes.
    # No outputs and single or multiple outputs are supported
    return x, e

    def test_workflow_lhs():
    assert my_wf_example._lhs == "my_wf_example"


def test_all_node_types():
    assert my_wf_example(a=1) == (6, 16)
    entity_mapping = OrderedDict()

    model_wf = get_serializable(entity_mapping, serialization_settings, my_wf_example)

    assert len(model_wf.template.interface.outputs) == 2
    assert len(model_wf.template.nodes) == 4
    assert model_wf.template.nodes[2].workflow_node is not None

    sub_wf = model_wf.sub_workflows[0]
    assert len(sub_wf.nodes) == 1
    assert sub_wf.nodes[0].id == "n0"
    assert sub_wf.nodes[0].task_node.reference_id.name == "tests.flytekit.unit.core.test_workflows.add_5"


def test_wf_docstring():
    model_wf = get_serializable(OrderedDict(), serialization_settings, my_wf_example)

    assert len(model_wf.template.interface.outputs) == 2
    assert model_wf.template.interface.outputs["o0"].description == "outputs"
    assert model_wf.template.interface.outputs["o1"].description == "outputs"
    assert len(model_wf.template.interface.inputs) == 1
    assert model_wf.template.interface.inputs["a"].description == "input a"


@pytest.mark.skipif("pandas" not in sys.modules, reason="Pandas is not installed.")
def test_structured_dataset_wf():
    import pandas as pd
    from pandas.testing import assert_frame_equal

    from flytekit.types.schema import FlyteSchema

    superset_cols = kwtypes(Name=str, Age=int, Height=int)
    subset_cols = kwtypes(Name=str)
    superset_df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22], "Height": [160, 178]})
    subset_df = pd.DataFrame({"Name": ["Tom", "Joseph"]})

    @task
    def t1() -> Annotated[pd.DataFrame, superset_cols]:
        return superset_df

    @task
    def t2(df: Annotated[pd.DataFrame, subset_cols]) -> Annotated[pd.DataFrame, subset_cols]:
        return df

    @task
    def t3(df: FlyteSchema[superset_cols]) -> FlyteSchema[superset_cols]:
        return df

    @task
    def t4() -> FlyteSchema[superset_cols]:
        return superset_df

    @task
    def t5(sd: Annotated[StructuredDataset, subset_cols]) -> Annotated[pd.DataFrame, subset_cols]:
        return sd.open(pd.DataFrame).all()

    @workflow
    def sd_wf() -> Annotated[pd.DataFrame, subset_cols]:
        # StructuredDataset -> StructuredDataset
        df = t1()
        return t2(df=df)

    @workflow
    def sd_to_schema_wf() -> pd.DataFrame:
        # StructuredDataset -> schema
        df = t1()
        return t3(df=df)

    @workflow
    def schema_to_sd_wf() -> typing.Tuple[pd.DataFrame, pd.DataFrame]:
        # schema -> StructuredDataset
        df = t4()
        return t2(df=df), t5(sd=df)  # type: ignore

    assert_frame_equal(sd_wf(), subset_df)
    assert_frame_equal(sd_to_schema_wf(), superset_df)
    assert_frame_equal(schema_to_sd_wf()[0], subset_df)
    assert_frame_equal(schema_to_sd_wf()[1], subset_df)


@pytest.mark.skipif("pandas" not in sys.modules, reason="Pandas is not installed.")
def test_compile_wf_at_compile_time():
    import pandas as pd

    from flytekit.types.schema import FlyteSchema

    superset_cols = kwtypes(Name=str, Age=int, Height=int)
    superset_df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [20, 22], "Height": [160, 178]})

    ctx = FlyteContextManager.current_context()
    with FlyteContextManager.with_context(
        ctx.with_execution_state(
            ctx.new_execution_state().with_params(mode=context_manager.ExecutionState.Mode.TASK_EXECUTION)
        )
    ):

        @task
        def t4() -> FlyteSchema[superset_cols]:
            return superset_df

        @workflow
        def wf():
            t4()

        assert ctx.compilation_state is None


@pytest.mark.parametrize(
    "error_message", [
        "Fail!",
        None,
        "",
        ("big", "boom!")
    ]
)
@patch("builtins.print")
def test_failure_node_local_execution(mock_print, error_message, exec_prefix):
    @task
    def clean_up(name: str, err: typing.Optional[FlyteError] = None):
        print(f"Deleting cluster {name} due to {err}")
        print("This is err:", str(err))

    @task
    def create_cluster(name: str):
        print(f"Creating cluster: {name}")

    @task
    def delete_cluster(name: str, err: typing.Optional[FlyteError] = None):
        print(f"Deleting cluster {name}")
        print(err)

    @task
    def t1(a: int, b: str):
        print(f"{a} {b}")
        raise ValueError(error_message)

    @workflow(on_failure=clean_up)
    def wf(name: str = "flyteorg"):
        c = create_cluster(name=name)
        t = t1(a=1, b="2")
        d = delete_cluster(name=name)
        c >> t >> d

    with pytest.raises(ValueError):
        wf()

    # Adjusted the error message to match the one in the failure
    expected_error_message = str(
        FlyteError(message=f"Error encountered while executing '{exec_prefix}tests.flytekit.unit.core.test_workflows.t1':
rror_message}", failed_node_id="fn0")
    )

    assert mock_print.call_count > 0

    mock_print.assert_any_call("Creating cluster: flyteorg")
    mock_print.assert_any_call("1 2")
    mock_print.assert_any_call(f"Deleting cluster flyteorg due to {expected_error_message}")
    mock_print.assert_any_call("This is err:", expected_error_message)
```


Again, users should keep in mind that even though the body of the function looks like regular Python, it is
actually not. When flytekit scans the workflow function, the objects being passed around between the tasks are not
your typical Python values. So even though you may have a task ``t1() -> int``, when ``a = t1()`` is called, ``a``
will not be an integer so if you try to ``range(a)`` you'll get an error.

Please see the :ref:`user guide <cookbook:workflow>` for more usage examples.



| Parameter | Type | Description |
|-|-|-|
| `_workflow_function` | `Optional[Callable[P, FuncOut]]` | This argument is implicitly passed and represents the decorated function. |
| `failure_policy` | `Optional[WorkflowFailurePolicy]` | Use the options in flytekit.WorkflowFailurePolicy |
| `interruptible` | `bool` | Whether or not tasks launched from this workflow are by default interruptible |
| `on_failure` | `Optional[Union[WorkflowBase, Task]]` | Invoke this workflow or task on failure. The Workflow / task has to match the signature of the current workflow, with an additional parameter called `error` Error |
| `docs` | `Optional[Documentation]` | Description entity for the workflow |
| `pickle_untyped` | `bool` | This is a flag that allows users to bypass the type-checking that Flytekit does when constructing the workflow. This is not recommended for general use. |
| `default_options` | `Optional[Options]` | Default options for the workflow when creating a default launch plan. Currently only the labels and annotations are allowed to be set as defaults. |

