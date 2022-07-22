import store from "../../store/index"


export function getKG(viewer)
 {
    store.state.viewer.cameraControl.on("picked", (coords) => {
            console.log(coords)
            const objectId = coords.entity.id;
            const v = viewer.metaScene.metaObjects[objectId]
            console.log(v.id)
            console.log(v.type)
            store.state.id = v.id
            store.state.class = v.type
            store.state.url = "http://localhost:4000/" + v.type + "/" + v.id
            store.state.humiditydisplay = true
        })
    
}
