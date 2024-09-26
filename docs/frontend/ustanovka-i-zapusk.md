# Установка и Запуск

## **Инструкция по запуску:**

1. Установите **node.js** если этого не сделали;
2. Находясь в дериктории с проектом, пропишите в консоль `npm install` для установки зависимостей;
3. Переименуйте `.env.example` в `.env`;
4. Измените значения в файле `.env` на свои;
5.
   * Либо запустите тестовый сервер с помощью команды `npm run dev`
   * Либо сделайте сборку проекта - `npm build` и загрузите файлы из папки `dist` на ваш веб сервер (например в `/var/www/html`)

***

## **Описание параметров `.env`:**

<table data-full-width="true"><thead><tr><th align="center">Параметр</th><th align="center">Описание</th><th align="center">Значение по умолчанию</th></tr></thead><tbody><tr><td align="center">VITE_API_URL</td><td align="center">Базовая ссылка на Api (backend)</td><td align="center">http://localhost:3000/api</td></tr><tr><td align="center">VITE_WEBSOCKET_URL</td><td align="center">Ссылка на WebSocket (backend)</td><td align="center">http://localhost:3000/ws</td></tr></tbody></table>
