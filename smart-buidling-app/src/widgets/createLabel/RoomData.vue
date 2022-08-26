<template>
<div>
    <div @click="m()" class="annotation-marker" id="my">412</div>
    <div class="annotation-la" id="myA" style="background-color: white">
        <div class="annotation-tit">Room Number - 421</div>
        <div class="annotation-tit">Maximum Capacatity - 48</div>
        <w-button class="annotation-de ma1" bg-color="primary" color="white" xs>click here</w-button>

    </div>
</div>
</template>

<script>
import store from "../../store/index";
import {
    AnnotationsPlugin
} from "@xeokit/xeokit-sdk/";
import * as FloorView from "../../features/floorViews/floorView"

export default {
    props: ["position"],
    components: {},

    data: () => ({
        tagOn: false,
    }),
    methods: {
        m() {

            FloorView.floorView("3_b98WEDT7feUaJ_WJeW$i", store.state.viewer, store.state.model);
        }
    },
    mounted() {
        store.state.viewer.scene.ticksPerOcclusionTest = 1;
        const anno = new AnnotationsPlugin(store.state.viewer, {});

        var prevAnnotationClicked = null;

        anno.on("markerClicked", (annotation) => {
            if (prevAnnotationClicked) {
                prevAnnotationClicked.setLabelShown(false);
            }
            annotation.setLabelShown(true);
            viewer.cameraFlight.flyTo(annotation);
            prevAnnotationClicked = annotation;
        });
        anno.on("markerMouseEnter", (annotation) => {
            annotation.setLabelShown(true);
        });

        anno.on("markerMouseLeave", (annotation) => {
            annotation.setLabelShown(false);
            console.log("djfhdfhsdfgghsdgfsdh", annotation);
        });

        console.log("teststetd");
        anno.createAnnotation({
            id: "myAnn",
            //entity: viewer.scene.objects["1bDMdL0k55X8oOMH5VK_cb"],
            worldPos: [1838785.0782395182, 17.683018689996043, -5156526.122360405],
            occludable: true,
            markerShown: true,
            eye: [1838784.226, 17.41054783, -5156525.58],
            look: [1838784.212, 17.40368311, -5156525.627],
            up: [-0.040127462, 0.990154669, -0.134102643],
            labelShown: false,
            markerElementId: "my",
            labelElementId: "myA",

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
    width: 30px;
    height: 30px;
    border-radius: 50%;
    border: 2px solid #ffffff;
    background-color: black;
    visibility: hidden;
    /* Set markers and labels initially hidden */
    box-shadow: 5px 5px 15px 1px #000000;
    z-index: 0;
    align-items: center;
    cursor: pointer;
     vertical-align: middle;
}

.openWindow {
    width: 100%;
}

.avatar {
    /* This image is 687 wide by 1024 tall, similar to your aspect ratio */

    /* make a square container */
    width: 150px;
    height: 150px;

    /* fill the container, preserving aspect ratio, and cropping to fit */
    background-size: cover;

    /* center the image vertically and horizontally */
    background-position: top center;

    /* round the edges to a circle with border radius 1/2 container size */
    border-radius: 50%;
    align-items: center;
}

.annotation-la {
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
    align-items: center;
    /* Set markers and labels initially hidden */
}

.annotation-la:after {
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
    align-items: center;
}

.annotation-la:before {
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
    align-items: center;
}

.annotation-tit {
    font: normal 18px arial, serif;
    margin-bottom: 8px;
    align-items: center;
    text-align: center;
}

.annotation-de {
    font: normal 10px arial, serif;
    text-align: center;
}
</style>
