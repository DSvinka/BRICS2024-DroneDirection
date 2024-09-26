import random

from serial import Serial
from serial.serialutil import SerialException

from models.command_type import CommandType


class SerialService:
    signals: tuple[int, int, int, int]
    __serial: Serial

    __simulate_mode: bool
    __simulate_counter: int = 0

    def __init__(self, ports: list[str], baudrate: int=9600, simulate_mode: bool = False):
        if not simulate_mode:
            for port in ports:
                print(f"[Serial {port}] Connecting...")
                try:
                    self.__serial = Serial(port, baudrate, timeout=1)
                    print(f"[Serial {port}] Connected successfully!")
                except SerialException:
                    print(f"[Serial {port}] Not connected")

        self.__simulate_mode = simulate_mode
        self.signals = (-1, -1, -1, -1)

    def processing(self) -> None:
        # Режим симуляции для тестирования
        if self.__simulate_mode:
            self.__simulate_counter -= 1

            if self.__simulate_counter > 0:
                return

            self.signals = (
                random.randrange(0, 400),
                random.randrange(0, 400),
                random.randrange(0, 400),
                random.randrange(0, 400)
            )
            self.__simulate_counter = 50

            print(f"[Simulate Mode] Set {self.signals} signals")

        # Если режим симуляции выключен - проверяем есть ли сообщения
        elif self.__serial.in_waiting:
            response = (self.__serial.readline().decode()
                        .replace("\n", "")
                        .replace("\r", "")
                        .split(' '))

            print(f"[Serial {self.__serial.name}] Serial Response: {response}")

            self.signals = (int(response[0]), int(response[1]), int(response[2]), int(response[3]))


    def send_command(self, command: CommandType):
        if self.__simulate_mode:
            print(f"[Simulate Mode] Send {command.name} command ({command.value})")
        else:
            print(f"[Serial {self.__serial.name}] Send {command.name} command ({command.value})")
            self.__serial.write(command.value)
