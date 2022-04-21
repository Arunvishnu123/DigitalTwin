import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../assets/xeokit-context-menu.css"
import store from "../store/index"

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
            ],
            [
                {
                    title: "Hide",
                    doAction: function (context) {
                        context.entity.visible = false;
                    }
                },
                {
                    title: "Hide Others",
                    doAction: function (context) {
                        const viewer = context.viewer;
                        const scene = viewer.scene;
                        const entity = context.entity;
                        const metaObject = viewer.metaScene.metaObjects[entity.id];
                        if (!metaObject) {
                            return;
                        }
                        scene.setObjectsVisible(scene.visibleObjectIds, false);
                        metaObject.withMetaObjectsInSubtree((metaObject) => {
                            const entity = scene.objects[metaObject.id];
                            if (entity) {
                                entity.visible = true;
                            }
                        }); 
                    }
                },
                {
                    title: "Hide All",
                    getEnabled: function (context) {
                        return (context.viewer.scene.visibleObjectIds.length > 0);
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
                    getTitle: (context) => {
                        return context.viewer.localeService.translate("objectContextMenu.xray") || "X-Ray";
                    },
                    getEnabled: (context) => {
                        return (!context.entity.xrayed);
                    },
                    doAction: (context) => {
                        const entity = context.entity;
                        entity.xrayed = true;
                        entity.pickable = context.bimViewer.getConfig("xrayPickable");
                    }
                },
                {
                    getTitle: (context) => {
                        return context.viewer.localeService.translate("objectContextMenu.xrayOthers") || "X-Ray Others";
                    },
                    doAction: (context) => {
                        const viewer = context.viewer;
                        const scene = viewer.scene;
                        const entity = context.entity;
                        const metaObject = viewer.metaScene.metaObjects[entity.id];
                        if (!metaObject) {
                            return;
                        }
                        scene.setObjectsVisible(scene.objectIds, true);
                        scene.setObjectsXRayed(scene.objectIds, true);
                        if (!context.bimViewer.getConfig("xrayPickable")) {
                            scene.setObjectsPickable(scene.objectIds, false);
                        }
                        metaObject.withMetaObjectsInSubtree((metaObject) => {
                            const entity = scene.objects[metaObject.id];
                            if (entity) {
                                entity.xrayed = false;
                                entity.pickable = true;
                            }
                        });
                    }
                },
                {
                    getTitle: (context) => {
                        return context.viewer.localeService.translate("objectContextMenu.xrayAll") || "X-Ray All";
                    },
                    getEnabled: (context) => {
                        const scene = context.viewer.scene;
                        return (scene.numXRayedObjects < scene.numObjects);
                    },
                    doAction: (context) => {
                        const scene = context.viewer.scene;
                        scene.setObjectsVisible(scene.objectIds, true);
                        if (!context.bimViewer.getConfig("xrayPickable")) {
                            scene.setObjectsPickable(scene.objectIds, false);
                        }
                        scene.setObjectsXRayed(scene.objectIds, true);
                    }
                },
                {
                    getTitle: (context) => {
                        return context.viewer.localeService.translate("objectContextMenu.xrayNone") || "X-Ray None";
                    },
                    getEnabled: (context) => {
                        return (context.viewer.scene.numXRayedObjects > 0);
                    },
                    doAction: (context) => {
                        const scene = context.viewer.scene;
                        const xrayedObjectIds = scene.xrayedObjectIds;
                        scene.setObjectsPickable(xrayedObjectIds, true);
                        scene.setObjectsXRayed(xrayedObjectIds, false);
                    }
                }
            ],
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