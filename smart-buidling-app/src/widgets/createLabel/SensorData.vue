<template>
<div>
    <div @click="m()" id="myAnnotation5Marker"></div>
    <div class="annotation-label" id="myAnnotation5Label" style="background-color: white">
        <div class="annotation-title">
            Temperature - {{ $store.state.readTemperature }} °C
        </div>
        <div class="annotation-title">Luminance - 20 C</div>
        <div class="annotation-title">Relative Humidity - 20 %</div>
        <div class="annotation-desc">
            click on the sensor box for more information
        </div>
    </div>
</div>
</template>

<script>
import store from "../../store/index";
import * as floorView from "../../features/floorViews/floorView";
import {
    AnnotationsPlugin
} from "@xeokit/xeokit-sdk/";

export default {
    props: ["position"],
    components: {},
    methods: {
        m() {
            console.log("work");
            floorView.floorView(
                "3_b98WEDT7feUaJ_WJeW$i",
                store.state.viewer,
                store.state.model
            );
        },
    },
    mounted() {
        store.state.viewer.scene.ticksPerOcclusionTest = 1;
        const annotations = new AnnotationsPlugin(store.state.viewer, {});

        var prevAnnotationClicked = null;

        annotations.on("markerClicked", (annotation) => {
            if (prevAnnotationClicked) {
                prevAnnotationClicked.setLabelShown(false);
            }
            annotation.setLabelShown(true);
            viewer.cameraFlight.flyTo(annotation);
            prevAnnotationClicked = annotation;
        });
        annotations.on("markerMouseEnter", (annotation) => {
            annotation.setLabelShown(true);
        });

        annotations.on("markerMouseLeave", (annotation) => {
            annotation.setLabelShown(false);
            console.log("djfhdfhsdfgghsdgfsdh", annotation);
        });
        store.state.viewer.cameraControl.on("hover", (pickResult) => {
            if (pickResult.entity.id == "1bDMdL0k55X8oOMH5VK_cb") {
                console.log("sdhkfjdfhsdhf  ", t);
                const t = annotations.createAnnotation({
                    id: "myAnnotation5",
                    //entity: viewer.scene.objects["1bDMdL0k55X8oOMH5VK_cb"],
                    worldPos: this.position,
                    //occludable: true,
                    markerShown: true,
                    eye: [1838784.226, 17.41054783, -5156525.58],
                    look: [1838784.212, 17.40368311, -5156525.627],
                    up: [-0.040127462, 0.990154669, -0.134102643],
                    labelShown: true,
                    markerElementId: "myAnnotation5Marker",
                    labelElementId: "myAnnotation5Label",
                });
            } else {
                annotations.destroy();
                console.log("annotations      ", annotations);
                console.log("jkdfhsdhfjsdfh");
            }
        });
    },
};
</script>

<style scoped>
.annotation-marker {
    color: white;
    line-height: 1;
    text-align: center;
    font-family: "Arial";
    position: absolute;
    width: 25px;
    height: 25px;
    border-radius: 15px;
    border: 2px solid #ffffff;
    background-color: rgb(228, 228, 228);
    visibility: hidden;
    /* Set markers and labels initially hidden */
    box-shadow: 5px 5px 15px 1px #000000;
    z-index: 0;
    align-items: center;
    cursor: pointer;
}

.annotation-label {
    position: absolute;
    max-width: 250px;
    min-height: 50px;
    padding: 8px;
    padding-left: 30px;
    padding-right: 12px;
    background: #ffffff;
    color: #000000;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 8px;
    border: #ffffff solid 2px;
    box-shadow: 5px 5px 15px 1px #000000;
    z-index: 90000;
    visibility: hidden;
    /* Set markers and labels initially hidden */
}

.annotation-label:after {
    content: "";
    position: absolute;
    border-style: solid;
    border-width: 8px 12px 8px 0;
    border-color: transparent white;
    display: block;
    width: 0;
    z-index: 1;
    margin-top: -11px;
    left: -1px;
    top: 20px;
}

.annotation-label:before {
    content: "";
    position: absolute;
    border-style: solid;
    border-width: 9px 13px 9px 0;
    border-color: transparent #ffffff;
    display: block;
    width: 0;
    z-index: 0;
    margin-top: -12px;
    left: -15px;
    top: 20px;
}

.annotation-title {
    font: normal 18px arial, serif;
    margin-bottom: 8px;
}

.annotation-desc {
    font: normal 10px arial, serif;
    text-align: center;
}
</style>
