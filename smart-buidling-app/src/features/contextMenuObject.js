import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../assets/xeokit-context-menu.css"

export function contextMenu3dModel(viewer) {
    const objectContextMenu = new ContextMenu({
        items: [
            [
                {
                    getTitle: (context) => {
                         console.log("gettitle",context)
                        return context.viewer.localeService.translate("objectContextMenu.inspectProperties") || "Inspect Properties";
                    },
                    doAction: (context) => {
                        console.log("doactioncontext",context)
                        const objectId = context.entity.id;
                        console.log(objectId)
                        console.log(context.viewer.metaScene.metaObjects[objectId]);
                        console.log("test")
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