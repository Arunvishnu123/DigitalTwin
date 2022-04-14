<template>
<div>
    <canvas id="myCanvas"></canvas>
    <canvas id="NavCubeCanvas"></canvas>
    <canvas id="AxisGizmoCanvas"></canvas>
</div>
</template>

<script>
import {
    Viewer,
    NavCubePlugin,AxisGizmoPlugin
} from "@xeokit/xeokit-sdk/";
import * as display3d from "../features/view3D"

export default {

    mounted() {
        const viewer = new Viewer({
            canvasId: "myCanvas",
        });
        display3d.display3d(viewer)

        new NavCubePlugin(viewer, {
            canvasId: "NavCubeCanvas",
            // color: "lightblue",
            visible: true, // Initially visible (default)
            cameraFly: true, // Fly camera to each selected axis/diagonal
            cameraFitFOV: 45, // How much field-of-view the scene takes once camera has fitted it to view
            cameraFlyDuration: 0.5 // How long (in seconds) camera takes to fly to each new axis/diagonal
        });
        new AxisGizmoPlugin(viewer, {
            canvasId: "AxisGizmoCanvas"
        });
        window.viewer = viewer;
    },
};
</script>

<style scoped>
body {
    margin: 0;
    width: 100%;
    height: 100%;
    user-select: none;
}

#myCanvas {
    width: 100%;
    height: 100%;
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
</style>
