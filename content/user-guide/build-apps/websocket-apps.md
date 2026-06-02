---
title: WebSocket apps
weight: 5
variants: +flyte +union
---

# WebSocket apps

WebSockets enable bidirectional, real-time communication between clients and servers. Flyte apps can serve WebSocket endpoints for real-time applications like chat, live updates, or streaming data.

## Example: Basic WebSocket app

Here's a simple FastAPI app with WebSocket support:

{{< code file="/unionai-examples/v2/user-guide/build-apps/websocket/basic_websocket.py" lang=python >}}

## WebSocket patterns

**Echo server**

{{< code file="/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=echo-server lang=python >}}

**Broadcast server**

{{< code file="/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=broadcast-server lang=python >}}

**Real-time data streaming**

{{< code file="/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=streaming-server lang=python >}}

**Chat application**

{{< code file="/unionai-examples/v2/user-guide/build-apps/websocket/websocket_patterns.py" fragment=chat-room lang=python >}}

## Using WebSockets with Flyte tasks

You can trigger Flyte tasks from WebSocket messages:

{{< code file="/unionai-examples/v2/user-guide/build-apps/websocket/task_runner_websocket.py" fragment=task-runner-websocket lang=python >}}

## WebSocket client example

Connect from Python:

```python
import asyncio
import websockets
import json

async def client():
    uri = "ws://your-app-url/ws"
    async with websockets.connect(uri) as websocket:
        # Send message
        await websocket.send("Hello, Server!")
        
        # Receive message
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.run(client())
```

## Best practices

1. **Connection management**: Track active connections and handle disconnections gracefully.
2. **Heartbeats**: Implement ping/pong for connection health monitoring.
3. **Rate limiting**: Consider rate limiting for production deployments.
4. **Error handling**: Handle WebSocket errors and connection drops.
5. **Authentication**: Implement authentication for secure WebSocket connections.
