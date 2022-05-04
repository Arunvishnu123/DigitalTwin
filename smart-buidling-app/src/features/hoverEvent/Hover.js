import store from "../../store/index"

export function hoverOver() {
    store.state.viewer.cameraControl.on("hover", (pickResult) => {
        if (pickResult.entity.id =="1bDMdL0k55X8oOMH5VK_cb") {
            console.log("id clicked");
        } 
    })
}