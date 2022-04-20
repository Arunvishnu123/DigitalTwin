<template>
  <div>
    <canvas id="myCanvas"></canvas>
    <canvas id="NavCubeCanvas"></canvas>
    <canvas id="AxisGizmoCanvas"></canvas>
  </div>
</template>

<script>
import { Viewer } from "@xeokit/xeokit-sdk/";
import * as display3d from "../features/view3D";
import * as selectObjects from "../features/selectObjects";
import * as ContextMenuCanvas from "../features/contextMenu3DModel";
import * as ContextMenu3DModel from "../features/contextMenuObject";
import store from "../store/index";
import * as FloorView from "../features/floorView";
import * as NavCube from "../features/navCube";
import * as AxisView from "../features/axisView";

export default {
  data: () => ({
    viewer: null,
    model:null
  }),
  mounted() {
    this.viewer = new Viewer({
      canvasId: "myCanvas",
    });

    store.state.viewer = this.viewer;

    this.viewer.scene.edgeMaterial.edges = false;
    ContextMenuCanvas.contextMenu3dModel(this.viewer);
    // display 3d model
     this.model = display3d.display3d(this.viewer);
    selectObjects.selectObects(this.viewer);
    ContextMenu3DModel.contextMenu3dModel(this.model, this.viewer);

    // NavCuve visualization
    NavCube.navCubeView("NavCubeCanvas", this.viewer);
    // Axis visualization
    AxisView.viewAxis("AxisGizmoCanvas", this.viewer);
    //FloorView.floorView("3_b98WEDT7feUaJ_WJeWog", this.viewer,this.     model);
    window.viewer = this.viewer;
  },

  methods: {
    view() {
      const eye = this.viewer.camera.eye;
      const look = this.viewer.camera.look;
      const up = this.viewer.camera.up;
      console.log("eye", eye);
      console.log("look", look);
      console.log("up", up);
    },
  },
};
</script>

<style scoped>
#myCanvas {
  top: 0px;
  width: 100%;
  height: 100%;
  position: absolute;
  background: rgb(0, 5, 7);
  background-image: linear-gradient(lightblue, rgb(56, 54, 54));
}

#NavCubeCanvas {
  position: absolute;
  width: 250px;
  height: 250px;
  bottom: 100px;
  left: 1450px;
  top: 645px;
  z-index: 200000;
}

#AxisGizmoCanvas {
  position: absolute;
  width: 250px;
  height: 250px;
  bottom: 100px;
  left: 30px;
  top: 645px;
  z-index: 200000;
}
</style>
