<template>
  <div>
    <canvas id="myCanvas"></canvas>
    <canvas id="NavCubeCanvas"></canvas>
    <canvas id="AxisGizmoCanvas"></canvas>
  </div>
</template>

<script>
import { Viewer , DirLight,} from "@xeokit/xeokit-sdk/";
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
    store.state.viewer = new Viewer({
      canvasId: "myCanvas",
    });


 

    store.state.viewer.scene.edgeMaterial.edges = false;
    ContextMenuCanvas.contextMenu3dModel(store.state.viewer);
    // display 3d model
     store.state.model = display3d.display3d(store.state.viewer);
    selectObjects.selectObects(store.state.viewer);
    ContextMenu3DModel.contextMenu3dModel(this.model, store.state.viewer);

    // NavCuve visualization
    NavCube.navCubeView("NavCubeCanvas", store.state.viewer);
    // Axis visualization
    AxisView.viewAxis("AxisGizmoCanvas", store.state.viewer);
    //FloorView.floorView("3_b98WEDT7feUaJ_WJeWog", this.viewer,this.model);
    window.viewer = store.state.viewer;
  },

  methods: {
    view() {
      const eye = store.state.viewer.camera.eye;
     // const look = this.viewer.camera.look;
      //const up = this.viewer.camera.up;
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
