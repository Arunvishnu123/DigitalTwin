<template>
<div>
    <canvas id="Canvas"> </canvas>
    <canvas id="NavCubeCanvas"></canvas>
    <canvas id="AxisGizmoCanvas"></canvas>
    <canvas id="SectionPlanesOverviewCanvas"></canvas>

</div>
</template>

<script>
import * as floorView from "../features/floorView";
import {
    Viewer,
    NavCubePlugin,
    AxisGizmoPlugin,
    SectionPlanesPlugin
} from "@xeokit/xeokit-sdk/";
export default {
    mounted() {
        const viewer = new Viewer({
            canvasId: "Canvas",
        });
        new NavCubePlugin(viewer, {
            canvasId: "NavCubeCanvas",
            // color: "lightblue",
            visible: true,
            cameraFly: true,
            cameraFitFOV: 45,
            cameraFlyDuration: 0.5,
        });
        new AxisGizmoPlugin(viewer, {
            canvasId: "AxisGizmoCanvas",
        });

        floorView.floorView("3_b98WEDT7feUaJ_WJeW_M", viewer);
        const sectionPlanes = new SectionPlanesPlugin(viewer, {
            overviewCanvasId: "SectionPlanesOverviewCanvas",
            overviewVisible: true
        });
        viewer.scene.input.on("mouseup", function (coords) {
            var hit = viewer.scene.pick({
                canvasPos: coords,
                pickSurface: true // <<------ This causes picking to find the intersection point on the entity
            });
            if (hit) {
                if (hit.entity.isObject) { // Only create CrossSections on surfaces of model objects, not on gizmos etc

                    const sectionPlane = sectionPlanes.createSectionPlane({
                        canvasPos: hit.canvasPos,
                        pos: hit.worldPos,
                        dir: [-hit.worldNormal[0], -hit.worldNormal[1], -hit.worldNormal[2]]
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
#Canvas {
    height: 100%;
    width: 100%;
    position: absolute;
    background: lightblue;
    background-image: linear-gradient(lightblue, white);
}

#NavCubeCanvas {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 100px;
    left: 1300px;
    z-index: 200000;
}

#AxisGizmoCanvas {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 100px;
    left: 50px;
    z-index: 200000;
}

#SectionPlanesOverviewCanvas {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 70px;
    right: 10px;
    z-index: 200000;
}
</style>
