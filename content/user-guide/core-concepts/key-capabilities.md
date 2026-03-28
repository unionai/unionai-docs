---
title: Key capabilities
weight: 5
variants: +flyte +union
---

# Key capabilities

Now that you understand the core concepts -- `TaskEnvironment`, tasks, runs, and apps -- here's an overview of what Flyte can do. Each capability is covered in detail later in the documentation.

## Environment and resources

Configure how and where your code runs.

- **Multiple environments**: Create separate configurations for different use cases (dev, prod, GPU vs CPU)
  → [Multiple environments](../task-configuration/multiple-environments)

- **Resource specification**: Request specific CPU, memory, GPU, and storage for your tasks
  → [Resources](../task-configuration/resources)

{{< variant union >}}
{{< markdown >}}
- **Reusable containers**: Eliminate container startup overhead with pooled, warm containers for millisecond-level task scheduling
  → [Reusable containers](../task-configuration/reusable-containers)
{{< /markdown >}}
{{< /variant >}}

## Deployment

Get your code running remotely.

{{< variant union >}}
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

- **Caching**: Add `cache="auto"` to any task and Flyte stores its outputs keyed on task name and inputs. Same inputs means instant results with no recomputation. This speeds up your development loop: skip re-downloading data, avoid replaying earlier steps in agentic chains, or bypass any expensive computation while you iterate.
  → [Caching](../task-configuration/caching)

  ```python
  @env.task(cache="auto")
  async def load_data(data_dir: str = "./data") -> str:
      """Downloads once, then returns instantly on subsequent runs."""
      # ... expensive download ...
      return data_dir
  ```

- **Traces**: Use `@flyte.trace` to get visibility into the internal steps of a task without the overhead of making each step a separate task. Traced functions show up as child nodes under their parent task, each with their own timing, inputs, and outputs. This is particularly useful for AI agents where you want to see which tools were called.
  → [Traces](../task-programming/traces)

  ```python
  @flyte.trace
  async def search(query: str) -> str:
      """Shows up as a child node under the parent task."""
      return await do_search(query)

  @env.task
  async def agent(request: str) -> str:
      results = await search(request)    # Traced
      answer = await summarize(results)   # Also traced if decorated
      return answer
  ```

- **Reports**: Add `report=True` to a task and it can generate an HTML report (charts, tables, images) saved alongside the task output. Combined with caching and persisted inputs/outputs, reports act as lightweight experiment tracking—each run produces a self-contained HTML file you can compare across runs and share with your team.
  → [Reports](../task-programming/reports)

  ```python
  import flyte.report

  @env.task(report=True)
  async def evaluate(model_file: File, test_data: str) -> str:
      # ... run evaluation ...
      await flyte.report.replace.aio(
          f"<h2>Training Report</h2>"
          f"<h3>Test Results</h3>"
          f"<p>Accuracy: {accuracy:.4f}</p>"
      )
      await flyte.report.flush.aio()
      return f"Accuracy: {accuracy:.4f}"
  ```

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
