---
description: В приложении используется 2 хранилища состояния.
---

# Хранилище состояния

{% tabs %}
{% tab title="Connections Store" %}
### Состояние (State)

<table><thead><tr><th width="312">Параметр</th><th width="151">Тип Данных</th><th>Значение по умолчанию</th></tr></thead><tbody><tr><td>webSocketInConnecting</td><td>Boolean</td><td>false</td></tr><tr><td>webSocketConnected</td><td>Boolean</td><td>false</td></tr><tr><td>lastMessageTime</td><td>Date</td><td>null</td></tr></tbody></table>

### Действия (Actions)

| Название Функции | Действие                                                        |
| ---------------- | --------------------------------------------------------------- |
| updateTime()     | Записывает в `lastMessageTime` текущую дату, время `(new Date)` |
| resetTime()      | Записывает в `lastMessageTime` значение `null`                  |

### Свойства (Getters)

| Название       | Что возвращает                                                                           |
| -------------- | ---------------------------------------------------------------------------------------- |
| pingMs         | Разницу между текущим временем и записаным в `lastMessageTime`                           |
| checkTryAgain  | Возвращает `true` если `WebSocket` не подключен и не предпренимается попытка подключения |
| isNotConnected | Возвращает `true` если `WebSocket` не подключен или предпринимается попытка подключения  |
{% endtab %}

{% tab title="Signals Store" %}
### Состояние (State)

<table><thead><tr><th width="312">Параметр</th><th width="151">Тип Данных</th><th>Значение по умолчанию</th></tr></thead><tbody><tr><td>signals</td><td>List&#x3C;Number></td><td>[-2, -2, -2, -2]</td></tr></tbody></table>

### Действия (Actions)

Отсутствуют

### Геттеры (Getters)

Отсутствуют
{% endtab %}
{% endtabs %}

