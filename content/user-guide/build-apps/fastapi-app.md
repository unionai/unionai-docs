---
title: FastAPI app
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# FastAPI app

FastAPI is a modern, fast web framework for building APIs. Flyte provides `FastAPIAppEnvironment` which makes it easy to deploy FastAPI applications.

## Basic FastAPI app

Here's a simple FastAPI app:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/basic_fastapi.py" lang=python >}}

Once deployed, you can:
- Access the API at the generated URL
- View interactive API docs at `/docs` (Swagger UI)
- View alternative docs at `/redoc`

## Serving a machine learning model

Here's an example of serving a scikit-learn model:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/ml_model_serving.py" fragment=ml-model lang=python >}}


## Accessing Swagger documentation

FastAPI automatically generates interactive API documentation. Once deployed:

- **Swagger UI**: Access at `{app_url}/docs`
- **ReDoc**: Access at `{app_url}/redoc`
- **OpenAPI JSON**: Access at `{app_url}/openapi.json`

The Swagger UI provides an interactive interface where you can:
- See all available endpoints
- Test API calls directly from the browser
- View request/response schemas
- See example payloads

## Example: REST API with multiple endpoints

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/rest_api.py" fragment=rest-api lang=python >}}

## Multi-file FastAPI app

Here's an example of a multi-file FastAPI app:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/app.py" lang=python >}}

The helper module:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/fastapi/multi_file/module.py" lang=python >}}

See [Multi-script apps](./multi-script-apps) for more details on building FastAPI apps with multiple files.

## Best practices

1. **Use Pydantic models**: Define request/response models for type safety and automatic validation
2. **Handle errors**: Use HTTPException for proper error responses
3. **Async operations**: Use async/await for I/O operations
4. **Environment variables**: Use environment variables for configuration
5. **Logging**: Add proper logging for debugging and monitoring
6. **Health checks**: Always include a `/health` endpoint
7. **API documentation**: FastAPI auto-generates docs, but add descriptions to your endpoints

## Advanced features

FastAPI supports many features that work with Flyte:

- **Dependencies**: Use FastAPI's dependency injection system
- **Background tasks**: Run background tasks with BackgroundTasks
- **WebSockets**: See [WebSocket-based patterns](./app-usage-patterns#websocket-based-patterns) for details
- **Authentication**: Add authentication middleware (see [secret-based authentication](./secret-based-authentication))
- **CORS**: Configure CORS for cross-origin requests
- **Rate limiting**: Add rate limiting middleware

## Troubleshooting

**App not starting:**
- Check that uvicorn can find your app module
- Verify all dependencies are installed in the image
- Check container logs for startup errors

**Import errors:**
- Ensure all imported modules are available
- Use `include` parameter if you have custom modules
- Check that file paths are correct

**API not accessible:**
- Verify `requires_auth` setting
- Check that the app is listening on the correct port (8080)
- Review network/firewall settings

