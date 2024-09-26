# Структура файлов проекта

<div align="center" data-full-width="true">

<figure><img src="../.gitbook/assets/{F56FE0F0-0257-4290-B102-A59D33DA4DD4}.png" alt="" width="218"><figcaption></figcaption></figure>

</div>

<details>

<summary>Components - Компоненты используемые в проекте</summary>

`RadiantGauge` - Компонент для отрисовки циферблатных индикаторов. Используется для отображения силы сигнала на каждой антенне.

<img src="../.gitbook/assets/{0C134AA4-EDDC-4B8B-B6C9-62DC93B2328B}.png" alt="" data-size="original">           ![](<../.gitbook/assets/{6684F018-A9B8-4235-AA9F-1C0F983AB1A0} (1).png>)

`ThemeChanger` - Компонент кнопки для смены темы со светлой на тёмную и наоборот.

![](<../.gitbook/assets/изображение (3).png>)       ![](<../.gitbook/assets/изображение (2).png>)

`VideoStream` - Компонент отвечающий за получение и отображение видеопотока и телеметрии с WebSocket подключения.&#x20;

</details>

<details>

<summary>Services - Вспомогательные скрипты для работы с Бекендом</summary>

`api.base.js` - Обработка конфигураций из `.env` и создание Axios и WebSocket клиентов для отправки запросов.

`api.channel.js` - Отправка запросов связанных с управлением каналом.

`api.tracker.js` - Отправка запросов связанных с управлением трекером.

</details>

<details>

<summary>Stores - Хранение состояния приложения</summary>

`connections.store.js` - Хранение состояния подключения и пинг подключения.

`signals.store.js` - Хранит текущую силу сигнала на антеннах.

</details>

`App.vue` - Само приложение.

`main.js` - Точка с которой стартует инициализация приложения.

`.env` - Конфигурационный файл приложения

`.env.example` - Пример заполнения конфигурационного файла приложения
