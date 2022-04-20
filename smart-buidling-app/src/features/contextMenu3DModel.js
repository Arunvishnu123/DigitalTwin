import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../assets/xeokit-context-menu.css"
import store from "../store/index"

export function contextMenu3dModel(viewer) {
    const canvasContextMenu = new ContextMenu({
        enabled: true,
        context: {
            viewer: viewer
        },
        items: [
            [
                {
                    title: "Hide All",
                    getEnabled: function (context) {
                        return (context.viewer.scene.numVisibleObjects > 0);
                    },
                    doAction: function (context) {
                        context.viewer.scene.setObjectsVisible(context.viewer.scene.visibleObjectIds, false);
                    }
                },
                {
                    title: "Show All",
                    getEnabled: function (context) {
                        const scene = context.viewer.scene;
                        return (scene.numVisibleObjects < scene.numObjects);
                    },
                    doAction: function (context) {
                        const scene = context.viewer.scene;
                        scene.setObjectsVisible(scene.objectIds, true);
                        scene.setObjectsXRayed(scene.xrayedObjectIds, false);
                        scene.setObjectsSelected(scene.selectedObjectIds, false);
                        store.state.selection = 0
                    }
                }
            ],
            [
                {
                    title: "Intial View",
                    doAction: function (context) {
                        viewer.camera.eye = [1838806.1036860247, 9.44347287346586, -5156481.191867573];
                        viewer.camera.look = [1838784.2194265071, 11.599380180651577, -5156512.788618103];
                        viewer.camera.up = [0.03188734217413631, 0.9984305577024861, 0.04603931857632314];
                        // context.viewer.cameraFlight.flyTo({
                        //     aabb: context.viewer.scene.getAABB()
                        // });
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

            console.log("test")
        }
        else {

            canvasContextMenu.context = { // Must set context before showing menu
                viewer: viewer
            };

            canvasContextMenu.show(e.pagePos[0], e.pagePos[1]);

            e.event.preventDefault();
        }

    });


}