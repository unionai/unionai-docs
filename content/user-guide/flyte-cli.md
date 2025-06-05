---
title: Flyte CLI
weight: 7
variants: +flyte +serverless +byoc +selfmanaged
---

# Flyte CLI

So far, we have executed our example scripts directly in Python. We enabled this by adding a main guard to each script that called the appropriate Flyte command to deploy the code.

Deploying and executing code programmatically as we have been doing is a powerful feature, but there are cases where you want to deploy and run workflows from the command line.
The Flyte CLI provides a convenient way to do this.

## API CLI equivalence

The Flyte SDK API provides all the functionality of the Flyte CLI.
Every command in the CLI has a corresponding function in the SDK.

## The essential commands

[TODO: Add content and example]