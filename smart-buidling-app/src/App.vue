<template>
<div>
    <canvas id="myCanvas"></canvas>
    <div id="storeys"></div>
</div>
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
        display3d.display3d(viewer,"storeys")
        sectionview.sectionview(viewer, "sectionPlanesOverviewCanvas")
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
#storeys {
            position: absolute;
            left: 10px;
            top: 60px;
            margin-top: 20px;
            overflow-y: scroll;
            height: calc(100% - 120px);
            margin-bottom: 10px;
            width: 320px;
            pointer-events: all;
            opacity: 0.8;
        }
</style>
