# Development cycle

This section covers developing production-ready workflows for Union.

```{list-table}
:header-rows: 0
:widths: 20 30

* - {doc}`Project structure <project-structure>`
  - Best practices in organizing a Union workflow project repository.
* - {doc}`Projects and domains <projects-and-domains>`
  - Understanding projects and domains in Union.
* - {doc}`Building workflows <building-workflows>`
  - Best practices in strucuring your workflows.
* - {doc}`Setting up a project <setting-up-a-project>`
  - Create a project on Union and initialize a workflow directory on your local machine.
* - {doc}`Local dependencies <local-dependencies>`
  - Install the required dependencies locally.
* - {doc}`Remote dependencies with ImageSpec <remote-dependencies-with-image-spec>`
  - Use `ImageSpec` to specify the dependencies needed in the containers that will run your tasks on Union.
* - {doc}`Running your code <running-your-code>`
  - Use different deploy and run commands for different steps in the development cycle.
* - {doc}`Overriding parameters <overriding-parameters>`
  - Use `with_overrides` to change parameters at execution time.
* - {doc}`Details of union run <details-of-union-run>`
  - Programmatically perform Union operations in Python.
* - {doc}`Debugging with interactive tasks <debugging-with-interactive-tasks>`
  - Inspect and debug live task code directly in the Union console.
* - {doc}`Managing secrets <managing-secrets>`
  - Create and manage secrets to connect to third-party services.
* - {doc}`Managing apps <managing-apps>`
  - Create applications to allow external systems to run compute on Union.
{@@ if serverless @@}
* - {doc}`Accessing AWS S3 buckets <accessing-aws-s3>`
  - Access data in AWS S3 Buckets from Union.
{@@ endif @@}
* - {doc}`Task resource validation <task-resource-validation>`
  - How Union handles workflows with unsatisfiable resource requests.
{@@ if byoc @@}
* - {doc}`Running in a local cluster <running-in-a-local-cluster>`
  - Run your workflows in a local Kubernetes cluster on your machine.
* - {doc}`CI/CD deployment <ci-cd-deployment>`
  - Automate workflow registration and execution.
{@@ endif @@}
* - {doc}`UnionRemote <union-remote>`
  - Programmatically perform Union operations in Python.
```
