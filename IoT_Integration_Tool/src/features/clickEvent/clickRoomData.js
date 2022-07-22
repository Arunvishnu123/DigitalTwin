import store from "../../store/index"


export function clickSensorData() {
    store.state.viewer.cameraControl.on("picked", (pickResult) => {
        if (pickResult.entity.id == "26RvPR7OX7XPFMpPoB2VUB") {
            console.log("id clicked");
            store.state.roomDialog = true

        }
    })
}