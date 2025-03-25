---
title: Jupyter notebooks
weight: 18
variants: +flyte +serverless +byoc +byok
---

# Jupyter notebooks

{{< key product_name >}} supports the development, running, and debugging of tasks and workflows in an interactive Jupyter notebook environment, which accelerates the iteration speed when building data- or machine learning-driven applications.

To enable 
Create an interactive FlyteRemote object
In Running and Scheduling Workflows, you learned how to run registered Flyte workflows from a Python runtime using the FlyteRemote client.

When developing workflows in a Jupyter notebook, FlyteRemote provides an interactive interface to register and run workflows on a Flyte cluster. Let’s create an interactive FlyteRemote object:

from flytekit.configuration import Config
from flytekit.remote import FlyteRemote

remote = FlyteRemote(
    config=Config.auto(),
    default_project="flytesnacks",
    default_domain="development",
    interactive_mode_enabled=True,
)
Note

The interactive_mode_enabled flag is automatically set to True when running in a Jupyter notebook environment, enabling interactive registration and execution of workflows.

Running a task or a workflow
You can run entities (tasks or workflows) using the FlyteRemote execute() method. During execution, flytekit first checks if the entity is registered with the Flyte backend, and if not, registers it before execution.

execution = remote.execute(my_task, inputs={"name": "Flyte"})
execution = remote.execute(my_wf, inputs={"name": "Flyte"})
You can then fetch the inputs and outputs of the execution by following the steps in Fetching inputs and outputs of an execution.

When Does Interactive FlyteRemote Re-register an Entity?
The interactive FlyteRemote client re-registers an entity whenever it’s redefined in the notebook, including when you re-execute a cell containing the entity definition, even if the entity remains unchanged. This behavior facilitates iterative development and debugging of tasks and workflows in a Jupyter notebook.