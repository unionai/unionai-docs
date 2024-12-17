# Best practices

This section gives guidance on the best practices for developing on Union.

Over the years, developers building on Union (and its OSS predecessor, Flyte) have evolved a set of principles and practices
around many aspects of programming on the platform.

This section attempts to capture the most relevant and useful of these and provide guidance on how to apply them to your projects.

By adopting these guidelines you will be able to unlock the true power the Union platform.




{@#
NOTES:

Focus this section on a full example of an actual project, preferably a maximally complex one (or at least one that exhibits all relevant features that we want to discuss)
We should add a template (one of a few) to `union init` that corresponds to this "full project".
The essence of this is that a project has the following structure:

```
<project-root>
  ├── .github/workflows/
  ├── workflows/
  │   ├── __init__.py
  │   └── example.py
  ├── tasks/
  ├── launch-plans/
  ├── config/
  ├── data/
  ├── local/
  ├── tests/
  ├── pyproject.toml
  ├── uv.lock
  ├── README.md
  └── LICENSE
```
or something along those lines

The GitHub action should:
* Register (and promote if needed) on merge to domain branch.
* Execute on merge of input YAML.
* Inject git SHA as entity version.

Consider adding a GitHub bot too.
#@}
