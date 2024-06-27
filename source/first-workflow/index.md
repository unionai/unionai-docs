# First workflow

This section walks through building your first Union workflow, exploring the major features of the platform along the way.

## Prerequisites

{@@ if serverless @@}

If you have not already done so, follow the [Quick start guide](../quick-start) to sign into the Union UI,
set up your local Python environment, and install the `unionai` command line tool.

{@@ elif byoc @@}

If you have not already done so, follow the [Quick start guide](../quick-start) to sign into the Union UI,
set up your local Python environment, and install the `unionai[byoc]` command line tool.

{@@ endif @@}


## Your project on Union

{@@ if serverless @@}

Union Serverless provides a default project (called **default**) where all your workflows will be registered unless you specify otherwise. We will use this default project for the rest of this guide.

{@@ elif byoc @@}

Each Union BYOC organization has a default project (called **flytesnacks**) where all your workflows will be registered unless you specify otherwise. We will use this default project for the rest of this guide.

{@@ endif @@}

To create additional projects, see [Setting up a project](../moving-onward/setting-up-a-project).

## Our example workflow

In this section, we will use a workflow from Union's [`unionai/unionai-examples`](https://github.com/unionai/unionai-examples) GitHub repository that illustrates training a simple model using `flytekit`, `scikit-learn`, and `pandas`.

The model training workflow has three steps:
- Getting the `penguins` dataset from [openml.org](https://www.openml.org/search?type=data&sort=runs&id=42585&status=active)
- Training a `HistGradientBoostingClassifier` model using `scikit-learn`.
- Evaluating the model by creating a confusion matrix, displayed as a Flyte `Deck`.

## Next step

The next step is [Setting up your local environment](setting-up-your-local-environment).
