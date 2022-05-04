import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../../assets/styles/xeokit-context-menu.css"
import store from "../../store/index"

export function contextMenufirstFloor(viewer) {
    const parameterContextMenu = new ContextMenu({

        items: [
            [{
                    getTitle: (context) => {
                        console.log("gettitle", context)
                        return "Temperature";
                    },
                    doAction: (context) => {
                        store.state.tempdisplay = true

                    }
                },
                {
                    title: "Humidity",
                    doAction: function (context) {
                        store.state.humiditydisplay = true
                    }
                },
                {
                    title: "Luminance",
                    doAction: function (context) {
                        store.state.luminancedisplay = true
                    }
                },
                {
                    title: "Room Details",
                    doAction: function (context) {
                        store.state.roomdisplay = true
                    }
                }
            ],
            [{
                title: "Reset View",
                doAction: function (context) {
                    viewer.camera.eye = [1838806.1036860247, 9.44347287346586, -5156481.191867573];
                    viewer.camera.look = [1838784.2194265071, 11.599380180651577, -5156512.788618103];
                    viewer.camera.up = [0.03188734217413631, 0.9984305577024861, 0.04603931857632314];
                    parameterContextMenu.enabled = false
                    store.state.objectContextMenu.enabled = true

                }
            }]
        ]
    });
    viewer.cameraControl.on("rightClick", function (e) {

        var hit = viewer.scene.pick({
            canvasPos: e.canvasPos
        });



        parameterContextMenu.context = { // Must set context before showing menu
            viewer: viewer,
            entity: hit.entity
        };

        parameterContextMenu.show(e.pagePos[0], e.pagePos[1]);


        e.event.preventDefault();

    })


}