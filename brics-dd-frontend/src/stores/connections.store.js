import {defineStore} from "pinia";

export const useConnectionsStore = defineStore('connections', {
    state: () => ({
        webSocketInConnecting: false,
        webSocketConnected: false
    }),
    getters: {
        checkTryAgain: (state) => !state.webSocketInConnecting && !state.webSocketConnected,
        isNotConnected: (state) => state.webSocketInConnecting || !state.webSocketConnected,
    },
})