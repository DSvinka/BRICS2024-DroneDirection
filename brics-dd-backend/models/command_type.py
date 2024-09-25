from enum import Enum


class CommandType(Enum):
    CALIBRATION = 0x01
    SEARCH = 0x02
    STOP = 0x03
    CENTERING = 0x04

    CHANNEL_UP = 0x05
    CHANNEL_DOWN = 0x06
    CHANNEL_AUTO = 0x07