---
title: API playground
weight: 13
variants: +flyte -serverless -byoc -selfmanaged
---

# Flyte API Playground: Swagger

Flyte services expose gRPC services for efficient/low latency communication across all services as well as for external clients (FlyteCTL, FlyteConsole, Flytekit Remote, etc.).

The services are defined [here](https://github.com/flyteorg/flyteidl/tree/master/protos/flyteidl/service).
FlyteIDL also houses open API schema definitions for the exposed services:

- [Admin](https://github.com/flyteorg/flyteidl/blob/master/gen/pb-go/flyteidl/service/admin.swagger.json)
- [Auth](https://github.com/flyteorg/flyteidl/blob/master/gen/pb-go/flyteidl/service/auth.swagger.json)
- [Identity](https://github.com/flyteorg/flyteidl/blob/master/gen/pb-go/flyteidl/service/identity.swagger.json)

To view the UI, run the following command:

```bash
flytectl demo start
```
Once sandbox setup is complete, a ready-to-explore message is shown:

```bash
   👨‍💻 Flyte is ready! Flyte UI is available at http://localhost:30081/console 🚀 🚀 🎉
```

Visit ``http://localhost:30080/api/v1/openapi`` to view the swagger documentation of the payload fields.
