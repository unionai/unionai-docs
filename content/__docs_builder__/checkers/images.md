---
title: Image Checker
variants: -flyte -serverless -byoc -selfmanaged
---

# Image Checker

| Test | Expectation | Image |
| --- | --- | --- |
| Image exists | OK | ![Good Image](../../_static/images/deployment/architecture.svg "medium") |
| Image exists | FAIL | ![Bad Image](/does/not/exist) |
| Unregistered Remote Image | FAIL | ![Bad External Image](https://www.union.ai/docs/flyte/images/icon-logo-flyte.png "icon") |
| Registered Remote Image | OK | ![Bad External Image](https://www.union.ai/docs/byoc/images/icon-logo.svg "icon") |