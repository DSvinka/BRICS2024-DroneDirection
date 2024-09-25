import {defineStore} from "pinia";

export const useSignalsStore = defineStore('signals', {
    state: () => ({ signals: [-2, -2, -2, -2] }),
})