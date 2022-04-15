<template>
<div>
    <canvas id="Canvas1"> </canvas>
        <button @click="view()" class="test2"> Arun  </button>
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
            canvasId: "Canvas1",
        });
        viewer.camera.eye = [1838806.1036860247, 9.44347287346586, -5156481.191867573];
        viewer.camera.look = [1838784.2194265071, 11.599380180651577, -5156512.788618103];
        viewer.camera.up = [0.03188734217413631, 0.9984305577024861, 0.04603931857632314];

        floorView.floorView("3_b98WEDT7feUaJ_WJeWog", viewer);
        viewer.scene.on("tick", function () {
            viewer.scene.camera.orbitYaw(0.3);
        });
viewer.scene.edgeMaterial.edges = false;
 viewer.scene.on("tick", function () {
            viewer.scene.camera.orbitYaw(0.3);
        });
    },

};
</script>

<style scoped>
#Canvas1 {
    top: 27px;
    height: 300px;
    background: lightblue;
    background-image: linear-gradient(lightblue, white);
}
.test2{
    position: relative;
    top:-10px
}
</style>
