---
title: Key capabilities
weight: 5
variants: +flyte +serverless +byoc +selfmanaged
---

# Key capabilities

Now that you understand the core concepts -- `TaskEnvironment`, tasks, runs, and apps -- here's an overview of what Flyte can do. Each capability is covered in detail later in the documentation.

## Environment and resources

Configure how and where your code runs.

- **Multiple environments**: Create separate configurations for different use cases (dev, prod, GPU vs CPU)
  → [Multiple environments](../task-configuration/multiple-environments)

- **Resource specification**: Request specific CPU, memory, GPU, and storage for your tasks
  → [Resources](../task-configuration/resources)

{{< variant byoc serverless selfmanaged >}}
{{< markdown >}}
- **Reusable containers**: Eliminate container startup overhead with pooled, warm containers for millisecond-level task scheduling
  → [Reusable containers](../task-configuration/reusable-containers)
{{< /markdown >}}
{{< /variant >}}

## Deployment

Get your code running remotely.

{{< variant byoc serverless selfmanaged >}}
{{< markdown >}}
- **Cloud image building**: Build container images remotely without needing local Docker
  → [Container images](../task-configuration/container-images)
{{< /markdown >}}
{{< /variant >}}

- **Code packaging**: Your local code is automatically bundled and deployed to remote execution
  → [Packaging](../task-deployment/packaging)

- **Local testing**: Test tasks locally before deploying with `flyte run --local`
  → [How task run works](../task-deployment/how-task-run-works)

## Data handling

Pass data efficiently between tasks.

- **Files and directories**: Pass large files and directories between tasks using `flyte.io.File` and `flyte.io.Dir`
  → [Files and directories](../task-programming/files-and-directories)

- **DataFrames**: Work with pandas, Polars, and other DataFrame types natively
  → [DataFrames](../task-programming/dataframes)

## Parallelism and composition

Scale out and compose workflows.

- **Fanout parallelism**: Process items in parallel using `flyte.map` or `asyncio.gather`
  → [Fanout](../task-programming/fanout)

- **Remote tasks**: Call previously deployed tasks from within your workflows
  → [Remote tasks](../task-programming/remote-tasks)

## Security and automation

Manage credentials and automate execution.

- **Secrets**: Inject API keys, passwords, and other credentials securely into tasks
  → [Secrets](../task-configuration/secrets)

- **Triggers**: Schedule tasks on a cron schedule or trigger them from external events
  → [Triggers](../task-configuration/triggers)

- **Webhooks**: Build APIs that trigger task execution from external systems
  → [App usage patterns](../build-apps/app-usage-patterns)

## Durability and reliability

Handle failures and avoid redundant work.

- **Error handling**: Catch failures and retry with different resources (e.g., more memory)
  → [Error handling](../task-programming/error-handling)

- **Retries and timeouts**: Configure automatic retries and execution time limits
  → [Retries and timeouts](../task-configuration/retries-and-timeouts)

- **Caching**: Skip redundant computation by caching task results based on inputs
  → [Caching](../task-configuration/caching)

- **Traces**: Add fine-grained checkpoints within tasks for recovery and observability
  → [Traces](../task-programming/traces)

## Apps and serving

Deploy long-running services.

- **FastAPI apps**: Deploy REST APIs and webhooks
  → [FastAPI app](../build-apps/fastapi-app)

- **LLM serving**: Serve large language models with vLLM or SGLang
  → [vLLM app](../build-apps/vllm-app), [SGLang app](../build-apps/sglang-app)

- **Autoscaling**: Scale apps up and down based on traffic, including scale-to-zero
  → [Autoscaling apps](../configure-apps/auto-scaling-apps)

- **Streamlit dashboards**: Deploy interactive data dashboards
  → [Streamlit app](../build-apps/streamlit-app)

## Notebooks

Work interactively.

- **Jupyter support**: Author and run workflows directly from Jupyter notebooks, and fetch workflow metadata (inputs, outputs, logs)
  → [Notebooks](../task-programming/notebooks)

## Next steps

Ready to put it all together? Head to [Basic project](../basic-project) to build an end-to-end ML system with training tasks and a serving app.
