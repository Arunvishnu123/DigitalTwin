<template>
<div>
    <canvas id="myCanvas"></canvas>
    <canvas id="NavCubeCanvas"></canvas>
    <canvas id="AxisGizmoCanvas"></canvas>
      <router-link to="/gg">gg</router-link>
</div>
</template>

<script>
import {
    Viewer,
    NavCubePlugin,
    AxisGizmoPlugin
} from "@xeokit/xeokit-sdk/";
import * as display3d from "../features/view3D";

export default {
    mounted() {
        const viewer = new Viewer({
            canvasId: "myCanvas",
        });
        display3d.display3d(viewer);

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
