# First project

This section walks through building your first Union project, exploring the major features of the platform along the way.

## Prerequisites

If you have not already done so, follow the [Quickstart guide](quickstart) to sign into the Union web console,
set up your local Python environment, and install the `unionai` command line tool.

## Your project on Union

{@@ if serverless @@}

Each Union Serverless (which is tied to your GitHub account) provides a default project (called **default**) where all your workflows will be registered unless you specify otherwise.
We will use this default project for the rest of this guide.
For information on creating additional projects, see the [Creating a Union project](creating-a-union-project).

{@@ elif byoc @@}

Each Union BYOC organization comes pre-configured with a default project (called **flytesnacks**) where all your workflows will be registered unless you specify otherwise.
We will use this default project for the rest of this guide.
For information on creating additional projects, see the [Creating projects](creating-projects).

{@@ elif byoc @@}

## Your local project

When developing workflows on Union you can organize (or not) your code as you wish.
However, as your workflows grow in complexity, it is a good idea to structure them into projects on your local machine
and manage those projects with a version control system.

## Our example project

In this section we will use a project from Union's examples GitHub repository [`unionai/examples`](https://github.com/unionai/examples).

This example illustrates how to train a simple model on Union using `flytekit`, `scikit-learn`, and `pandas`.

The model training workflow that we're going to run is composed of three steps.
- Getting the `penguins` dataset from [openml.org](https://www.openml.org/search?type=data&sort=runs&id=42585&status=active)
- Training a `HistGradientBoostingClassifier` model using `scikit-learn`.
- Evaluating the model by creating a confusion matrix, displayed as a Flyte `Deck`.

## Next step

The next step is [Setting up the local environment](setting-up-the-local-environment).

