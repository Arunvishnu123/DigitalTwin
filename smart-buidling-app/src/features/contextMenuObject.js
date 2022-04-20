import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../assets/xeokit-context-menu.css"
import * as FloorView from "../features/floorView";

export function contextMenu3dModel(model,viewer) {
    const objectContextMenu = new ContextMenu({
        items: [
            [
                {
                    title: "Inspect Properties",
                    doAction: (context) => {
                        console.log("doactioncontext",context)
                        const objectId = context.entity.id;
                        console.log(objectId)
                        console.log(context.viewer.metaScene.metaObjects[objectId]);
                        console.log("test")
                    }
                },
                {
                    title: "IsolateFloor",
                    doAction: function (context) {
                       
                      console.log("testzsdfdsfs")
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
    });

}