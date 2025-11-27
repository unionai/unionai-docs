---
title: BranchEvalMode
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# BranchEvalMode

**Package:** `flytekit.core.context_manager`

This is a 3-way class, with the None value meaning that we are not within a conditional context. The other two
values are
* Active - This means that the next ``then`` should run
* Skipped - The next ``then`` should not run


