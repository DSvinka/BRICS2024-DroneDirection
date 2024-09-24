<template>
  <canvas ref="root" class="canvas-gauges"></canvas>
</template>

<script setup>
import { RadialGauge } from 'canvas-gauges'
import {onBeforeUnmount, onMounted, ref, watch, watchEffect} from "vue";

const root = ref(null)

const props = defineProps({
  value: Number,
  options: {
    type: Object,
    default: () => ({})
  }
})

const chart = ref(null)

function updateCanvas() {
  if (props.value) props.options.value = props.value
  props.options.renderTo = root
  chart.value.update(props.options)
}

onMounted(() => {
  if (props.value) props.options.value = props.value
  props.options.renderTo = root
  chart.value = new RadialGauge(props.options).draw()
})

watch(() => props.value, () => {
  chart.value.value = props.value
})

onBeforeUnmount(() => {
  chart.value.destroy()
})

defineExpose({updateCanvas})
</script>
