# UnionRemote

```{eval-rst}
===========
UnionRemote
===========

The UnionRemote module provides utilities for performing operations on tasks, workflows, launchplans, and executions. For example, the following code fetches and executes a workflow:

.. code-block:: python

    # create a remote object from flyte config and environment variables
    UnionRemote(config=Config.auto())
    UnionRemote(config=Config.auto(config_file=....))
    UnionRemote(config=Config(....))

    # Or if you need to specify a custom cert chain
    # (options and compression are also respected keyword arguments)
    UnionRemote(private_key=your_private_key_bytes, root_certificates=..., certificate_chain=...)

    # fetch a workflow from the Union backend
    remote = UnionRemote(...)
    union_workflow = remote.fetch_workflow(name="my_workflow", version="v1")

    # execute the workflow, wait=True will return the execution object after it's completed
    workflow_execution = remote.execute(union_workflow, inputs={"a": 1, "b": 10}, wait=True)

    # inspect the execution's outputs
    print(workflow_execution.outputs)

.. _remote-entrypoint:

Entrypoint
==========


.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   ~unionai.remote.UnionRemote
   ~flytekit.remote.remote.Options

.. _remote-flyte-entities:

Entities
========

.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   ~flytekit.remote.entities.FlyteTask
   ~flytekit.remote.entities.FlyteWorkflow
   ~flytekit.remote.entities.FlyteLaunchPlan

.. _remote-flyte-entity-components:

Entity Components
=================

.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   ~flytekit.remote.entities.FlyteNode
   ~flytekit.remote.entities.FlyteTaskNode
   ~flytekit.remote.entities.FlyteWorkflowNode

.. _remote-flyte-execution-objects:

Execution Objects
=================

.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   ~flytekit.remote.executions.FlyteWorkflowExecution
   ~flytekit.remote.executions.FlyteTaskExecution
   ~flytekit.remote.executions.FlyteNodeExecution

```