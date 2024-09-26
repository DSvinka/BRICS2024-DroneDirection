import {defineStore} from "pinia";

export const useConnectionsStore = defineStore('connections', {
    state: () => ({
        webSocketInConnecting: false,
        webSocketConnected: false,

        lastMessageTime: null
    }),
    actions: {
        updateTime() {
            this.lastMessageTime = new Date();
        },
        resetTime() {
            this.lastMessageTime = null;
        }
    },
    getters: {
        pingMs: state => state.lastMessageTime ? new Date().getMilliseconds() - state.lastMessageTime.getMilliseconds() : '???',
        checkTryAgain: (state) => !state.webSocketInConnecting && !state.webSocketConnected,
        isNotConnected: (state) => state.webSocketInConnecting || !state.webSocketConnected,
    },
})