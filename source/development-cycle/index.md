# Development cycle

This section covers developing production-ready workflows for Union.

{@@ if serverless @@}

```{list-table}
:header-rows: 0
:widths: 20 30

* - {doc}`Initializing a local project <initializing-a-local-project>`
  - Use `unionai init` to initialize production-ready projects on your local machine.
* - {doc}`Creating a project on Union <creating-a-project-on-union>`
  - Create a project on Union to organize your workflows.
* - [Registering workflows](registering-workflows)
  - Register workflows from your local machine to Union.
* - {doc}`ImageSpec <image-spec>`
  - Use ImageSpec to specify custom container images that will be built and hosted by the Union Serverless image builder.
* - {doc}`Managing secrets <managing-secrets>`
  - Create and manage secrets to connect to third-party services.
* - {doc}`Managing apps <managing-apps>`
  - Create applications to allow external systems to run compute on Union.
* - {doc}`Accessing AWS S3 buckets <accessing-aws-s3>`
  - Access data in AWS S3 Buckets from Union.
* - {doc}`Task resource validation <task-resource-validation>`
  - How Union handles workflows with unsatisfiable resource requests.
* - {doc}`Debugging with interactive tasks <debugging-with-interactive-tasks>`
  - Inspect and debug live task code directly in the Union console.
* - {doc}`UnionRemote <unionremote>`
  - Programmatically perform certain operations on the Union control plane in Python.
```

{@@ elif byoc @@}

```{list-table}
:header-rows: 0
:widths: 20 30

* - {doc}`Initializing a local project <initializing-a-local-project>`
  - Use `unionai init` to initialize production-ready projects on your local machine.
* - {doc}`Creating a project on Union <creating-a-project-on-union>`
  - Create a project on Union to organize your workflows.
* - [Registering workflows](registering-workflows)
  - Register workflows from your local machine to Union.
* - {doc}`ImageSpec <image-spec>`
  - Use ImageSpec to specify custom container images that you build locally and push to a container registry.
* - {doc}`Managing secrets <managing-secrets>`
  - Create and manage secrets to connect to third-party services.
* - {doc}`Managing apps <managing-apps>`
  - Create applications to allow external systems to run compute on Union.
* - {doc}`Accessing AWS S3 buckets <accessing-aws-s3>`
  - Access data in AWS S3 Buckets from Union.
* - {doc}`Task resource validation <task-resource-validation>`
  - How Union handles workflows with unsatisfiable resource requests.
* - {doc}`Debugging with interactive tasks <debugging-with-interactive-tasks>`
  - Inspect and debug live task code directly in the Union console.
* - {doc}`Setting up CI/CD deployment <setting-up-ci-cd-deployment>`
  - Automate workflow registration and execution.
* - {doc}`UnionRemote <unionremote>`
  - Programmatically perform certain operations on the Union control plane in Python.
* - {doc}`Running in a local cluster <running-in-a-local-cluster>`
  - Test your workflows in a local Kubernetes cluster.
```

{@@ endif @@}
