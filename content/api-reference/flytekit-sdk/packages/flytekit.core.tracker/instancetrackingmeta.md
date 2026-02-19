---
title: InstanceTrackingMeta
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# InstanceTrackingMeta

**Package:** `flytekit.core.tracker`

Please see the original class :flytekit.common.mixins.registerable._InstanceTracker` also and also look
at the tests in the ``tests/flytekit/unit/core/tracker/test_tracking/`` folder to see how it's used.

Basically, this will make instances of classes that use this metaclass aware of the module (the .py file) that
caused the instance to be created. This is useful because it means that we can then (at least try to) find the
variable that the instance was assigned to.



