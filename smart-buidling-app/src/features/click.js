import store from "../store/index"


export function clickSensorData() {
    store.state.viewer.cameraControl.on("picked", (pickResult) => {
        if (pickResult.entity.id == "1bDMdL0k55X8oOMH5VK_cb") {
            console.log("id clicked");
            store.state.temeperatureRealTime = true
           
        }
    })
}