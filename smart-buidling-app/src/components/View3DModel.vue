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
    NavCubePlugin,
    AxisGizmoPlugin,ViewCullPlugin
} from "@xeokit/xeokit-sdk/";
import * as display3d from "../features/view3D";
import * as selectObjects from "../features/selectObjects"

export default {
     data: () => ({
        viewer:null,
    }),
    mounted() {
        this.viewer = new Viewer({
            canvasId: "myCanvas",
        });
        // const viewCullPlugin = new ViewCullPlugin(this.viewer , {
        //     maxTreeDepth: 20
        // });
          this.viewer.scene.edgeMaterial.edges = false;

        display3d.display3d(this.viewer );
        selectObjects.selectObects(this.viewer);

        new NavCubePlugin(this.viewer , {
            canvasId: "NavCubeCanvas",
            // color: "lightblue",
            visible: true,
            cameraFly: true,
            cameraFitFOV: 45,
            cameraFlyDuration: 0.5,
        });
        new AxisGizmoPlugin(this.viewer , {
            canvasId: "AxisGizmoCanvas",
        });
        window.viewer = this.viewer ;
    },

     methods: {
        view() {
            const eye = this.viewer.camera.eye
            const  look = this.viewer.camera.look
            const up = this.viewer.camera.up
            console.log("eye" , eye)
            console.log("look", look)
            console.log("up", up)
        }
    }
};
</script>

<style scoped>

#myCanvas {
    top: 0px;
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
    left: 1250px;
    top:545px;
    z-index: 200000;
}

#AxisGizmoCanvas {
    position: absolute;
    width: 250px;
    height: 250px;
    bottom: 100px;
    left: 30px;
    top:545px;
    z-index: 200000;
}
.test2{
    position: relative;
    top:-10px
}
</style>
