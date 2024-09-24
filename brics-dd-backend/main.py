from fastapi import FastAPI, Response, Depends
from fastapi.responses import StreamingResponse
import cv2
from starlette.websockets import WebSocket, WebSocketDisconnect

app = FastAPI()

# Инициализация камеры
camera = cv2.VideoCapture(1)
# Обычно 0 - это первая камера


async def get_video_frame(camera):
    while True:
        success, frame = camera.read()
        if not success:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        yield buffer.tobytes()

@app.websocket("/ws")
async def get_stream(websocket: WebSocket, camera=Depends(lambda: camera)):
    await websocket.accept()
    try:
        async for frame in get_video_frame(camera):
            await websocket.send_bytes(frame)
    except WebSocketDisconnect:
        await websocket.close(code=1000)
        print("Client disconnected")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
