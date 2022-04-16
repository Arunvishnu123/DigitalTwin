<template>
<div>
    <canvas id="Canvas8"> </canvas>
</div>
</template>

<script>
import * as floorView from "../features/floorView";
import {
    Viewer
} from "@xeokit/xeokit-sdk/";
export default {
    mounted() {
        const viewer = new Viewer({
            canvasId: "Canvas8",
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
        floorView.floorView("3_b98WEDT7feUaJ_WJe2lo", viewer);
        viewer.scene.edgeMaterial.edges = false;
        // viewer.scene.on("tick", function () {
        //     viewer.scene.camera.orbitYaw(0.3);
        // });
    },
};
</script>

<style scoped>
#Canvas8 {
    top: 27px;
    height: 300px;
    position: absolute;
    background: lightblue;
    background-image: linear-gradient(lightblue, white);
}
</style>
