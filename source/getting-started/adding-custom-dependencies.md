# Adding custom dependencies

With image builder, the Docker images used by your tasks are built in the cloud on Union.
For this example, save the following as `image_build.py`

```{code-block} python
from flytekit import ImageSpec, task, workflow

image = ImageSpec(
    builder="unionai",
    packages=["numpy==1.26.4"],
)

@task(container_image=image)
def fn() -> int:
    import numpy as np
    x = np.array([1, 2, 3])
    return int(x.sum())

@workflow
def main() -> int:
    return fn()

```

This example contains an `ImageSpec` that specifies the dependencies of the `@task`. We
set `builder="unionai"` to configure `ImageSpec` to build the image on our hosted image
builder. Next, run run the `image_build.py` script to see how it works:

```{code-block} shell
unionai run --remote image_build.py main
```

This command will start up an image builder task on Flyte:

```{code-block} shell
👍 Build submitted!
⏳ Waiting for build to finish at: https://serverless-1.us-east-2.s.union.ai/org/cosmicbboy/projects/default/domains/development/executions/EXECUTION_ID
```

After the build is complete, then the original workflow will run with the newly created image!
