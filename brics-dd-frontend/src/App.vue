<script setup>
import RadialGauge from "./components/RadialGauge.vue";
import {onMounted, ref} from "vue";
import {useDisplay, useTheme} from "vuetify";

import {mdiThemeLightDark} from "@mdi/js";
import VideoStream from "./components/VideoStream.vue";


import {useNotification} from "@kyvg/vue3-notification";
import {useSignalsStore} from "./stores/signals.store.js";
import {storeToRefs} from "pinia";

import {
  sendTrackerStopCommand, sendTrackerCenteringCommand,
  sendTrackerCalibrationCommand, sendTrackerSearchCommand
} from "./services/api/api.tracker.js"

import {
  sendChannelAutoCommand, sendChannelDownCommand, sendChannelUpCommand
} from "./services/api/api.channel.js"
import {Notifications} from "@kyvg/vue3-notification";
import {useConnectionsStore} from "./stores/connections.store.js";


const { notify }  = useNotification()

const { smAndUp, md } = useDisplay()
const theme = useTheme()

const signalsStore = useSignalsStore()
const { signals } = storeToRefs(signalsStore)

const connectionsStore = useConnectionsStore()
const { isNotConnected, pingMs } = storeToRefs(connectionsStore)

const radiantOptions = ref({
  units: "RSSI",
  height: 150,
  width: 150,
  minValue: 50,
  startAngle: 90,
  ticksAngle: 180,
  valueBox: false,
  maxValue: 400,
  majorTicks: [
    "50",
    "100",
    "150",
    "200",
    "250",
    "300",
    "350",
    "400"
  ],
  minorTicks: 10,
  strokeTicks: true,
  highlights: [
    {
      "from": 250,
      "to": 400,
      "color": "rgba(108,200,50,0.75)"
    }
  ],
  borderShadowWidth: 0,
  borders: false,
  needleType: "arrow",
  needleWidth: 2,
  needleCircleSize: 7,
  needleCircleOuter: true,
  needleCircleInner: false,
  animationDuration: 1500,
  animationRule: "linear"
})

const radiant1Ref = ref(null);
const radiant2Ref = ref(null);
const radiant3Ref = ref(null);
const radiant4Ref = ref(null);

function toggleTheme () {
  theme.global.name.value = theme.global.current.value.dark ? 'lightTheme' : 'darkTheme'

  setRadiantColors(theme.global.current.value)
}

function setRadiantColors(colors) {
  radiantOptions.value.colorMajorTicks = theme.global.current.value.dark ? "#ddd": "#232529"
  radiantOptions.value.colorMinorTicks = theme.global.current.value.dark ? "#ddd": "#232529"
  radiantOptions.value.colorTitle = theme.global.current.value.dark ? "#eee": "#2c2f33"
  radiantOptions.value.colorUnits = theme.global.current.value.dark ? "#ccc": "#232529"
  radiantOptions.value.colorNumbers = theme.global.current.value.dark ? "#eee": "#2c2f33"
  radiantOptions.value.colorPlate = theme.global.current.value.dark ? "#2c2f33": "#FFFFFF"

  radiant1Ref.value.updateCanvas()
  radiant2Ref.value.updateCanvas()
  radiant3Ref.value.updateCanvas()
  radiant4Ref.value.updateCanvas()
}
</script>

<template>
  <v-app>
    <v-container class="my-auto">
      <notifications position="bottom left" close-on-click :duration="3000"/>
      <v-row>
        <v-col cols="12" md="9">
          <v-card class="d-flex justify-center align-center">
            <video-stream />
          </v-card>

          <div class="d-flex justify-center align-center">
            <v-skeleton-loader class="mt-0 mt-md-2" width="100%" :loading="isNotConnected" type="card">
              <v-card class="mt-0 mt-md-2" width="100%">
                <v-card-title class="text-center">Сила Сигнала</v-card-title>

                <template v-if="smAndUp">
                  <div class="d-flex justify-center align-center" style="margin-bottom: -50px; ">
                    <span>
                      <radial-gauge ref="radiant1Ref" :value="signals[0]" :options="radiantOptions"/>
                    </span>
                    <span>
                      <radial-gauge ref="radiant2Ref" :value="signals[1]" :options="radiantOptions"/>
                    </span>
                    <span>
                      <radial-gauge ref="radiant3Ref" :value="signals[2]" :options="radiantOptions"/>
                    </span>
                    <span>
                      <radial-gauge ref="radiant4Ref" :value="signals[3]" :options="radiantOptions"/>
                    </span>
                  </div>
                </template>

                <template v-else>
                  <div class="d-flex justify-center align-center" style="margin-bottom: -50px; ">
                    <div>
                      <radial-gauge ref="radiant1Ref" :value="signals[0]" :options="radiantOptions"/>
                    </div>
                    <div>
                      <radial-gauge ref="radiant2Ref" :value="signals[1]" :options="radiantOptions"/>
                    </div>
                  </div>

                  <div class="d-flex justify-center align-center" style="margin-bottom: -50px; ">
                    <div>
                      <radial-gauge ref="radiant3Ref" :value="signals[2]" :options="radiantOptions"/>
                    </div>
                    <div>
                      <radial-gauge ref="radiant4Ref" :value="signals[3]" :options="radiantOptions"/>
                    </div>
                  </div>
                </template>

                <div class="text-center">Сигнал (RSSI): {{signals[0]}} / {{signals[1]}} / {{signals[2]}} / {{signals[3]}}</div>
                <div class="text-center">Пинг (мс): {{ pingMs }}</div>
              </v-card>
            </v-skeleton-loader>
          </div>
        </v-col>

        <v-col cols="12" md="3">
          <v-card max-width="100%">
            <v-card-title class="text-center" v-text="md ? 'Трекер' : 'Управление Трекером'"/>

            <v-card-text>

              <v-btn :loading="isNotConnected" @click="sendTrackerSearchCommand" block color="info" class="d-block my-2 mx-auto">Поиск</v-btn>
              <v-btn :loading="isNotConnected" @click="sendTrackerCenteringCommand" block color="info" class="d-block my-2 mx-auto">Центровка</v-btn>
              <v-btn :loading="isNotConnected" @click="sendTrackerCalibrationCommand" block color="success" class="d-block my-2 mx-auto">Калибровка</v-btn>
              <v-btn :loading="isNotConnected" @click="sendTrackerStopCommand" block color="error" class="d-block my-2 mx-auto">Стоп</v-btn>
            </v-card-text>
          </v-card>

          <v-card max-width="100%" class="mt-2">
            <v-card-title class="text-center" v-text="md ? 'Канал' : 'Управление каналом'"/>

            <v-card-text>
              <v-btn :loading="isNotConnected" @click="sendChannelUpCommand" block color="info" class="d-block my-2 mx-auto">Канал Выше</v-btn>
              <v-btn :loading="isNotConnected" @click="sendChannelDownCommand" block color="info" class="d-block my-2 mx-auto">Канал Ниже</v-btn>
              <v-btn :loading="isNotConnected" @click="sendChannelAutoCommand" block color="secondary" class="d-block my-2 mx-auto">Авто Канал</v-btn>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-fab :icon="mdiThemeLightDark" @click="toggleTheme" location="bottom" app/>
  </v-app>
</template>
