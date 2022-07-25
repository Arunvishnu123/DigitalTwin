import store from "../../store/index"


export function getID(viewer)

 {
    store.state.viewer.cameraControl.on("picked", (coords) => {
            const objectId = coords.entity.id;
            const v = viewer.metaScene.metaObjects[objectId]
            store.state.thingIfcId= v.id
            store.state.thingifcClass = v.type
    
        })
    
}
