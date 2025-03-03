# Reference launch plans

A reference launch plan references previously defined, serialized, and registered launch plans. You can reference launch plans from other projects and create workflows that use launch plans declared by others.

When you create a reference launch plan, be sure to verify that the workflow interface corresponds to that of the referenced workflow.

```--note--
Reference launch plans cannot be run locally. To test locally, mock them out.
```

## Example

In this example, we create a reference launch plan for the [`simple_wf`](https://github.com/flyteorg/flytesnacks/blob/master/examples/basics/basics/workflow.py#L25) workflow from the [Flytesnacks repository](https://github.com/flyteorg/flytesnacks).

1. Clone the Flytesnacks repository:

{{< highlight shell >}}
git clone git@github.com:flyteorg/flytesnacks.git
{{< /highlight >}}

2. Navigate to the `basics` directory:

{{< highlight shell >}}
cd flytesnacks/examples/basics
{{< /highlight >}}

3. Register the `simple_wf` workflow:

{{< highlight shell >}}
union register --project flytesnacks --domain development --version v1 basics/workflow.py.
{{< /highlight >}}


4. Create a file called `simple_wf_ref_lp.py` and copy the following code into it:

{{< highlight python >}}
import union
from flytekit import reference_launch_plan


@reference_launch_plan(
    project="flytesnacks",
    domain="development",
    name="basics.workflow.simple_wf",
    version="v1",
)
def simple_wf_lp(
    x: list[int], y: list[int]
) -> float:
    return 1.0


@union.workflow
def run_simple_wf() -> float:
    x = [-8, 2, 4]
    y = [-2, 4, 7]
    return simple_wf_lp(x=x, y=y)
{{< /highlight >}}


5. Register the `run_simple_wf` workflow:

{{< highlight shell >}}
union register simple_wf_ref_lp.py
{{< /highlight >}}

6. In the Union UI, run the workflow `run_simple_wf`.

