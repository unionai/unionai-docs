---
title: WebSocket app
weight: 9
variants: +flyte +serverless +byoc +selfmanaged
---

# WebSocket app

WebSockets enable bidirectional, real-time communication between clients and servers. Flyte apps can serve WebSocket endpoints for real-time applications like chat, live updates, or streaming data.

## Basic WebSocket app

Here's a simple FastAPI app with WebSocket support:

{{< code file="/external/unionai-examples/v2/user-guide/build-apps/websocket/basic_websocket.py" lang=python >}}

## WebSocket patterns

### Echo server

Simple echo that sends messages back:

```python
@app.websocket("/echo")
async def echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        pass
```

### Broadcast server

Broadcast messages to all connected clients:

```python
@app.websocket("/broadcast")
async def broadcast(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

### Real-time data streaming

Stream data updates to clients:

```python
@app.websocket("/stream")
async def stream_data(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Generate or fetch data
            data = {"timestamp": datetime.now().isoformat(), "value": random.random()}
            await websocket.send_json(data)
            await asyncio.sleep(1)  # Send update every second
    except WebSocketDisconnect:
        pass
```

### Chat application

Multi-user chat with rooms:

```python
class ChatRoom:
    def __init__(self, name: str):
        self.name = name
        self.connections: list[WebSocket] = []
    
    async def join(self, websocket: WebSocket):
        self.connections.append(websocket)
    
    async def leave(self, websocket: WebSocket):
        self.connections.remove(websocket)
    
    async def broadcast(self, message: str, sender: WebSocket):
        for connection in self.connections:
            if connection != sender:
                await connection.send_text(message)

rooms: dict[str, ChatRoom] = {}

@app.websocket("/chat/{room_name}")
async def chat(websocket: WebSocket, room_name: str):
    await websocket.accept()
    
    if room_name not in rooms:
        rooms[room_name] = ChatRoom(room_name)
    
    room = rooms[room_name]
    await room.join(websocket)
    
    try:
        while True:
            data = await websocket.receive_text()
            await room.broadcast(data, websocket)
    except WebSocketDisconnect:
        await room.leave(websocket)
```

## Using WebSockets with Flyte tasks

You can trigger Flyte tasks from WebSocket messages:

```python
@app.websocket("/task-runner")
async def task_runner(websocket: WebSocket):
    await websocket.accept()
    
    try:
        while True:
            # Receive task request
            message = await websocket.receive_text()
            request = json.loads(message)
            
            # Trigger Flyte task
            task = await remote.TaskDetails.fetch(
                project=request["project"],
                domain=request["domain"],
                name=request["task"],
                version=request["version"],
            )
            
            run = await flyte.run.aio(task, **request["inputs"])
            
            # Send run info back
            await websocket.send_json({
                "run_id": run.id,
                "url": run.url,
                "status": "started",
            })
            
            # Optionally stream updates
            async for update in run.stream():
                await websocket.send_json({
                    "status": update.status,
                    "message": update.message,
                })
    
    except WebSocketDisconnect:
        pass
```

## Client example

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

1. **Connection management**: Implement proper connection management and cleanup
2. **Error handling**: Handle WebSocket disconnections gracefully
3. **Message format**: Use JSON for structured messages
4. **Heartbeats**: Implement heartbeat/ping-pong to detect dead connections
5. **Rate limiting**: Consider rate limiting for WebSocket connections
6. **Authentication**: Implement authentication for WebSocket connections if needed
7. **Scalability**: Consider connection limits and scaling strategies

## Troubleshooting

**Connections dropping:**
- Check for timeout settings
- Implement heartbeat/ping-pong
- Review connection management code

**Messages not received:**
- Verify WebSocket protocol (ws:// vs wss://)
- Check message format and encoding
- Review error handling

**Performance issues:**
- Monitor connection count
- Implement connection pooling if needed
- Consider horizontal scaling

