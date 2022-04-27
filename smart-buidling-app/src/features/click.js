import store from "../store/index"


export function clickSensorData(id) {
    store.state.viewer.cameraControl.on("picked", (pickResult) => {
        if (pickResult.entity.id == id) {
            console.log("id clicked");
            store.state.temeperatureRealTime = true
           
        }
    })
}