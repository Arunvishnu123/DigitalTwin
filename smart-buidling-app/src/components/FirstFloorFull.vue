<template>
<div>
    <canvas id="Canvas100"> </canvas>
    <canvas id="NavCubeCanvas100"></canvas>
    <canvas id="AxisGizmoCanvas100"></canvas>
    <canvas id="SectionPlanesOverviewCanvas100"></canvas>
</div>
</template>

<script>
import * as floorView from "../features/floorView";
import {
    Viewer,
    NavCubePlugin,
    AxisGizmoPlugin,
    SectionPlanesPlugin,
} from "@xeokit/xeokit-sdk/";
export default {
    mounted() {
        const viewer = new Viewer({
            canvasId: "Canvas100",
        });
        new NavCubePlugin(viewer, {
            canvasId: "NavCubeCanvas100",
            // color: "lightblue",
            visible: true,
            cameraFly: true,
            cameraFitFOV: 45,
            cameraFlyDuration: 0.5,
        });
        new AxisGizmoPlugin(viewer, {
            canvasId: "AxisGizmoCanvas100",
        });

        floorView.floorView("3_b98WEDT7feUaJ_WJeWog", viewer);
        const sectionPlanes = new SectionPlanesPlugin(viewer, {
            overviewCanvasId: "SectionPlanesOverviewCanvas100",
            overviewVisible: true,
        });
        viewer.camera.eye = [
            1838806.1036860247, 9.44347287346586, -5156481.191867573,
        ];
        viewer.camera.look = [
            1838784.2194265071, 11.599380180651577, -5156512.788618103,
        ];
        viewer.camera.up = [
            0.03188734217413631, 0.9984305577024861, 0.04603931857632314,
        ];
        viewer.scene.input.on("mouseup", function (coords) {
            var hit = viewer.scene.pick({
                canvasPos: coords,
                pickSurface: true, // <<------ This causes picking to find the intersection point on the entity
            });
            if (hit) {
                if (hit.entity.isObject) {
                    // Only create CrossSections on surfaces of model objects, not on gizmos etc

                    const sectionPlane = sectionPlanes.createSectionPlane({
                        canvasPos: hit.canvasPos,
                        pos: hit.worldPos,
                        dir: [
                            -hit.worldNormal[0],
                            -hit.worldNormal[1],
                            -hit.worldNormal[2],
                        ],
                    });

                    sectionPlanes.showControl(sectionPlane.id);
                }
            }
        });
        window.viewer = viewer;
    },
};
</script>

<style scoped>
#Canvas100 {
    top: 0px;
    height: 100%;
    width: 100%;
    position: absolute;
    background: lightblue;
    background-image: linear-gradient(lightblue, white);
}

#NavCubeCanvas100 {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 100px;
    left: 1300px;
    z-index: 200000;
}

#AxisGizmoCanvas100 {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 100px;
    left: 50px;
    z-index: 200000;
}

#SectionPlanesOverviewCanvas100 {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 70px;
    right: 10px;
    z-index: 200000;
}
</style>
