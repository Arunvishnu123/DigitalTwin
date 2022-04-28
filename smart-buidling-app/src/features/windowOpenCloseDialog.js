import store from "../store/index"


export function clickPersonData(id) {
    store.state.viewer.cameraControl.on("picked", (pickResult) => {
        if (pickResult.entity.id == id) {
            console.log("id clicked");
            store.state.windowOpenDialog = true
           
        }
    })
}