<template>
<div>
    <div id="myAnno"></div>
    <div class="annotation-la" id="myAnnot" style="background-color: white">
        <div class="annotation-tit">Window Status - Closed</div>
        <w-tag v-model="tagOn"  class= "openWindow" :bg-color="tagOn ? 'red' : 'green'" dark lg>
            {{ tagOn ? "Click here to Open Window" : "Window Opened" }}
        </w-tag>
        <div class="annotation-de">click on the window for more information</div>
    </div>
</div>
</template>

<script>
import store from "../../store/index";
import {
    AnnotationsPlugin
} from "@xeokit/xeokit-sdk/";

export default {
    props: ["position"],
    components: {},

    data: () => ({
        tagOn: false,
    }),
    methods: {},
    mounted() {
        store.state.viewer.scene.ticksPerOcclusionTest = 1;
        const anno = new AnnotationsPlugin(store.state.viewer, {});

        // var prevAnnotationClicked = null;

        // annotations.on("markerClicked", (annotation) => {
        //     if (prevAnnotationClicked) {
        //         prevAnnotationClicked.setLabelShown(false);
        //     }
        //     annotation.setLabelShown(true);
        //     viewer.cameraFlight.flyTo(annotation);
        //     prevAnnotationClicked = annotation;
        // });
        // annotations.on("markerMouseEnter", (annotation) => {
        //     annotation.setLabelShown(true);
        // });

        anno.on("markerMouseLeave", (annotation) => {
            annotation.setLabelShown(false);
            console.log("djfhdfhsdfgghsdgfsdh", annotation);
        });
        store.state.viewer.cameraControl.on("hover", (pickResult) => {
            if (pickResult.entity.id == "1jMGJTzbX0Gu65H0cXPmD5") {
                console.log("teststetd");
                anno.createAnnotation({
                    id: "myAnn",
                    //entity: viewer.scene.objects["1bDMdL0k55X8oOMH5VK_cb"],
                    worldPos: [1838780.3832532489, 18.04636003861201, -5156533.031637598],
                    //occludable: true,
                    markerShown: true,
                    eye: [1838784.226, 17.41054783, -5156525.58],
                    look: [1838784.212, 17.40368311, -5156525.627],
                    up: [-0.040127462, 0.990154669, -0.134102643],
                    labelShown: true,
                    markerElementId: "myAnno",
                    labelElementId: "myAnnot",
                });
            } else {
                anno.destroy();
                console.log(anno.destroy());
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
    background-color: black;
    visibility: hidden;
    /* Set markers and labels initially hidden */
    box-shadow: 5px 5px 15px 1px #000000;
    z-index: 0;
    align-items: center;
    cursor: pointer;
}
.openWindow{
    width:100%;
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
