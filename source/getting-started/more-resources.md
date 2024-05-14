# Learning more about Union and Flyte

Since Union shares its programming model (and specifically, the Flytekit SDK) with the open source project Flyte, you can learn more about programming in Union by reading the Flyte documentation:
* [Flyte project homepage](https://flyte.org/)
* [Flyte docs](https://docs.flyte.org/en/latest/)

Specific sections that you might find helpful:

* [Flyte Fundamentals](https://docs.flyte.org/en/latest/flyte_fundamentals/index.html)
* [Core Use Cases](https://docs.flyte.org/en/latest/core_use_cases/index.html)
* [User Guide](https://docs.flyte.org/en/latest/user_guide/index.html)
* [Tutorials](https://docs.flyte.org/en/latest/flytesnacks/tutorials.html)
* [Integrations](https://docs.flyte.org/en/latest/flytesnacks/integrations.html)
* [Concepts](https://docs.flyte.org/en/latest/concepts/basics.html)
* [Flytekit](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)

:::{admonition} Differences between Flyte and Union
As you read the Flyte docs, keep in mind a few of the differences between Flyte and Union:

* The command-line tool for Flyte OSS is `flytectl`.
The one for Union is `uctl`.
They are identical except that `uctl` has a few extra Union-specific features.
* The default local configuration location for Flyte is `~/.flyte/` while for Union it is `~/.uctl/`.
:::