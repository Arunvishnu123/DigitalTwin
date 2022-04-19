import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../assets/xeokit-context-menu.css"
import store from "../store/index"

export function contextMenufirstFloor(viewer) {
    const objectContextMenu = new ContextMenu({

        items: [
            [
                {
                    getTitle: (context) => {
                        console.log("gettitle", context)
                        return "Temperature";
                    },
                    doAction: (context) => {
                       store.state.testDialog = true
                        
                    }
                },
                {
                    title: "Humidity",
                    getEnabled: function (context) {
                        const scene = context.viewer.scene;
                        return (scene.numVisibleObjects < scene.numObjects);
                    },
                    doAction: function (context) {
                        
                    }
                }
            ],
            [
                {
                    title: "View Fit All",
                    doAction: function (context) {
                        context.viewer.cameraFlight.flyTo({
                            aabb: context.viewer.scene.getAABB()
                        });
                    }
                }
            ]
        ]
    });
    viewer.cameraControl.on("rightClick", function (e) {

        var hit = viewer.scene.pick({
            canvasPos: e.canvasPos
        });

        if (hit && hit.entity.isObject) {

            objectContextMenu.context = { // Must set context before showing menu
                viewer: viewer,
                entity: hit.entity
            };

            objectContextMenu.show(e.pagePos[0], e.pagePos[1]);
        }

        e.event.preventDefault();

    })


}
