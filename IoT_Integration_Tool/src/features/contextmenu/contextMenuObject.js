import {
    ContextMenu
} from "@xeokit/xeokit-sdk/";
import "../../assets/styles/xeokit-context-menu.css"
import store from "../../store/index"
import * as floorView from "../floorViews/floorView"

export function contextMenu3dModel(model, viewer) {
    store.state.objectContextMenu = new ContextMenu({
        items: [[
            {
                title: "Add new Thing",
                doAction: (context) => {
                 store.state.createThing = true
                }
            }
        ] , 
        [
            {
                title: "Add new Employee",
                doAction: (context) => {
                 store.state.createEmployee = true
                 console.log(store.state.createEmployee)
                 console.log("cicksdfjsdhfdfhdsfhdfshdfsdhfhh")
                }
            }
        ] ,
            [{
                    title: "Plan View",
                    doAction: (context) => {
                        viewer.cameraControl.navMode = "planView"
                    }
                },
                {
                    title: "First Person View",
                    doAction: (context) => {
                        viewer.cameraControl.navMode = "firstPerson"
                    }
                },
                {
                    title: "Camera Orbit",
                    doAction: (context) => {
                        viewer.cameraControl.navMode = "orbit"
                    }
                }
            ],
            [{
                title: "View Fit All",
                doAction: function (context) {
                    context.viewer.cameraFlight.flyTo({
                        aabb: context.viewer.scene.getAABB()
                    });
                }
            }],
            [{
                title: "Fly to Object",
                doAction: function (context) {
                    const viewer = context.viewer;
                    const entity = context.entity;
                    viewer.cameraFlight.flyTo({
                        aabb: entity.aabb,
                        duration: 0.5
                    }, () => {});
                }
            }],

            [{
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
            
            [{
                title: "Reset View",
                doAction: function (context) {

                    viewer.camera.eye = [1838806.1036860247, 9.44347287346586, -5156481.191867573];
                    viewer.camera.look = [1838784.2194265071, 11.599380180651577, -5156512.788618103];
                    viewer.camera.up = [0.03188734217413631, 0.9984305577024861, 0.04603931857632314];
                    // context.viewer.cameraFlight.flyTo({
                    //     aabb: context.viewer.scene.getAABB()
                    // });
                }
            }],
        ]
    });
    viewer.cameraControl.on("rightClick", function (e) {
        console.log("ee", e)
        var hit = viewer.scene.pick({
            canvasPos: e.canvasPos
        });

        console.log("hit" , hit)

        const objectId = hit.entity.id;
        const v = viewer.metaScene.metaObjects[objectId]
        store.state.thingIfcId= v.id
        store.state.thingifcClass = v.type

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