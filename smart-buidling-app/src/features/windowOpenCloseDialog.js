import store from "../store/index"


export function clickPersonData() {
    store.state.viewer.cameraControl.on("picked", (pickResult) => {
        if (pickResult.entity.id == "1jMGJTzbX0Gu65H0cXPmD5") {
            console.log("id clicked");
            store.state.windowOpenDialog = true
           
        }
    })
}