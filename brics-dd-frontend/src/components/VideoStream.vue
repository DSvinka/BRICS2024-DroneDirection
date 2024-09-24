<script setup>
import {onMounted, onUnmounted, ref} from "vue";

const frame = ref(null)
const ws = ref(null)

onMounted(() => {
  ws.value = new WebSocket("ws://localhost:8000/ws");

  frame.value.onload = function(){
    URL.revokeObjectURL(this.src);
  };

  ws.value.onmessage = function(event) {
    frame.value.src = URL.createObjectURL(event.data);
  };

  ws.value.onclose = function(event) {
    console.log("WebSocket closed:", event);
  };
})

onUnmounted(() => {
  ws.value.close();
})
</script>

<template>
  <img ref="frame" src="">
</template>