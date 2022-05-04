import {
    NavCubePlugin
} from "@xeokit/xeokit-sdk/";

export function navCubeView(canvasID, viewer) {

    new NavCubePlugin(viewer, {
        canvasId: canvasID,
        //color: "lightblue",
        visible: true,
        cameraFly: true,
        cameraFitFOV: 45,
        cameraFlyDuration: 0.5,
    });
}