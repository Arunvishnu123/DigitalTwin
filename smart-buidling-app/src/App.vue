<template>
<canvas id="myCanvas"></canvas>
<canvas id="mySectionPlanesOverviewCanvas"></canvas>
</template>

<script>
import {
    Viewer
} from "@xeokit/xeokit-sdk/";
import * as display3d from "./features/view3D"
import * as sectionview from "./features/sectionview"
export default {

    mounted() {
        const viewer = new Viewer({
            canvasId: "myCanvas",
        });
        display3d.display3d(viewer)
        sectionview.sectionview(viewer,"mySectionPlanesOverviewCanvas")
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

#mySectionPlanesOverviewCanvas {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 70px;
    right: 10px;
    z-index: 200000;
}
</style>
