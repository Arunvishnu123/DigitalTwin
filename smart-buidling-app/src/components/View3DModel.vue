<template>
<div>
    <router-link to="/" ><canvas id="myCanvas"></canvas></router-link>
</div>
</template>

<script>
import {
    Viewer
} from "@xeokit/xeokit-sdk/";
import * as display3d from "../features/view3D"

export default {

    mounted() {
        const viewer = new Viewer({
            canvasId: "myCanvas",
        });
        display3d.display3d(viewer)
        
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


</style>
