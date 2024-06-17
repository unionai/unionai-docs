# First project

This section walks through building your first Union project, exploring the major features of the platform along the way.

## Prerequisites

If you have not already done so, follow the [Quick start guide](../quick-start) to sign into the Union web console,
set up your local Python environment, and install the `unionai` command line tool.

## Your project on Union

{@@ if serverless @@}

Union Serverless provides a default project (called **default**) where all your workflows will be registered unless you specify otherwise. We will use this default project for the rest of this guide.

To create additional projects, see [Creating a Union project](../moving-onward/creating-a-union-project).

{@@ elif byoc @@}

Each Union BYOC organization has a default project (called **flytesnacks**) where all your workflows will be registered unless you specify otherwise. We will use this default project for the rest of this guide.

To create additional projects, see [Creating projects](../moving-onward/creating-a-union-project).

{@@ endif @@}

## Your local project

When developing workflows on Union, you can organize your code as you wish.
However, as your workflows grow in complexity, we recommend structuring them into projects on your local machine
and putting those under version control.

## Our example local project

In this section, we will use a project from Union's examples GitHub repository, [`unionai/unionai-examples`](https://github.com/unionai/unionai-examples), that illustrates training a simple model using `flytekit`, `scikit-learn`, and `pandas`.

The model training workflow that we're going to run has three steps:
- Getting the `penguins` dataset from [openml.org](https://www.openml.org/search?type=data&sort=runs&id=42585&status=active)
- Training a `HistGradientBoostingClassifier` model using `scikit-learn`.
- Evaluating the model by creating a confusion matrix, displayed as a Flyte `Deck`.

## Next step

The next step is [Setting up the local environment](setting-up-the-local-environment).
