from typing import AsyncGenerator, Any

import cv2


class VideoProcessingService:
    __camera: cv2.VideoCapture
    __camera_index: int

    def __init__(self, camera_index: int=0) -> AsyncGenerator[bytes | None, Any]:
        self.__camera = cv2.VideoCapture(camera_index)
        self.__camera_index = camera_index

    async def get_video_frame_generator(self) -> AsyncGenerator[bytes | None, Any]:
        while True:
            success, frame = self.__camera.read()
            if not success:
                self.__camera = cv2.VideoCapture(self.__camera_index)
                print('[Camera] Failed to capture frame')
                yield None
            else:
                _, buffer = cv2.imencode('.jpg', frame)
                yield buffer.tobytes()