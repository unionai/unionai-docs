---
title: Classes
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# Classes

| Class | Description |
|-|-|
| [`union.Environment`](../packages/union#unionenvironment) |Environment class to define a new environment for a set of tasks. |
| [`union.Image`](../packages/union#unionimage) |This is an abstract representation of Container Images, which can be used to create layered images programmatically. |
| [`union.Resources`](../packages/union#unionresources) |Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`union.ReusePolicy`](../packages/union#unionreusepolicy) |ReusePolicy can be used to configure a task to reuse the environment. |
| [`union.Secret`](../packages/union#unionsecret) |Secrets are used to inject sensitive information into tasks. |
| [`union.errors.CustomError`](../packages/union.errors#unionerrorscustomerror) |This error is raised when the user raises a custom error. |
| [`union.errors.InitializationError`](../packages/union.errors#unionerrorsinitializationerror) |This error is raised when the Union system is tried to access without being initialized. |
| [`union.errors.OOMError`](../packages/union.errors#unionerrorsoomerror) |This error is raised when the underlying task execution fails because of an out-of-memory error. |
| [`union.errors.RuntimeError`](../packages/union.errors#unionerrorsruntimeerror) |Base class for all Union runtime errors. |
| [`union.errors.RuntimeSystemError`](../packages/union.errors#unionerrorsruntimesystemerror) |This error is raised when the underlying task execution fails because of a system error. |
| [`union.errors.RuntimeUnknownError`](../packages/union.errors#unionerrorsruntimeunknownerror) |This error is raised when the underlying task execution fails because of an unknown error. |
| [`union.errors.RuntimeUserError`](../packages/union.errors#unionerrorsruntimeusererror) |This error is raised when the underlying task execution fails because of an error in the user's code. |
| [`union.errors.TaskTimeoutError`](../packages/union.errors#unionerrorstasktimeouterror) |This error is raised when the underlying task execution runs for longer than the specified timeout. |
| [`union.errors.UnionRpcError`](../packages/union.errors#unionerrorsunionrpcerror) |This error is raised when communication with the Union server fails. |
| [`union.extend.TypeTransformerAPI`](../packages/union.extend#unionextendtypetransformerapi) |API type to xtend type transformers. |
| [`union.io.Dir`](../packages/union.io#unioniodir) |A generic directory class representing a directory with files of a specified format. |
| [`union.io.File`](../packages/union.io#unioniofile) |A generic file class representing a file with a specified format. |
| [`union.remote.Run`](../packages/union.remote#unionremoterun) |A class representing a run of a task. |
| [`union.remote.Task`](../packages/union.remote#unionremotetask) | |
