# Структура файлов проекта

<figure><img src="../.gitbook/assets/{9738825E-C426-45AD-812F-CE2E254BD9B9}.png" alt=""><figcaption></figcaption></figure>

<details>

<summary>Models - Модели данных, типы, Enum</summary>

`command_type` - Содержит класс `CommandType` который наследуется от Enum и определяет какая команда будет отправлена на Arduino.

![](../.gitbook/assets/{1C95B30C-15D8-40D1-B3F1-C45A8E5BE027}.png)

</details>

<details>

<summary>Services - Вспомогательные классы для работы с определёнными компонентами проекта.</summary>

`serial_service` - Сервис для отправки команд и получения телеметрии с Arduino.

`video_processing_service` - Сервис для получения и обработки видеопотока с приемника.

</details>

`config.py` - Хранит конфигурации приложения.

`example.config.py` - Пример заполнения конфигурации приложения.

`main.py` - Главный файл приложения.

`requirements.txt` - Файл со списком необходимых пакетов для установки.
