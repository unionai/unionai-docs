# Execution time support

Most of the tasks that are written in Flytekit will be Python functions decorated with `@union.task`, which turns the body of the function into a Flyte task, capable of being run independently, or included in any number of workflows. The interaction between Flytekit and these tasks does not end once the tasks have been serialized and registered to the control plane, however. When compiled, the command that will be executed when the task is run is hardcoded into the task definition itself.

In the basic `@union.task`-decorated function scenario, the command to be run will be something containing `pyflyte-execute`, which is the open source version of the `union` CLI.

That command, if you were to inspect a serialized task, might look something like the following:

{{< highlight shell >}}
flytekit_venv pyflyte-execute --task-module app.workflows.failing_workflows --task-name divider --inputs {{.input}} --output-prefix {{.outputPrefix}} --raw-output-data-prefix {{.rawOutputDataPrefix}}
{{< /highlight >}}

The point of running this script, or rather the reason for having any Flyte-related logic at execution time, is purely to codify and streamline the interaction between Flyte the platform, and the function body comprising user code. The CLI is responsible for:

* Performing I/O. The templated `--inputs` and `--output-prefix` arguments in the example command above will be filled in by the Flyte execution engine with an S3 path (in the case of an AWS deployment). The `pyflyte` script will download the inputs to the right location in the container, and upload the results to the `output-prefix` location.
* Ensuring that raw output data prefix configuration option, which is again filled in by the Flyte engine, is respected so that `FlyteFile`, `FlyteDirectory`, and `FlyteSchema` objects offload their data to the correct place.
* Capturing and handling error reporting. Exceptions thrown in the course of task execution are captured and uploaded to the Flyte control plane for display on the Console.
* Setting up helper utilities like the `statsd` handle, logging and logging levels, etc.
* Ensuring configuration options about the Flyte backend, which are passed through by the Flyte engine, are properly loaded in Python memory.
