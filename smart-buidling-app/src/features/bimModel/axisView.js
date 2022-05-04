import {
    AxisGizmoPlugin
} from "@xeokit/xeokit-sdk/";

export function viewAxis(canvasID, viewer) {
    new AxisGizmoPlugin(viewer, {
        canvasId: canvasID,
    });
}