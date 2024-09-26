<script setup>
import {onMounted, onUnmounted, ref} from "vue";

import {useSignalsStore} from "../stores/signals.store.js";
import {useConnectionsStore} from "../stores/connections.store.js";

import {storeToRefs} from "pinia";

import { useNotification } from "@kyvg/vue3-notification";
import {webSocketUrl} from "../services/api/api.base.js";

const { notify }  = useNotification()

const signalsStore = useSignalsStore()
const { signals } = storeToRefs(signalsStore)

const connectionsStore = useConnectionsStore()
const { webSocketInConnecting, webSocketConnected } = storeToRefs(connectionsStore)

const frame = ref(null)
const ws = ref(null)

function connect() {
  if (webSocketConnected.value)
    return;

  webSocketInConnecting.value = true;

  notify({title: "WebSocket", text: "Производится попытка подключения..."});

  ws.value = new WebSocket(webSocketUrl);

  ws.value.onmessage = function(event) {
    let data = JSON.parse(JSON.parse(event.data));

    if (data.dataType === "img") {
      frame.value.src = "data:image/jpg;base64,"+data.img;
    }

    if (data.dataType === "data") {
      signals.value = data.signals
    }

    connectionsStore.updateTime()
  };

  ws.value.onclose = function(event) {
    webSocketInConnecting.value = false;
    webSocketConnected.value = false;

    notify({type: "error", title: "WebSocket", text: `Не удалось произвести подключение!`});
    connectionsStore.resetTime()
  };

  ws.value.onopen = function(event) {
    webSocketInConnecting.value = false;
    webSocketConnected.value = true;

    notify({type: "success", title: "WebSocket", text: "Подключение к успешно создано!"});
    connectionsStore.resetTime()
  }
}

onMounted(() => {
  connect()
})

onUnmounted(() => {
  if (ws.value)
    ws.value.close();
})
</script>

<template>
  <v-skeleton-loader :loading="!webSocketConnected" width="100%" color="surface" type="image">
    <img ref="frame" src="" alt="video">
  </v-skeleton-loader>

  <v-btn v-if="!webSocketConnected" :loading="webSocketInConnecting" class="position-absolute" @click="connect">Попробовать ещё раз</v-btn>
</template>