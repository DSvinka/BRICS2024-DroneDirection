import asyncio
import base64
import json

from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from starlette.websockets import WebSocket, WebSocketDisconnect

from models.command_type import CommandType
from services.serial_service import SerialService
from services.video_processing_service import VideoProcessingService

app = FastAPI()
serial_service = SerialService("/dev/ttyUSB0", 9600, simulate_mode=True)
video_processing_service = VideoProcessingService(camera_index=0)

# Video sender websocket
@app.websocket("/ws")
async def get_stream(
        websocket: WebSocket,
        serial: SerialService=Depends(lambda: serial_service),
        video_processing: VideoProcessingService=Depends(lambda: video_processing_service)
):
    await websocket.accept()
    try:
        # TODO: Попробовать добавить Threading для уменьшения нагрузки при подключении нескольких клиентов.
        print("[WebSocket] Client connected")
        async for frame in video_processing.get_video_frame_generator():
            serial.processing()

            if frame is None:
                print("[WebSocket] Camera error, wait 5 seconds and resend...")
                await asyncio.sleep(5)
                continue

            await websocket.send_json(
                json.dumps({"dataType": "data", "signals": list(serial.signals)})
            )

            frame_bytes = base64.b64encode(frame)
            frame_encoded = frame_bytes.decode()
            await websocket.send_json(
                json.dumps({"dataType": "img", "img": frame_encoded})
            )

    except WebSocketDisconnect:
        await websocket.close(code=1000)
        print("[WebSocket] Client disconnected")


# Tracker
@app.post("/api/tracker/search", status_code=200)
async def tracker_search(serial: SerialService=Depends(lambda: serial_service)) -> None:
    """Команда поиска"""
    serial.send_command(CommandType.SEARCH)
    return

@app.post("/api/tracker/centering", status_code=200)
async def tracker_centering(serial: SerialService=Depends(lambda: serial_service)) -> None:
    """Команда центровки"""
    serial.send_command(CommandType.CENTERING)
    return

@app.post("/api/tracker/calibration", status_code=200)
async def tracker_calibration(serial: SerialService=Depends(lambda: serial_service)) -> None:
    """Команда калибровки"""
    serial.send_command(CommandType.CALIBRATION)
    return

@app.post("/api/tracker/stop", status_code=200)
async def tracker_stop(serial: SerialService=Depends(lambda: serial_service)) -> None:
    """Команда остановки"""
    serial.send_command(CommandType.STOP)
    return


# Channels
@app.post("/api/channel/up", status_code=200)
async def tracker_up(serial: SerialService=Depends(lambda: serial_service)) -> None:
    """Команда "повышения" канала"""
    serial.send_command(CommandType.CHANNEL_UP)
    return

@app.post("/api/channel/down", status_code=200)
async def tracker_down(serial: SerialService=Depends(lambda: serial_service)) -> None:
    """Команда "понижения" канала"""
    serial.send_command(CommandType.CHANNEL_DOWN)
    return

@app.post("/api/channel/auto", status_code=200)
async def tracker_auto(serial: SerialService=Depends(lambda: serial_service)) -> None:
    """Команда автоматического поиска канала"""
    serial.send_command(CommandType.CHANNEL_AUTO)
    return

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="BRICS2024 - Drone Direction",
        version="1.0.0",
        description="Система наведения направленной антенны без использования системы навигации для увеличения дальности связи дронов",
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
