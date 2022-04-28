import store from "../store/index"

export function hoverOver(id) {
    store.state.viewer.cameraControl.on("hover", (pickResult) => {
        if (pickResult.entity.id == id) {
            console.log("id clicked");
        } else {
            console.log("notclcickedd")
        }
    })
}