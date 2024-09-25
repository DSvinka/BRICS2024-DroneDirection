import {channelClient} from "./api.base.js";

export function sendChannelUpCommand() {
    channelClient.post('/up')
}

export function sendChannelDownCommand() {
    channelClient.post('/down')
}

export function sendChannelAutoCommand() {
    channelClient.post('/auto')
}