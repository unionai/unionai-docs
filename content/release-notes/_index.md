---
title: Release notes
weight: 6
variants: +byoc +selfmanaged -flyte
top_menu: true
sidebar_expanded: true
---

# Release notes

{{< variant byoc selfmanaged >}}
{{< markdown >}}

## February 2026

### :sparkles: JSON Schema Enhancement

Flyte now accurately converts Python types to JSON Schemas by leveraging Flyte's internal type system. Previously, certain types, like `Literal["C", "F"]`, were incorrectly mapped. Now, input schemas for Flyte tasks will reflect comprehensive and precise JSON Schemas, improving integrations with tools like Anthropic's Claude. This adjustment ensures that parameters such as enums, dataclasses, and Flyte-native types generate the correct JSON types, enhancing task definition clarity and facilitating seamless tool usage.

```python
# Example: Converting Literal to JSON Schema correctly
def my_func(unit: Literal["C", "F"]) -> str:
    return unit

schema = NativeInterface.from_callable(my_func).json_schema
assert schema["properties"]["unit"] == {"type": "string", "enum": ["C", "F"]}
```

### :calculator: Panel Calculator Example

You can now experiment with building interactive Panel applications using Flyte's `AppEnvironment`. The new example showcases a calculator app embedded in a Panel interface, providing a hands-on learning experience with Flyte's capabilities for developing web-based UIs. This update further highlights Flyte's versatility in handling both data-centered and interactive applications in a seamless environment.

### :sparkles: Spark Plugin Update

You can now specify stable releases when using the Spark plugin in Flyte. The dependency for `flyteplugins-spark` has been updated to version `>=2.0.0`, providing enhanced stability by moving away from pre-release versions. This update ensures a more reliable experience when building and running Spark tasks within Flyte workflows.

### :lock: Secure Package Specification

You can now safely specify package versions in your Flyte SDK Docker builds, thanks to improved handling of version constraints. Previously, specifying package constraints like `apache-airflow<=3.0.0` without quotes could result in incorrect Dockerfile interpretation. Now, version constraints are automatically quoted, ensuring correct parsing and preventing build failures. This update makes your Docker image builds more robust, helping you avoid common pitfalls related to shell command execution in Dockerfiles.

### :zap: Enum Name Acceptance in CLI

You can now use enum names as valid inputs in the Flyte CLI. Previously, Flyte required enum values for command-line inputs, causing errors when users provided names instead (e.g., `"RED"` instead of `"red"`). This update aligns CLI behavior with the Flyte internals, accepting both enum names and values, enhancing usability and consistency for workflow authors. 

```python
import enum
from flyte import flyte

class Color(enum.Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

@flyte.task
def example_task(color: Color):
    return f"Selected color is {color.name}"
```

Now, when executing workflows via the CLI, providing names like `--color=RED` is smoothly handled without errors.

### :wrench: Enhanced Pod Template Handling

This update ensures pod templates are properly maintained across task overrides. Previously, overriding certain task attributes could inadvertently discard custom pod templates, impacting task execution environments. You can now rest assured that pod specifications, labels, and annotations will persist, even after renaming tasks or modifying other properties. This enhancement is especially beneficial for workflows requiring consistent environments across variations, ensuring accurate resource and configuration retention without manual intervention.

### :zap: Stress Testing Example Added

A new stress testing example has been added to Flyte SDK, allowing you to simulate high concurrency scenarios. This example demonstrates a fan-out execution pattern, creating a dynamic tree of asynchronous tasks that simulates a load. Users can control the number of tasks spawned at each layer and introduce variability in task execution time with a jitter parameter, providing a powerful tool for testing system resilience under load.

### :bug: Correct Serialization Field

The PR fixes a bug in the serialization of scaling metrics by using the correct field `target_value` instead of the incorrect `val`. This change ensures proper serialization behavior for the `Scaling.Concurrency` and `Scaling.RequestRate` metrics as expected by the protobuf definitions. This update might prevent potential runtime errors for users relying on correct metric serialization in their applications.

### :wrench: Improved Async Task Handling

Async Flyte tasks now route execution through `task.aio()`, enhancing task invocation consistency with Flyte's controller. This improvement ensures that nested async tasks are managed correctly within the Flyte framework, providing a more seamless experience for users working with asynchronous workflows.

### :wrench: Sync Alignment of File Upload Methods

The methods `File.from_local_sync` and `File.from_local` now ensure consistent filename handling when uploading files to remote storage. Previously, there was a discrepancy in filename assignment between the asynchronous and synchronous upload methods that could lead to naming inconsistencies. This change aligns their behavior, making the name preservation consistent regardless of the upload method used.

```python
# Example of uploading a file with consistent naming:
import flyte

with tempfile.TemporaryDirectory() as temp_dir:
    local_path = os.path.join(temp_dir, "source.txt")
    remote_path = os.path.join(temp_dir, "destination.txt")

    # Ensure the file content
    with open(local_path, "w") as f:
        f.write("sample content")

    # Upload the local file to a remote location
    uploaded_file = File.from_local_sync(local_path, remote_path)

    print(f"Uploaded file path: {uploaded_file.path}")
```

### :hourglass: Request Timeout Configuration

You can now configure request timeouts for Flyte applications using the new `Timeouts` dataclass. This enhancement allows you to set a `request` timeout (as an integer or `timedelta`) that determines the maximum duration a request can take within an application environment. Users can specify timeouts during environment configuration, ensuring that requests do not exceed the defined limits and can be reset using cloning methods. This feature enhances reliability by preventing excessively long execution times and provides flexibility in managing service responsiveness.

### Context and Changes
The changes made in PR #717 involve two main updates:
1. **Standard Ignore Pattern Update**: `.git` has been added to the standard ignore patterns in the `_ignore.py` file. This modifies the behavior of code bundling by excluding `.git` directories from being included.
   
2. **Bundle Logic Adjustment**: In the `bundle.py` and `_deploy.py` files, logic is added to handle the `copy_style` parameter. If `copy_style` is set to "none", a `ValueError` is now raised with a message instructing not to make a code bundle. This prevents unnecessary bundling operations when no copying is required.

3. **Test Additions**: Tests are added to ensure that files and directories like `.git` are ignored during the file copy process.

### User-Facing Impact
These changes directly impact users who interact with Flyte's SDK in the following ways:
- **Improved Code Bundling**: By ignoring `.git` directories, users experience faster bundling operations and reduced artifact sizes, improving the efficiency of deployments.
  
- **Error Awareness**: The introduction of explicit error handling for the `copy_style` parameter clarifies user expectations and reduces confusion about bundling behaviors.

### Documentation and Release Note

This change is indeed user-facing as it affects how users manage their code deployments and provides clearer handling of code bundling configurations. Now let's frame a release note entry.

### :wrench: Enhanced Bundling and Error Handling

You can now enjoy faster bundling operations in Flyte by ignoring `.git` directories in deployment code bundles. This update optimizes the bundling process, reducing artifact size and improving deployment efficiency. Additionally, explicit error handling for the `copy_style` parameter ensures clear guidance when bundling is unnecessary.

### :wrench: Dynamic Pydantic Model Creation

This update introduces a new feature in the Flyte SDK, allowing dynamic creation of Pydantic models from JSON schema metadata through the `PydanticTransformer.guess_python_type` method. This functionality enables users to handle situations where the original Pydantic model class isn't available, facilitating more flexible serialization and deserialization processes. Users can now seamlessly work with Pydantic models within Flyte tasks, leveraging the ability to map back to Python types even when dealing with complex nested structures.

### :busts_in_silhouette: Human-in-the-Loop Plugin

The new Human-in-the-Loop (HITL) plugin for Flyte enables workflows to pause and wait for human input via a web interface or programmatically. You can create events that invite human interaction through an auto-served FastAPI app, making your workflows interactive. This feature is designed for use cases where workflows require human decision-making to proceed, enhancing the flexibility and interactivity of your data processes. 

```python
import flyteplugins.hitl as hitl

# Create event and wait for human input
event = await hitl.new_event.aio(
    "input_event",
    data_type=int,
    scope="run",
    prompt="Enter a number"
)
value = await event.wait.aio()
```

This plugin is perfect for asynchronous workflows needing occasional manual intervention without constant human oversight.

### :rocket: Stateless Code Sandbox

Flyte now supports running arbitrary Python code and shell commands in an isolated, stateless Docker container with the `flyte.sandbox.create()` API. This powerful feature offers three execution modes: Auto-IO, Verbatim, and Command, each providing flexibility in handling inputs and outputs while ensuring the code runs in fresh, ephemeral containers. This sandboxing capability is particularly useful for tasks requiring containerized execution without dependencies on the host environment, further enhancing Flyte's modularity and reliability.

### :wrench: Improved CLI Logging Initialization

The Flyte SDK now ensures a consistent logging setup when using the CLI. Previously, invoking Flyte CLI commands would inadvertently initialize the configuration multiple times, leading to duplicated log entries. With this update:

- Initialization occurs precisely once per command execution, streamlining log outputs.
- Enhanced logging clarity is achieved by enabling `RichHandler` from the start, allowing all logs to display in rich format.
- A default value is now provided in the `hello.py` example script, enabling it to run without arguments.

These changes ensure a cleaner, more informative logging experience during command execution, benefiting all Flyte CLI users by providing clearer insights without unnecessary log duplication.

```python
@env.task
def main(x_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> float:
    x_len = len(x_list)
    if x_len < 10:
        raise ValueError(f"x_list doesn't have a larger enough sample size, found: {x_len}")
    y_list = list(flyte.map(fn, x_list))
    y_mean = sum(y_list) / len(y_list)
    return y_mean
```

### :wrench: Enhanced Ignore Handling

Flyte SDK now intelligently skips processing of `.gitignore` and `.flyteignore` files inside directories commonly ignored, such as `.venv` or `__pycache__`. This prevents unnecessary file processing and aligns with typical developer workflows, ensuring only the relevant files are considered during operations. The update simplifies code management and speeds up task execution by avoiding redundant checks in standard-ignored directories.

### :whale: CI Image Builder

You can now automate Docker image building and pushing directly from CI with the new example script. This feature allows seamless integration with continuous deployment pipelines, ensuring that images are consistently built and pushed to desired registries. Simply configure the script with your source and target image details.

### :wrench: TypedDict Compatibility Fix

The Flyte SDK now correctly handles `TypedDict` usage for Python versions earlier than 3.12, using `typing_extensions.TypedDict`. This ensures that users on older Python versions can continue to define and utilize `TypedDict` in their workflows, maintaining compatibility and enabling the usage of complex data structures in Flyte tasks.

```python
# Importing TypedDict based on Python version
import sys
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict
```

### :globe_with_meridians: Cross-Platform Code Bundling

The Flyte SDK now ensures consistent cross-platform behavior for code bundling. By using POSIX-style paths for file hashing and tarball creation, tasks now behave consistently between Windows and Unix systems, preventing subtle bugs. This change ensures that users working across different OS environments can rely on consistent processing and file integrity, improving the overall development experience on Flyte.

The pull request focuses on improving the robustness of the app deployment watching logic in the Flyte SDK. Specifically, it ensures that the `watch` function in `src/flyte/remote/_app.py` now handles delayed status updates more gracefully by waiting for status conditions to be present before proceeding. This prevents potential race conditions or errors when status updates are delayed.

After reviewing the diff, reading the source code, and checking for related examples, the change primarily affects internal logic handling and is not directly user-facing. It doesn’t introduce new API changes, features, or behaviors that users would interact with differently.

Based on the information gathered, there are **NO_USER_FACING_CHANGES** to document for this PR.

### :wrench: Improved CLI JSON Formatting

You can now run CLI commands that output JSON without encountering errors caused by non-iterable object types. The `flyte` CLI smartly utilizes the `to_dict()` method when available, fixing issues where certain commands would previously fail with a `TypeError`. This enhancement improves CLI stability and user experience when dealing with complex objects.

### :wrench: Improved Pod Image Handling

This update enhances how Flyte handles container images when using a pod template. You can now rely on consistent image merging, where the primary container will use the `app_env.image` if no explicit image is set, ensuring flexibility with `"auto"` and specific image values. This behavior is verified by additional tests in the SDK.

### :sparkles: Flyte Webhook Environment

You can now leverage a pre-built Flyte webhook environment, making it easier to integrate with FastAPI endpoints for common Flyte operations. This update simplifies tasks like running tasks, managing apps, and handling triggers. Enhancements include using `httpx` for modern HTTP requests and expanding endpoint exports for better customization. This streamlines deploying and managing Flyte tasks and environments using webhooks. 

This new functionality supports developers by simplifying webhook deployment and management, adding robustness to remote app operations, and enabling easier testing with new example scripts.

### :repeat: Retry Interceptor for gRPC

A new retry interceptor has been implemented for gRPC channels in Flyte, allowing users to define how many times a gRPC call should be retried in case of transient failures. This feature helps ensure more robust connectivity and improved reliability when Flyte interacts with remote services over gRPC. You can specify the number of retry attempts using the `rpc_retries` option during channel creation, with sensible defaults provided by the SDK.

### :sparkles: Orchestration Sandbox Feature

Flyte 2.0 now supports dynamic orchestration within a sandbox using the `flyte.sandbox.orchestrator_from_str()` method. This feature allows you to create reusable orchestration templates directly from Python code strings, making it easier to build lightweight pipelines without defining decorated functions. It is particularly beneficial for scenarios where code is dynamically generated, such as from UIs or language models, or when you need to run code snippets in a secure, isolated environment.

### :wrench: Task Shortname Override Fix

You can now override the shortname for tasks in the UI by setting the `short_name` parameter when using task overrides. This resolves an issue where overridden shortnames were not reflected in the Flyte UI, enhancing task configurability and visibility.

### :sparkles: NVIDIA H100 GPU Support

You can now configure tasks to use NVIDIA H100 GPUs in your Flyte workflows. This release introduces support for various H100 MIG partitions, allowing fine-grained resource allocation for distributed AI workloads. Integrating H100 GPUs enables enhanced performance for machine learning models requiring significant computational power.

```python
from flyte import GPU, Resources

h100_mig_env = flyte.TaskEnvironment(
    name="h100_mig",
    resources=Resources(
        cpu="1",
        memory="4Gi",
        gpu=GPU(device="H100", quantity=1, partition="1g.10gb"),
    ),
)
```

With this capability, users can specify H100 partitions directly, optimizing resource usage according to their workload needs.

### :zap: Enhanced Error Handling in PyTorch Elastic Jobs

Flyte's PyTorch integration now includes configurable NCCL timeout settings to better manage CUDA out-of-memory (OOM) situations. This update prevents PyTorch elastic jobs from hanging due to OOM by introducing a faster failure detection mechanism and customizable restart policies. New settings allow you to reduce timeout durations, enable asynchronous error handling, and activate built-in monitoring, ensuring more efficient error recovery and minimizing downtime in distributed training environments. These enhancements provide greater control over job execution and resilience against GPU memory limitations.

### :wrench: Reverse Path Priority Fix

The Flyte SDK's handling of `sys.path` when running tasks remotely has been improved to respect the path priority set on your local environment. Previously, the `entrypoint` directory could override top-level packages, potentially leading to unexpected behavior. This fix ensures consistent path prioritization between local development and remote execution, improving reliability when running workflows.

### :globe_with_meridians: S3 Virtual Hosted-Style Support

You can now specify the addressing style for S3-compatible backends in the Flyte SDK. By setting the `FLYTE_AWS_S3_ADDRESSING_STYLE` environment variable to `virtual`, URLs are constructed in the format `https://<bucket>.<endpoint>/<key>`, allowing compatibility with more storage providers. This addition ensures greater flexibility and integration options for Flyte users leveraging S3-compatible storage solutions.


## March 2026

The GitHub pull request #775 focused on modifying a workflow to no longer use the `--prerelease allow` flag when running `uv` commands for building and publishing plugins. This change is reflected in the `.github/workflows/publish.yml` file. The change is part of the CI configuration and affects how pre-release plugins are handled during publishing.

Now I will explore the source code of the Flyte SDK in the `./flyte-sdk-v2.0.6/` directory to further understand the context of these changes and check if there are any user-facing implications.
The PR doesn't introduce any changes to user-facing code or functionality in the Flyte SDK. It strictly modifies a GitHub Action workflow configuration, specifically removing the `--prerelease allow` flag during the plugin build and publish process. This change ensures that non-prerelease versions of plugins are published.

Since it is a modification of CI/CD processes with no direct impact on user-visible features or APIs, there are no user-facing changes to document in the Union docs. 

NO_USER_FACING_CHANGES

This pull request updates plugin "uv lock" files related to dependencies. The changes are mostly to the lock files, which means they handle updates to the dependency versions. This is typically an internal maintenance activity ensuring updates to dependencies do not unexpectedly change behavior. Given this context and the absence of any explanation about new features or user-facing changes, there is nothing explicitly visible to users or changing the SDK interface. 

Therefore, the outcome is:

```
NO_USER_FACING_CHANGES
```

### :wrench: Extended Idle Timeout for Panel Apps

Flyte now allows longer idle times for websocket connections in panel apps. This update increases session token expiration to 3 hours, allowing users more time for interaction without disconnection. Additionally, new parameters for managing unused session lifetimes improve the overall stability and performance of long-running applications. Users can experience smoother sessions when interacting with Flyte panel applications.

### :wrench: Plugin Variants Documentation

You can now generate variant-scoped CLI documentation using the new `--plugin-variants` flag in `flyte gen docs`. This option allows you to wrap plugin-contributed CLI commands in Hugo `{{< variant >}}` shortcodes, helping differentiate core and plugin commands in documentation. Core commands appear unconditionally, while plugin commands are shown only in specified variants (e.g., 'byoc', 'selfmanaged'). This feature enables a clean and organized display of CLI documentation across different deployment modes.

### :rocket: Google Gemini Plugin Integration

You can now integrate Google's Gemini API with Flyte, allowing Flyte tasks to be seamlessly used as tools within Gemini agents. This advancement introduces the `function_tool` decorator for automatic conversion of Flyte tasks, supporting both synchronous and asynchronous operations. Additionally, the new `Agent` class offers configurations for integrating with Gemini models, enhancing task orchestration and execution management. This feature empowers users to leverage Gemini's capabilities, providing flexibility and efficiency in model selection and task integration across different providers. 

```python
import flyte
from flyteplugins.gemini import function_tool, run_agent

env = flyte.TaskEnvironment("gemini-agent")

@env.task
async def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

# Run Gemini agent with a tool
async def agent_task(prompt: str):
    tools = [function_tool(get_weather)]
    return await run_agent(prompt=prompt, tools=tools, model="gemini-2.5-flash")
```

This addition bolsters Flyte's extensibility and adaptability in handling complex AI workflows.

The pull request implements a new step in the CI process to check for stale lock files. It adds a check for `uv.lock` files within each `plugins/*/` directory, enhancing the entire project’s build stability but does not impact user-facing features or APIs.

**Conclusion:** This change does not affect users directly through updated features or APIs.

```
NO_USER_FACING_CHANGES
```

### :hammer: Forced Image Build Caching

With this update, you can now force a rebuild of images by setting `force=True`. This skips the existence check and forces a rebuild even if the image already exists. When using the remote image builder, this also sets `overwrite_cache=True`, ensuring that the cache is overwritten during the build run. This feature is particularly useful for developers who need to ensure that the latest changes are included in every build, improving the efficiency and reliability of the build process.

```python
import flyte

image = flyte.Image("your_image")
result = await flyte.build.aio(image, force=True)
```

The pull request adds comprehensive module-level docstrings and improves class/field documentation for various plugins, which enhances the API references on the Union.ai documentation site. However, these changes are primarily internal and related to documentation updates rather than functionality that would directly impact the user experience or require users to alter their workflows or code.

Therefore, the changes are internal with no user-facing impact or new features, so there are no user-facing changes worth documenting in the release notes.

NO_USER_FACING_CHANGES

### :computer: LLM-Powered Code Generation

You can now use the `flyteplugins-codegen` plugin to generate code from natural language prompts, run tests, and iterate in isolated sandboxes using LLMs. The plugin supports Python code generation and integrates seamlessly with various execution backends, ensuring robust and error-free code generation processes.

```python
from flyteplugins.codegen import AutoCoderAgent

agent = AutoCoderAgent(model="gpt-4.1", name="data-processor", resources=flyte.Resources(cpu=1, memory="1Gi"))

result = await agent.generate.aio(
    prompt="Process the CSV data to calculate total revenue and units.",
    samples={"sales": csv_file},
    outputs={"total_revenue": float, "total_units": int},
)
```

This advancement opens new avenues for rapid development and testing in automated deployments.

### :wrench: Updated AI Plugin Examples

We've fixed and improved the plugin examples for working with OpenAI and Anthropic within Flyte 2.0. Now, users can efficiently run real-world tasks by employing an agent pattern with updated versions of `flyteplugins-openai` and `flyteplugins-anthropic`. This update ensures better compatibility and ease of use, especially in orchestrating complex workflows using AI tools.

```python
from flyteplugins.openai.agents import function_tool

agent_env = flyte.TaskEnvironment(
    "openai-agent",
    resources=flyte.Resources(cpu=1),
    secrets=[flyte.Secret(key="niels_openai_api_key", as_env_var="OPENAI_API_KEY")],
)

@function_tool
@agent_env.task
async def get_bread() -> str:
    await asyncio.sleep(1)
    return "bread"
```

### :wrench: Debug Mode Integration

The Flyte SDK now supports a `--debug` flag allowing users to initiate tasks in VS Code debug mode directly from the CLI or Python interface. By specifying `debug=True` in the `flyte.with_runcontext` method, a VS Code Debugger can be activated, enhancing troubleshooting capabilities during task execution. This feature provides an interactive debugging environment, making it easier for developers to diagnose issues in real time. 

```python
import flyte

env = flyte.TaskEnvironment(name="debug_example")

@env.task
def say_hello(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting

if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.with_runcontext(debug=True).run(say_hello, name="World")
    print(run.name)
    print("Run url", run.url)
    print("Waiting for debug url...")
    print("Debug url", run.get_debug_url())
```

This addition significantly enhances the developer experience, making debugging within the Flyte platform more efficient and accessible.

Based on the code diff and documentation, the pull request adds a new feature that introduces support for running arbitrary Python scripts on remote Flyte clusters. This includes a command-line interface option that allows users to define and execute scripts with configurable resources such as CPU, memory, and GPU. It includes both the API and CLI for facilitating this new capability.

I'll now draft the release note entry for this feature.

### PR Description
The pull request addresses an issue where the SDK would unnecessarily attempt OAuth2/PKCE authentication even when `insecure=True`, leading to unwanted keyring access and OAuth2 metadata fetches against servers that don't require authentication. The change ensures that when a plaintext channel is created with `insecure=True`, the SDK skips creating authentication interceptors entirely.

### Code Changes
- **Channel Creation Update**: The `create_channel()` function in `src/flyte/remote/_client/auth/_channel.py` now includes a conditional check for `insecure=True` to avoid setting up OAuth2/PKCE authentication interceptors.
- **Test Enhancements**: Two new tests verify that authentication interceptors are skipped when creating an insecure channel, ensuring that unnecessary authentication operations are avoided.

### Test Additions
- Tests ensure that authentication interceptors are not created when `insecure=True`, even when an explicit `auth_type` is specified.

## Impact on Users
- **User-Facing Benefit**: Users can configure channels to skip authentication interceptors when communicating with servers that don't require it, potentially improving connection speeds and eliminating unnecessary errors related to authentication processes in specific environments.

### Example Scenario
Consider a scenario where developers work with a local development server that doesn't require authentication. With this change, setting `insecure=True` means developers won't encounter authentication overhead, making local development simpler and faster.

Based on this analysis, I will draft the release note entry for this change.

### :sparkles: Improved CLI Enum Support

You can now utilize enum names directly when passing parameters via the Flyte CLI, thanks to support for `EnumParamType`. Previously, only enum values were recognized, which could lead to user confusion. This improvement makes CLI interactions more intuitive, as you can use friendly enum names like `--color=GREEN` instead of requiring specific internal values. This change enhances usability and aligns with previous updates that prioritize enum names in other components of the Flyte SDK.

### :memo: Programmatic Log Access

You can now access logs programmatically in Flyte by using the `get_logs()` method on `remote.Run` and `remote.Action`. This addition provides an iterator over log lines, enabling asynchronous processing with `.aio()`. The feature supports filtering system-generated logs and including timestamps. This enhancement is particularly useful for users needing to consume logs in code rather than manually viewing them in the terminal.

### :zap: Simplified PyTorch Example Setup

You can now streamline your PyTorch environment setup by specifying `flyteplugins-pytorch` directly via `with_pip_packages`. This change replaces the internal `PythonWheels` API, simplifying both example usage and development setups.

### :chart_with_upwards_trend: Distributed Training Evaluation

Flyte now supports distributed training with callback-driven evaluation. This feature enables users to automatically trigger evaluation tasks after each training checkpoint, using Flyte's EvalOnCheckpointCallback. This setup not only runs evaluations in parallel to the training process but also monitors model convergence. Upon convergence, a stop signal is generated to gracefully halt training, optimizing resource usage. This advancement is crucial for efficient resource management and quick iterations during model development.

### :zap: Improved Benchmark Flexibility

The benchmark script for Flyte's large I/O operations has been refactored for enhanced flexibility and maintainability. Users can now parameterize CPU and memory allocations, making resource management more intuitive. The benchmark tests are more flexible, permitting optional execution of file and directory tests. Additionally, the HTML report generation is now robust against missing data, ensuring comprehensive results. This update allows for more efficient benchmarking within Flyte, enhancing user control over testing parameters.

The PR involves increasing code coverage to ensure user-facing APIs remain consistent. It primarily adds unit tests to various components of the Flyte SDK. These tests cover `Cache`, `Environment`, and other user API components. Since these changes do not introduce new user-facing features or modifications that end users would notice during normal operations, it's essentially about enhancing internal code quality and stability.

Given the nature of the changes, this does not require a user-facing release note.

```
NO_USER_FACING_CHANGES
```

### :computer: CLI Project Management

You can now create, update, and manage Flyte projects directly from the CLI. This new feature allows you to create projects with specific IDs, names, descriptions, and labels, offering a streamlined way to manage project metadata. Users can also archive or unarchive projects, providing better control over project lifecycle states.

```bash
# Example usage
flyte create project --id my_project_id --name "My Project" --description "Project description" -l team=dev -l env=prod
flyte update project my_project_id --archive
flyte get project --archived
``` 

This enhancement simplifies project management tasks and provides more flexibility in organizing and maintaining projects.

The pull request primarily focuses on updates to plugins and continuous integration (CI) tests and does not introduce any user-facing changes. It concerns:

- Adding missing plugins to the testing and publishing workflows.
- Adjustments to port configurations and parameter definitions.
- Adding the `kubernetes` dependency in the Spark plugin's development requirements.
- Modifications to how parameters are accessed in some plugins, changing from `inputs` to `parameters`.

Given these changes are related to internal tests, CI configuration, and minor development dependencies without directly affecting user interactions with the SDK, there are no user-facing changes that require documentation.

NO_USER_FACING_CHANGES

### :robot: Anthropic Claude Integration

With this release, you can now seamlessly integrate Flyte tasks as tools for Anthropic Claude agents. This enhancement enables Claude to leverage Flyte's task orchestration capabilities, facilitating the automation of complex workflows. Users can define tasks in Flyte and convert them into Claude tool definitions, allowing for sophisticated agent-driven operations using the new `function_tool` utility.

```

### :hourglass_flowing_sand: Panel App Enhancements

The Flyte SDK panel app now includes UI updates and a new asynchronous execution model using threading. These changes improve user experience by allowing actions like code execution within the app to proceed without blocking the interface. Additionally, the integration of Reo.Dev tracking offers enhanced monitoring capabilities. Users can observe execution improvements and better app monitoring without needing toolchain adjustments, enabling more fluid task execution and insights directly from the app interface.

### :gear: AWS Config File Support

You can now configure S3 authentication using the `AWS_CONFIG_FILE` environment variable. This addition allows Flyte to utilize AWS profile-based authentication if both `AWS_PROFILE` and `AWS_CONFIG_FILE` are set, providing a boto3-backed credential provider. This change is particularly useful for users who prefer managing AWS credentials via configuration files, offering a seamless integration without the need for static credentials.

### :sparkles: Improved Task Execution Reliability

Flyte now automatically uses `task.aio()` for both synchronous and asynchronous tasks, ensuring consistent execution through the Flyte controller. This update removes the previous fallback to `asyncio.to_thread()` for synchronous tasks, enhancing reliability and integration within Flyte-defined contexts. You can achieve dependable task processing without altering your existing task definitions.

The PR adds a job to automatically discover plugins with `tests/` directories for unit testing in the CI workflow. This change dynamically updates the testing matrix without manual edits, ensuring new plugins are included seamlessly. It's a CI enhancement, not user-facing.

NO_USER_FACING_CHANGES

### :wrench: Enhanced Action Service Integration

This update introduces the ability to attach custom gRPC headers when interacting with the Actions service. Users leveraging workflows with gRPC endpoints can now maintain consistent request metadata, enabling more seamless integration and routing through complex systems. This change is particularly useful for ensuring actions are correctly associated and processed in distributed environments.

### :rocket: Async Training with Early Stopping

Explore a new ML pattern example that runs asynchronous training with periodic evaluations using Flyte's durable task management. The training task asynchronously saves checkpoints while evaluation tasks periodically assess convergence. If convergence is detected, the training gracefully stops. This update highlights graceful async handling, showcasing Flyte's advanced orchestration capabilities that enhance reliability in AI workflows.

```python
async def train(checkpoint_dir: str, total_epochs: int, seconds_per_epoch: float) -> File:
    # Training logic
    pass

async def evaluate(checkpoint_file: File, eval_round: int, convergence_loss: float) -> bool:
    # Evaluation logic
    pass

async def main(total_epochs, seconds_per_epoch, convergence_loss, eval_interval_seconds, max_eval_rounds):
    # Orchestration logic
    pass
```

Use `flyte run examples/ml/async_train_eval.py` to execute this pattern locally.

### :wrench: Improved Include Path Handling

Flyte now correctly resolves include paths relative to the app directory during deployment. Previously, using include paths that escaped the app script's directory caused deployment failures due to invalid tar entries. This fix ensures robust app bundling and deployment, improving the reliability of the `flyte serve` command in multi-directory projects.

### :zap: Enhanced Retry Management

The latest update introduces advanced support for managing task retries during local runs, featuring exponential backoff and detailed tracking of retry attempts. Users can benefit from a more resilient task execution process, as the changes allow for recovery from transient errors without immediate task failure. This update improves task reliability and visibility in both the controller logic and terminal user interface, ensuring seamless navigation and analysis of retry attempts.

### :zap: Improved Module Loading

Enhance your workflow with the updated Flyte SDK's module loading feature. Now, the SDK respects `.gitignore` and standard ignore rules, excluding unnecessary directories like `.venv` and `__pycache__`. This change streamlines Python module management, aligning with typical development practices, and enhances efficiency by ignoring irrelevant files.

### :zap: Dynamic Batching for Improved GPU Utilization

You can now efficiently batch GPU workloads using the new `DynamicBatcher` and `TokenBatcher` classes, maximizing resource utilization. These features allow concurrent tasks to share a single processing resource, improving efficiency and throughput—ideal for use cases like large-scale machine learning inference. As part of this update, an example demonstrates how to use `TokenBatcher` for inference tasks with reusable containers.

### :sparkles: Run Cache Disabling 

The latest update introduces a new feature allowing users to disable run-level task result caching. This enhancement ensures that when caching is disabled for a specific run, no cache hits are reported and cache operations are bypassed. This behavior is now reflected in the Terminal UI (TUI), offering a clear indication that caching is disabled, both for task execution and within the TUI display. This addition empowers users to have more granular control over caching mechanisms during local and terminal-based executions.

### :computer: Vim Key Navigation for TUI

You can now navigate the terminal user interface using Vim keys `j` and `k` for cursor movement in the `FlyteTUIApp` and `ExploreTUIApp`. This feature enhances navigation by allowing users familiar with Vim to move up and down the `ActionTreeWidget` and `RunsTable` efficiently without relying solely on arrow keys. This improvement is ideal for developers who prefer keyboard navigation and increases accessibility and convenience in terminal-based operations.

### :sparkles: Clickable Image Build URLs

You can now access clickable image URIs directly in TaskMetadata within the Union frontend. This enhancement links to the specific Flyte run that built a task's image, providing a seamless way to trace image builds to their execution context. This new capability simplifies navigation and monitoring of image builds within your deployment pipeline.

### :sparkles: Enhanced Run Filters

You can now filter runs and actions in Flyte by project, domain, and creation/update time ranges. This enhancement allows you to query runs across different projects without needing to reconfigure the context, making it easier to manage and analyze runs in complex environments. The new `TimeFilter` class supports filtering by `created_at` and `updated_at` timestamps, providing a more precise way to retrieve relevant data. The filters are available through both the Flyte SDK and the CLI, allowing seamless integration into your workflows.

```python
from flyte.remote import TimeFilter

# Example usage to fetch runs created after a specific date
runs = Run.listall(
    project="my-project",
    created_at=TimeFilter(after="2026-03-01")
)
```

This update improves the flexibility and usability of the Flyte SDK by enabling finely-grained control over data queries.

### :wrench: Simplified Dependency Management

You can now build Flyte images more efficiently by copying only the `pyproject.toml` files of each editable dependency in `UVProject`'s `dependencies_only` mode, rather than the entire directory. This change reduces build context size and speeds up the image build process. Ensure to verify the `source_dir` is corrected during prototyping to avoid compilation errors.

### :robot: MLE Agent Enhancements

The Flyte SDK now includes two new agents: the MLE Orchestrator Agent and the MLE Tool Builder Agent. These agents leverage large language models to automatically generate orchestration and processing code, allowing you to create, execute, and iteratively optimize machine learning models in an isolated sandbox environment. You can now configure tasks with specific computing resources, and they intelligently adjust based on workload requirements. This enhancement simplifies the development of complex ML pipelines by automating the orchestration process.

### :sparkles: Improved Task Command Initialization

The Flyte CLI now ensures that configuration is initialized when listing or resolving task commands using `TaskPerFileGroup`. This improvement helps prevent failures during command resolution by ensuring that any config-dependent operations required by task commands are handled properly. You can now confidently run tasks that rely on specific configurations, such as those requiring file inputs.

```python
import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="example_env")

@env.task
async def test_file(project: str, input_file: File) -> str:
    return f"Got input {project=}, {input_file=}"
```

This enhancement can significantly improve workflow reliability for projects with configurations dependent on files or other external inputs.

### :zap: New Example Applications & Bug Fixes

Several new example applications have been added to the Flyte SDK, showcasing capabilities for asynchronous workflows, distributed training, caching/retries, agent-based orchestration, and external API integration. These examples are valuable resources for learning and illustrating Flyte's powerful features:

- Distributed training using async tasks
- MNIST model handling with PyTorch
- Agent workflows with LangGraph & Gemini API

Additionally, a bug fix was implemented for proper scaling metric serialization, ensuring more accurate performance monitoring. These updates enhance the SDK's robustness and usability for developers.

### :arrow_up: Vim Key Navigation

You can now navigate the status dropdown menu in the Flyte TUI using vim keys `j` and `k`. This update allows for smoother and quicker navigation for users familiar with vim keybindings, enhancing the overall user experience when exploring past runs in Flyte's terminal interface.

### :gear: Phase Transitions Tracking

You can now view detailed phase transition information for actions in your Flyte workflows. This enhancement breaks down the time spent in each phase (e.g., QUEUED, INITIALIZING, RUNNING) for a specific run or action attempt. It provides granular insights into execution by showing phase durations, helping you identify potential bottlenecks and optimize task execution times. The `get_phase_transitions` method and properties like `queued_time`, `running_time`, etc., can be utilized to access these insights programmatically.

```python
action = Action.get(run_name="my-run", name="my-action")
details = action.details()
transitions = details.get_phase_transitions()
for t in transitions:
    print(f"{t.phase}: {t.duration.total_seconds()}s")
```

This functionality is particularly beneficial for understanding and improving the performance of complex workflows.

### :wrench: Multiple Source Files Support

The `with_source_file` function now supports passing a list of file paths, allowing you to include multiple files in a single image layer sequence. This enhancement prevents silent overwrites by raising an error if duplicate filenames are destined for the same location. You can conveniently layer various source files in one call without repetitive invocations.

```python
from flyte._image import Image
from pathlib import Path

# Example usage with two different files
img = Image.from_debian_base(name="my-image").with_source_file([Path("a.py"), Path("b.py")])
```

This change enhances flexibility when composing container images, providing an improved workflow for setting up complex dependencies or configurations.

### :package: Simplified Code Bundling

Flyte now offers a streamlined way to package source code into Docker images using the `with_code_bundle()` method. When the `copy_style` is set to `"none"` in `with_runcontext()` or during `flyte deploy`, your source code is automatically baked into the image, freeing you from manual copying steps. This feature activates only when code is not pre-bundled, ensuring efficient packaging without redundant steps. Customize the inclusion of specific Python modules or entire directories with the `"loaded_modules"` or `"all"` options, respectively.

### :wrench: Improved Error Messaging for Deployment

Now, when using a `src/` layout, you will receive a clearer error message hinting at the `--root-dir` option if you encounter the "Duplicate environment name" error during deployment. This update helps users correctly configure their deployment directories to avoid dual-import issues, making the deployment process smoother and less error-prone.

```python
# New deployment configuration example
flyte deploy --dry-run --recursive --root-dir src src/my_module
```

This is particularly useful for users who structure their projects with a `src/` directory, ensuring more intuitive guidance when deploying.

### :wrench: Improved Debugging for Reusable Tasks

You can now rest easy knowing that reusable tasks have enhanced debugging capabilities. Previously, debugging was enabled by default, which could lead to unintended issues when dealing with reusable tasks. With this update, reusable tasks automatically disable debugging, ensuring smoother execution without unnecessary overhead. This enhancement helps maintain the efficiency and reliability of your workflows.

### :sparkles: JSONL Plugin Support

You can now use JSONL file and directory types in Flyte workflows with the new JSONL plugin. The plugin supports asynchronous and synchronous read and write operations with optional `zstd` compression for efficient storage. This enhancement leverages fast serialization with `orjson`, making it suitable for handling large datasets across cloud environments. The JSONL plugin facilitates seamless data processing and batch operations in Flyte orchestrations.

```python
from flyteplugins.jsonl import JsonlFile, JsonlDir

# Example usage of JsonlFile
@env.task
async def process_file(f: JsonlFile):
    async for record in f.iter_records():
        print(record)

# Example usage of JsonlDir for sharded directories
@env.task
async def process_dir(d: JsonlDir):
    async for record in d.iter_records():
        print(record)
```

Enhance your data handling capabilities with automatic sharding, compression, and batch processing support.


## November 2025

### :fast_forward: Grouped Runs
We redesigned the Runs page to better support large numbers of runs. Historically, large projects produced so many runs that flat listings became difficult to navigate. The new design groups Runs by their root task - leveraging the fact that while there may be millions of runs, there are typically only dozens or hundreds of deployed tasks. This grouped view, combined with enhanced filtering (by status, owner, duration, and more coming soon), makes it dramatically faster and easier to locate the exact runs users are looking for, even in the largest deployments.

![Grouped Runs View](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/release-notes/2025-11_grouped_runs.gif)

### :globe_with_meridians: Apps (beta)

You can now deploy apps in Union 2.0. Apps let you host ML models, Streamlit dashboards, FastAPI services, and other interactive applications alongside your workflows. Simply define your app, deploy it, and Union will handle the infrastructure, routing, and lifecycle management. You can even call apps from your tasks to build end-to-end workflows that combine batch processing with real-time serving.

To create an app, import `flyte` and use either `FastAPIAppEnvironment` for FastAPI applications or the generic `AppEnvironment` for other frameworks. Here's a simple FastAPI example:

```python
from fastapi import FastAPI
import flyte
from flyte.app.extras import FastAPIAppEnvironment

app = FastAPI()
env = FastAPIAppEnvironment(
    name="my-api",
    app=app,
    image=flyte.Image.from_debian_base(python_version=(3, 12))
        .with_pip_packages("fastapi", "uvicorn"),
    resources=flyte.Resources(cpu=1, memory="512Mi"),
    requires_auth=False,
)

@env.app.get("/greeting/{name}")
async def greeting(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    flyte.init_from_config()
    flyte.deploy(env) # Deploy and serve your app
```

For Streamlit apps, use the generic `AppEnvironment` with a command:

```python
app_env = flyte.app.AppEnvironment(
    name="streamlit-hello-v2",
    image=flyte.Image.from_debian_base(python_version=(3, 12)).with_pip_packages("streamlit==1.41.1"),
    command="streamlit hello --server.port 8080",
    resources=flyte.Resources(cpu="1", memory="1Gi"),
)
```

You can call apps from tasks by using `depends_on` and making HTTP requests to the app's endpoint. Please refer to the example in the [SDK repo](https://github.com/flyteorg/flyte-sdk/blob/main/examples/apps/call_apps_in_tasks/app.py). Similarly, you can call apps from other apps (see this [example](https://github.com/flyteorg/flyte-sdk/blob/main/examples/apps/app_calling_app/app.py)).

### :label: Custom context

You can now pass configuration and metadata implicitly through your entire task execution hierarchy using custom context. This is ideal for cross-cutting concerns like tracing IDs, experiment metadata, environment information, or logging correlation keys—data that needs to be available everywhere but isn't logically part of your task's computation.

Custom context is a string key-value map that automatically flows from parent to child tasks without adding parameters to every function signature. Set it once at the run level with `with_runcontext()`, or override values within tasks using the `flyte.custom_context()` context manager:

```python
import flyte

env = flyte.TaskEnvironment("custom-context-example")

@env.task
async def leaf_task() -> str:
    # Reads run-level context
    print("leaf sees:", flyte.ctx().custom_context)
    return flyte.ctx().custom_context.get("trace_id")

@env.task
async def root() -> str:
    return await leaf_task()

if __name__ == "__main__":
    flyte.init_from_config()
    # Base context for the entire run
    run = flyte.with_runcontext(custom_context={"trace_id": "root-abc", "experiment": "v1"}).run(root)
    print(run.url)
```

### :lock: Secrets UI

Now you can view and create secrets directly from the UI. Secrets are stored securely in your configured secrets manager and injected into your task environments at runtime.

![Secrets Creation Flow](https://raw.githubusercontent.com/unionai/unionai-docs-static/main/images/release-notes/2025-11_secrets_creation.gif)

### Image builds now run in the same project-domain
The image build task is now executed within the same project and domain as the user task, rather than in system-production. This change improves isolation and is a key step toward supporting multi-dataplane clusters.

### Support for secret mounts in Poetry and UV projects
We added support for mounting secrets into both Poetry and UV-based projects. This enables secure access to private dependencies or credentials during image build.

```python
import pathlib

import flyte

env = flyte.TaskEnvironment(
    name="uv_project_lib",
    resources=flyte.Resources(memory="1000Mi"),
    image=(
        flyte.Image.from_debian_base().with_uv_project(
            pyproject_file=pathlib.Path(__file__).parent / "pyproject.toml",
            pre=True,
            secret_mounts="my_secret",
        )
    ),
)
```


## October 2025

### :infinity: Larger fanouts
You can now run up to 50,000 actions within a run and up to 1,000 actions concurrently.
To enable observability across so many actions, we added group and sub-actions UI views, which show summary statistics about the actions which were spawned within a group or action.
You can use these summary views (as well as the action status filter) to spot check long-running or failed actions.

![50k Fanout Visualization](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_50k_fanout.gif)

### :computer: Remote debugging for Ray head nodes
Rather than locally reproducing errors, sometimes you just want to zoom into the remote execution and see what's happening.
We directly enable this with the debug button.
When you click "Debug action" from an action in a run, we spin up that action's environment, code, and input data, and attach a live VS Code debugger.
Previously, this was only possible with vanilla Python tasks.
Now, you can debug multi-node distributed computations on Ray directly.

![Debugging Ray Head Node](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_ray_head_debug.gif)

### :zap: Triggers and audit history
[Triggers](../user-guide/task-configuration/triggers) let you templatize and set schedules for your workflows, similar to Launch Plans in Flyte 1.0.

```python
@env.task(triggers=flyte.Trigger.hourly())  # Every hour
def example_task(trigger_time: datetime, x: int = 1) -> str:
    return f"Task executed at {trigger_time.isoformat()} with x={x}"
```

Once you deploy, it's possible to see all the triggers which are associated with a task:

![Triggers for a Task](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_triggers_for_task.png)

We also maintain an audit history of every deploy, activation, and deactivation event, so you can get a sense of who's touched an automation.

![Triggers Activity Log](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_trigger_activity_log.gif)

### :arrow_up: Deployed tasks and input passing

You can see the runs, task spec, and triggers associated with any deployed task, and launch it from the UI. We've converted the launch forms to a convenient JSON Schema syntax, so you can easily copy-paste the inputs from a previous run into a new run for any task.

![Deployed Tasks and Input Passing](https://raw.githubusercontent.com/unionai/unionai-docs-static/refs/heads/main/images/release-notes/2025-10_tasks_and_input_passing.gif)

{{< /markdown >}}
{{< /variant >}}