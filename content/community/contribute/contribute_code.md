---
title: Contributing code
weight: 1
variants: +flyte -serverless -byoc -byok
---

# Contributing code

## 🧱 Component Reference

To understand how the below components interact with each other, refer to [Understand the lifecycle of a workflow](#workflow-lifecycle).

> [!NOTE]
> With the exception of `flytekit`, the below components are maintained in the [flyte monorepo](https://github.com/flyteorg/flyte).

![Dependency graph between various flyteorg repos](https://raw.githubusercontent.com/flyteorg/static-resources/main/flyte/contribution_guide/dependency_graph.png)

### `flyte`

| **Repo** | [flyte](https://github.com/flyteorg/flyte) |
|----------|-------------------------------------------|
| **Purpose** | Deployment, Documentation, and Issues |
| **Languages** | RST |

### `flyteidl`

| **Repo** | [flyteidl](https://github.com/flyteorg/flyteidl) |
|----------|-------------------------------------------------|
| **Purpose** | Flyte workflow specification is in [protocol buffers](https://developers.google.com/protocol-buffers) which forms the core of Flyte |
| **Language** | Protobuf |
| **Guidelines** | Refer to the [README](https://github.com/flyteorg/flyteidl#generate-code-from-protobuf) |

### `flytepropeller`

| **Repo** | [flytepropeller](https://github.com/flyteorg/flytepropeller) \| [Code Reference](https://pkg.go.dev/mod/github.com/flyteorg/flytepropeller) |
|----------|------------------------------------------------------------------------------------------------|
| **Purpose** | Kubernetes-native operator |
| **Language** | Go |
| **Guidelines** |                                                                                          |
|              | - Check for Makefile in the root repo                                                      |
|              | - Run the following commands:                                                              |
|              |   - `make generate`                                                                        |
|              |   - `make test_unit`                                                                       |
|              |   - `make lint`                                                                            |
|              | - To compile, run `make compile`                                                           |

### `flyteadmin`

| **Repo** | [flyteadmin](https://github.com/flyteorg/flyteadmin) \| [Code Reference](https://pkg.go.dev/mod/github.com/flyteorg/flyteadmin) |
|----------|------------------------------------------------------------------------------------------------|
| **Purpose** | Control Plane |
| **Language** | Go |
| **Guidelines** |                                                                                          |
|              | - Check for Makefile in the root repo                                                      |
|              | - If the service code has to be tested, run it locally:                                    |
|              |   - `make compile`                                                                         |
|              |   - `make server`                                                                          |
|              | - To seed data locally:                                                                    |
|              |   - `make compile`                                                                         |
|              |   - `make seed_projects`                                                                   |
|              |   - `make migrate`                                                                         |
|              | - To run integration tests locally:                                                        |
|              |   - `make integration`                                                                     |
|              |   - (or to run in containerized dockernetes): `make k8s_integration`                       |

### `flytekit`

| **Repo** | [flytekit](https://github.com/flyteorg/flytekit) |
|----------|-------------------------------------------------|
| **Purpose** | Python SDK & Tools |
| **Language** | Python |
| **Guidelines** | Refer to the [Flytekit Contribution Guide](https://docs.flyte.org/en/latest/api/flytekit/contributing.html) |

### `flyteconsole`

| **Repo** | [flyteconsole](https://github.com/flyteorg/flyteconsole) |
|----------|---------------------------------------------------------|
| **Purpose** | Admin Console |
| **Language** | Typescript |
| **Guidelines** | Refer to the [README](https://github.com/flyteorg/flyteconsole/blob/master/README.md) |

### `datacatalog`

| **Repo** | [datacatalog](https://github.com/flyteorg/datacatalog) \| [Code Reference](https://pkg.go.dev/mod/github.com/flyteorg/datacatalog) |
|----------|------------------------------------------------------------------------------------------------|
| **Purpose** | Manage Input & Output Artifacts |
| **Language** | Go |

### `flyteplugins`

| **Repo** | [flyteplugins](https://github.com/flyteorg/flyteplugins) \| [Code Reference](https://pkg.go.dev/mod/github.com/flyteorg/flyteplugins) |
|----------|------------------------------------------------------------------------------------------------|
| **Purpose** | Flyte Plugins |
| **Language** | Go |
| **Guidelines** |                                                                                          |
|              | - Check for Makefile in the root repo                                                      |
|              | - Run the following commands:                                                              |
|              |   - `make generate`                                                                        |
|              |   - `make test_unit`                                                                       |
|              |   - `make lint`                                                                            |

### `flytestdlib`

| **Repo** | [flytestdlib](https://github.com/flyteorg/flytestdlib) |
|----------|-------------------------------------------------------|
| **Purpose** | Standard Library for Shared Components |
| **Language** | Go |

### `flytectl`

| **Repo** | [flytectl](https://github.com/flyteorg/flytectl) |
|----------|-------------------------------------------------|
| **Purpose** | A standalone Flyte CLI |
| **Language** | Go |
| **Guidelines** | Refer to the [FlyteCTL Contribution Guide](https://docs.flyte.org/en/latest/flytectl/contribute.html) |
