import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../assets/xeokit-context-menu.css"
import store from "../store/index"
import * as ContextMenuParameters from "../features/contextMenuParameters";

export function contextMenu3dModel(model, viewer) {
    store.state.objectContextMenu = new ContextMenu({
        items: [
            [
                {
                    title: "Inspect Properties",
                    doAction: (context) => {
                        viewer.cameraControl.navMode = "planView"
                        IfcFlowTerminal:{
                         visible:false   
                        }
                        console.log("doactioncontext", context)
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
                        return context.viewer.localeService.translate("objectContextMenu.xrayOthers") || "X-Ray";
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
            [
                {
                    title: "Reset View",
                    doAction: function (context) {
                        viewer.camera.eye = [1838806.1036860247, 9.44347287346586, -5156481.191867573];
                        viewer.camera.look = [1838784.2194265071, 11.599380180651577, -5156512.788618103];
                        viewer.camera.up = [0.03188734217413631, 0.9984305577024861, 0.04603931857632314];
                        // context.viewer.cameraFlight.flyTo({
                        //     aabb: context.viewer.scene.getAABB()
                        // });
                    }
                }
            ],

            [
                {
                    title: "Capture Current View",
                    doAction: function (context) {
                        const eye = store.state.viewer.camera.eye;
                        const look = store.state.viewer.camera.look;
                        const up = store.state.viewer.camera.up;
                        console.log("eye", eye);
                        console.log("look", look);
                        console.log("up", up);
                    }
                }
            ],

            [

                {

                    getTitle: (context) => {
                        return "Fourth Floor";
                    },

                    doAction: function (context) {

                    },

                    items: [

                        [

                            {
                                getTitle: (context) => {
                                    return "Room No - 421"
                                },

                                doAction: function (context) {
                                    store.state.objectContextMenu.enabled = false
                                    ContextMenuParameters.contextMenufirstFloor(store.state.viewer);
                                    viewer.camera.eye = [1838784.226, 17.41054783, -5156525.58];
                                    viewer.camera.look = [1838784.212
                                        , 17.40368311
                                        , -5156525.627
                                    ];
                                    viewer.camera.up = [-0.040127462
                                        , 0.990154669
                                        , -0.134102643
                                    ];
                                }
                            },


                        ]
                    ]
                }
            ]

        ]
    });
    viewer.cameraControl.on("rightClick", function (e) {
    console.log("ee", e)
        var hit = viewer.scene.pick({
            canvasPos: e.canvasPos
        });

        if (hit && hit.entity.isObject) {

            store.state.objectContextMenu.context = { // Must set context before showing menu
                viewer: viewer,
                entity: hit.entity
            };

            store.state.objectContextMenu.show(e.pagePos[0], e.pagePos[1]);
        }

        e.event.preventDefault();
    });

}