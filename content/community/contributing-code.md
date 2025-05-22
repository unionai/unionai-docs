---
title: Contributing code
weight: 2
variants: +flyte -serverless -byoc -selfmanaged
---

# Contributing code

Thank you for taking the time to contribute to Flyte!

Here are some guidelines for you to follow, which will make your first and follow-up contributions easier.

TL;DR: Find the repo-specific contribution guidelines in the [Component Reference](#component-reference) section.

## 💻 Becoming a contributor

An issue tagged with [`good first issue`](https://github.com/flyteorg/flyte/labels/good%20first%20issue) is the best place to start for first-time contributors.

**Fork and clone the concerned repository. Create a new branch on your fork and make the required changes. Create a pull request once your work is ready for review.**

> [!NOTE]
> To open a pull request, refer to [GitHub's guide](https://guides.github.com/activities/forking/) for detailed instructions.

Example PR for your reference: [GitHub PR](https://github.com/flyteorg/flytepropeller/pull/242).
Several checks are introduced to help maintain the robustness of the project:

1. To get through DCO, sign off on every commit ([Reference](https://github.com/src-d/guide/blob/master/developer-community/fix-DCO.md)).
2. To improve code coverage, write unit tests to test your code.
3. Make sure all the tests pass. If you face any issues, please let us know in the [`#contribute`](https://flyte-org.slack.com/archives/C04NJPLRWUX) channel.
4. Format your Go code with `golangci-lint` followed by `goimports` (use `make lint` and `make goimports`).
5. Format your Python code with `black` and `isort` (use `make fmt`).
6. If make targets are not available, you can manually format the code.

> [!NOTE]
> Refer to [Effective Go](https://golang.org/doc/effective_go), [Black](https://github.com/psf/black), and [Isort](https://github.com/PyCQA/isort) for full coding standards.

As you become more involved with the project, you may be able to be added as a committer to the repos you're working on. Check out the [Flyte Contributor Ladder](https://github.com/flyteorg/community/blob/main/GOVERNANCE.md#community-roles-and-path-to-maintainership) to learn more.

### Before submitting your PR

We strongly encourage you to add one of these labels to your Pull Request:

- **added**: For new features.
- **changed**: For changes in existing functionality.
- **deprecated**: For soon-to-be-removed features.
- **removed**: For features being removed.
- **fixed**: For any bug fixes.
- **security**: In case of vulnerabilities.

This is helpful to build human-readable release notes. [Learn more](https://keepachangelog.com/en/1.1.0/).

> [!NOTE]
> Learn how to apply a label to a PR in the [GitHub docs](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels#applying-a-label).

## 🐞 File an issue

We use [GitHub Issues](https://github.com/flyteorg/flyte/issues) for issue tracking. The following issue types are available for filing an issue:

- [Plugin Request](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=untriaged%2Cplugins&template=backend-plugin-request.md&title=%5BPlugin%5D)
- [Bug Report](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=bug%2C+untriaged&template=bug_report.md&title=%5BBUG%5D+)
- [Documentation Bug/Update Request](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=documentation%2C+untriaged&template=docs_issue.md&title=%5BDocs%5D)
- [Core Feature Request](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=enhancement%2C+untriaged&template=feature_request.md&title=%5BCore+Feature%5D)
- [Flytectl Feature Request](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=enhancement%2C+untriaged%2C+flytectl&template=flytectl_issue.md&title=%5BFlytectl+Feature%5D)
- [Housekeeping](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=housekeeping&template=housekeeping_template.md&title=%5BHousekeeping%5D+)
- [UI Feature Request](https://github.com/flyteorg/flyte/issues/new?assignees=&labels=enhancement%2C+untriaged%2C+ui&template=ui_feature_request.md&title=%5BUI+Feature%5D)

If none of the above fit your requirements, file a [blank](https://github.com/flyteorg/flyte/issues/new) issue.
Also, add relevant labels to your issue. For example, if you are filing a Flytekit plugin request, add the `flytekit` label.

For feedback at any point in the contribution process, feel free to reach out to us on [Slack](https://flyte-org.slack.com/archives/C04NJPLRWUX).

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
