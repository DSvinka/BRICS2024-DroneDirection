# WebSocket

Для подключения по WebSocket необходимо обратиться к конечной точке `/ws` (то есть полностью будет `ws://localhost:3000`**`/ws`**)&#x20;

## **Возвращаемые значения:**

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><p>Сначала отправляется <code>json</code> с данными о сигналах с антенн. </p><pre class="language-json"><code class="lang-json">{
    "dataType": "data", 
    "signals": [70, 80, 120, 200]
}
</code></pre></td><td></td><td></td></tr><tr><td>Затем отправляется <code>json</code> c закодированными в строку байтами изображения.</td><td><pre class="language-json"><code class="lang-json"><strong>{
</strong>    "dataType": "img", 
    "img": "ZLg/fUjeOSubs&#x3C;...>"
}
</code></pre></td><td></td></tr></tbody></table>

Различать типы данных можно по значению ключа `dataType`
