# Установка и Запуск

## **Инструкция по запуску:**

1. Установите **Python 3.11** если этого не сделали.
2. Находясь в директории с проектом, пропишите в консоль `python3 -m venv venv` для создания виртуального окружения.
3. Зайдите в виртуальное окружение. (для Linux команда `source venv/bin/activate`)
4. Установите необходимые пакеты командой `pip install -r requirements.txt`
5. Переименуйте `example.config.py` в `config.py`
6. Измените значения в файле `config.py` на свои.
7. Запустите сервер разработки с помощью команды `python main.py`

***

## **Описание параметров `config.py`:**

<table data-full-width="true"><thead><tr><th align="center">Параметр</th><th width="453.3333333333333" align="center">Описание</th><th align="center">Значение по умолчанию</th></tr></thead><tbody><tr><td align="center">SERIAL_SIMULATION_MODE</td><td align="center">Режим симуляции Serial подключения к Arduino.<br>Нужна для тестирования работы без подключения к Arduino.</td><td align="center"><code>True</code></td></tr><tr><td align="center">ARDUINO_SERIAL_PORT</td><td align="center">Порт к которому подключена Arduino.</td><td align="center"><code>["/dev/ttyUSB0", "/dev/ttyUSB1"]</code></td></tr><tr><td align="center">ARDUINO_SERIAL_BAUDRATE</td><td align="center">Baudrate порта. (должна совпадать с той, что установлена на Arduino)</td><td align="center"><code>115200</code></td></tr><tr><td align="center">CAMERA_INDEX</td><td align="center">Порядковый номер камеры. (приемник подключается как веб-камера)<br>Если камер на устройстве нет - то устанавливаем 0.<br>Если камеры есть на устройстве (например на ноутбуке) - то необходимо указать последний номер, например 1</td><td align="center"><code>0</code></td></tr></tbody></table>
