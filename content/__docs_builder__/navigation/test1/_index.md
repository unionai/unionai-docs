---
title: Navigation Tests (Test 1)
variants: -flyte -serverless -byoc -byok
---

# Index

## External URL

[https://www.google.com](https://www.google.com)

## Same Folder

| Link                       | Destination                                     |
| -------------------------- | ----------------------------------------------- |
| [./page1](./page1)         | `/__docs_builder__/navigation/test1/page1/`     |
| [./page2#abc](./page2#abc) | `/__docs_builder__/navigation/test1/page2/#abc` |

## Parent Folder

| Link                                     | Destination                                  |
| ---------------------------------------- | -------------------------------------------- |
| [../test2](../test2)                     | `/__docs_builder__/navigation/test2/`        |
| [../test2/_index.md](../test2/_index.md) | `/__docs_builder__/navigation/test2/`        |
| [../test2/test2a](../test2/test2a)       | `/__docs_builder__/navigation/test2/test2a/` |
| [../test3](../test3)                     | `/__docs_builder__/navigation/test3/`        |