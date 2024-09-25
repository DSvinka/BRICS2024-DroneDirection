import {trackerClient} from "./api.base.js";

export function sendTrackerSearchCommand() {
    trackerClient.post('/search')
}

export function sendTrackerCenteringCommand() {
    trackerClient.post('/centering')
}

export function sendTrackerCalibrationCommand() {
    trackerClient.post('/calibration')
}

export function sendTrackerStopCommand() {
    trackerClient.post('/stop')
}