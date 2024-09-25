import { createApp } from 'vue'
import { createPinia } from "pinia";

import Notifications from '@kyvg/vue3-notification'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import { aliases, mdi } from 'vuetify/iconsets/mdi-svg'

import App from './App.vue'



const lightTheme = {
    dark: false,
    colors: {
        'background': '#FFFFFF',
        'surface': '#FFFFFF',

        'primary': '#1867C0',
        'secondary': '#48A9A6',

        'error': '#B00020',
        'info': '#2196F3',
        'success': '#4CAF50',
        'warning': '#FB8C00',
    }
}

const darkTheme = {
    dark: true,
    colors: {
        'background': '#23272A',
        'surface': '#2C2F33',

        'primary': '#99AAB5',
        'secondary': '#FFFFFF',

        "hover": "#FFFFFF",

        'error': '#B00020',
        'info': '#2196F3',
        'success': '#4CAF50',
        'warning': '#FB8C00',
    }
}

const vuetify = createVuetify({
    components,
    directives,
    icons: {
        defaultSet: 'mdi',
        aliases,
        sets: {
            mdi,
        },
    },
    theme: {
        defaultTheme: 'lightTheme',
        themes: {
            lightTheme, darkTheme
        }
    }
})


const pinia = createPinia()
const app = createApp(App)

app.use(vuetify)
app.use(pinia)
app.use(Notifications)
app.mount('#app')
