<template>
<div>
    <canvas id="myCanvas"></canvas>
    <canvas id="NavCubeCanvas"></canvas>
    <canvas id="AxisGizmoCanvas"></canvas>
    <w-app>
        <w-transition-scale>
            <div class="transition-box" v-if="t">Scaling transition</div>
        </w-transition-scale>
    </w-app>

</div>
</template>

<script>
import {
    Viewer,
    Skybox,
    PerformanceModel,
    ImagePlane,
} from "@xeokit/xeokit-sdk/";
import * as DisplayPersonData from "../features/clickPerosonDetails"
import * as display3d from "../features/view3D";
import * as selectObjects from "../features/selectObjects";
import * as ContextMenuCanvas from "../features/contextMenu3DModel";
import * as ContextMenu3DModel from "../features/contextMenuObject";
import store from "../store/index";
import * as FloorView from "../features/floorView";
import * as NavCube from "../features/navCube";
import * as AxisView from "../features/axisView";
import * as ContextMenuParameters from "../features/contextMenuParameters";
import * as CreateAnnotation from "../features/Annotation";
import * as CreateKeyMap from "../features/keyMap"
import * as ClickSensor from "../features/click"
import * as ObjectLoader from "../features/objectLoader"
import * as windowClickEvent from "../features/windowOpenCloseDialog"
import * as ReadMqtt from "../features/mqtt"

export default {
    data: () => ({
        viewer: null,
        model: null,
        t: false
    }),
    mounted() {
        store.state.viewer = new Viewer({
            canvasId: "myCanvas",
            transparent: true,
            saoEnabled: true,
        });
        console.log("test", store.state.viewer)

        const performanceModel = new PerformanceModel(store.state.viewer.scene, {
            id: "model",
            isModel: true, // <--------------------- Represents a model, registers PerformanceModel by ID on viewer.scene.models
            rotation: [0, 0, 0],
        });

        const cameraControl = store.state.viewer.cameraControl;
        const scene = store.state.viewer.scene;

        const camera = scene.camera;
        store.state.viewer.scene.edgeMaterial.edges = false;
       // ObjectLoader.objectLoader()
        const cameraFlight = store.state.viewer.cameraFlight;
        const sao = scene.sao;
        const saoParams = new(function () {
            this.enabled = sao.enabled;
            this.kernelRadius = sao.kernelRadius;
            this.intensity = sao.intensity;
            this.bias = sao.bias;
            this.scale = sao.scale;
            this.minResolution = sao.minResolution;
            this.numSamples = sao.numSamples;
            this.blendFactor = sao.blendFactor;
            this.blendCutoff = sao.blendCutoff;
            this.blur = sao.blur;
            this.perspective = camera.projection === "perspective";
            this.far = camera.perspective.far;
            this.fov = camera.perspective.fov;
        })();

        const update = function () {
            sao.enabled = saoParams.enabled;
            sao.kernelRadius = saoParams.kernelRadius;
            sao.intensity = saoParams.intensity;
            sao.bias = saoParams.bias;
            sao.scale = saoParams.scale;
            sao.minResolution = saoParams.minResolution;
            sao.numSamples = saoParams.numSamples;
            sao.blendFactor = saoParams.blendFactor;
            sao.blendCutoff = saoParams.blendCutoff;
            sao.blur = saoParams.blur;
            camera.projection = saoParams.perspective ? "perspective" : "ortho";
            camera.perspective.far = saoParams.far;
            camera.ortho.far = saoParams.far;
            camera.perspective.fov = saoParams.fov;
            requestAnimationFrame(update);
        };

        update();

        sao.enabled = true; // Enable SAO - only works if supported (see above)
        sao.intensity = 10;
        sao.bias = 10;
        sao.scale = 10.0;
        sao.minResolution = 0.0;
        sao.numSamples = 10;
        sao.kernelRadius = 1000;
        sao.blendCutoff = 1;
        sao.blendFactor = 0.9;

        cameraControl.followPointer = true;
        camera.perspective.near = 0.1;
        camera.perspective.far = 5000.0;

        camera.ortho.near = 0.1;
        camera.ortho.far = 1000.0;

        camera.projection = "perspective";
       

        scene.highlightMaterial.fill = true;
        scene.highlightMaterial.fillAlpha = 0.3;
        scene.highlightMaterial.edgeColor = [1, 1, 0];
        store.state.viewer.scene.sao.enabled = true;
        // new AmbientLight(store.state.viewer.scene, {
        //     color: [0.9, 0.9, 0.9],
        //     intensity: 0.2,
        // });
        // new DirLight(store.state.viewer.scene, {
        //     dir: [0.8, -0.5, -0.5],
        //     color: [0.67, 0.67, 1.0],
        //     intensity: 0.2,
        //     space: "world",
        // });
        // new DirLight(store.state.viewer.scene, {
        //     dir: [-0.8, -1.0, 0.5],
        //     color: [1, 1, 0.9],
        //     intensity: 0.2,
        //     space: "world",
        // });
        ReadMqtt.readMQTT()
        const skybox = new Skybox(store.state.viewer.scene, {
            src: "src/assets/cloudySkyBox.jpg",
            size: 1000,
        });
        // find the corodinates
        // store.state.viewer.cameraControl("hover", (coords) => {
        //     console.log("corodinates", coords);
        //     const pickResult = store.state.viewer.scene.pick({
        //         canvasPos: coords,
        //         pickSurface: true, // <<------ This causes picking to find the intersection point on the entity
        //     });
        //     if (pickResult) {
        //         console.log("pickresult", pickResult);
        //         if (pickResult.entity.id == "1bDMdL0k55X8oOMH5VK_cb") {
        //             console.log("id clicked");
        //         } else {
        //             console.log("notclcickedd")
        //         }
        //     }
        // });

        store.state.viewer.scene.input.on("picked", (e) => {
            const entity = e.entity;
            const canvasPos = e.canvasPos;
            const worldPos = e.worldPos; // 3D World-space position
            const viewPos = e.viewPos; // 3D View-space position
            const worldNormal = e.worldNormal; // 3D World-space normal vector
            console.log(e)
        });

        // store.state.viewer.cameraControl.on("hover", (pickResult) => {
        //     if (pickResult.entity.id == "1bDMdL0k55X8oOMH5VK_cb") {
        //         this.t = true
        //         console.log(this.t)
        //         console.log("id clicked");
        //     } else {
        //         this.t = false
        //         console.log(this.t)
        //         console.log("notclcickedd")
        //     }
        // })

      ///  CreateAnnotation.createAnnotation()
        ClickSensor.clickSensorData("1bDMdL0k55X8oOMH5VK_cb")
        windowClickEvent.clickPersonData()

        DisplayPersonData.clickPersonData()
        CreateKeyMap.keyMap()
        new ImagePlane(store.state.viewer.scene, {
            src: "src/assets/1.jpg",
            size: 3000,
            position: [1838775.8837769788, -60.25278768461993, -5156526.636644002],
            rotation: [0, 0, 0], // X, Y and Z
            opacity: 1.0,
            collidable: false,
            gridVisible: false,
            pickable: true,
        });

        ContextMenuCanvas.contextMenu3dModel(store.state.viewer);
        // display 3d model
        store.state.model = display3d.display3d(store.state.viewer);
        selectObjects.selectObects(store.state.viewer);
        if (store.state.contextMenuSelection == false) {
            ContextMenu3DModel.contextMenu3dModel(
                store.state.model,
                store.state.viewer
            );
        } else {
            ContextMenuParameters.contextMenufirstFloor(store.state.viewer);
            //ContextMenu3DModel.contextMenu3dModel(this.model, store.state.viewer);
        }

        // NavCuve visualization
        NavCube.navCubeView("NavCubeCanvas", store.state.viewer);
        // Axis visualization
        AxisView.viewAxis("AxisGizmoCanvas", store.state.viewer);
        //FloorView.floorView("3_b98WEDT7feUaJ_WJeWog", this.viewer,this.model);
        window.viewer = store.state.viewer;

         console.log("model",store.state.model.scene.objects)
    },

    methods: {
        view() {
            const eye = store.state.viewer.camera.eye;
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

.transition-toggle {
    margin: 12px 24px 12px 0;
    width: 7.7em;
}

.transition-box {
    background-color: #eee;
    border: 1px solid #ddd;
    border-radius: 3px;
    padding: 1em;
    width: 14em;
    text-align: center;
}

@media screen and (min-width: 800px) {
    #NavCubeCanvas {
        position: absolute;
        width: 250px;
        height: 250px;
        bottom: 100px;
        left: 1310px;
        top: 445px;
        z-index: 200000;
    }

    #AxisGizmoCanvas {
        position: absolute;
        width: 250px;
        height: 250px;
        bottom: 100px;
        left: 30px;
        top: 445px;
        z-index: 200000;
    }
}
</style>
