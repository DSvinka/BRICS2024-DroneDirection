import axios from "axios";

import { useNotification } from "@kyvg/vue3-notification";
const { notify }  = useNotification()

export const apiUrl = import.meta.env.VITE_API_URL
export const webSocketUrl = import.meta.env.VITE_WEBSOCKET_URL;

export const channelClient = axios.create({
    baseURL: apiUrl+'/channel',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});

export const trackerClient = axios.create({
    baseURL: apiUrl+'/tracker',
    timeout: 1000,
    headers: {'X-Custom-Header': 'foobar'}
});

channelClient.interceptors.response.use(successHandler, errorHandler);
trackerClient.interceptors.response.use(successHandler, errorHandler);

function successHandler(response) {
    notify({type: "success", title: "Отправлено!"});
    return response;
}

function errorHandler(error) {
    notify({type: "error", title: "Ошибка!", text: error.message});
    return error;
}