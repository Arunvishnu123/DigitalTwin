import store from "../../store/index"
import {
    AnnotationsPlugin
} from "@xeokit/xeokit-sdk/";
import "../../assets/styles/annotation.css"

export function createAnnotation() {
    const annotations = new AnnotationsPlugin(store.state.viewer, {

        markerHTML: "<div class='annotation-marker' style='background-color: {{markerBGColor}};'>{{glyph}}</div>",
        labelHTML: "<div class='annotation-label' style='background-color: {{labelBGColor}};'>\
            <div class='annotation-title'>{{title}}</div>\
            <div class='annotation-desc'>{{description}}</div>\
            </div>",

        values: {
            markerBGColor: "red",
            labelBGColor: "white",
            glyph: "X",
            title: "Untitled",
            description: "No description"
        }
    });
    annotations.on("markerClicked", (annotation) => {
        annotation.setLabelShown(!annotation.getLabelShown());
    });

    var prevAnnotationClicked = null;

    var i = 1;

    // store.state.viewer.scene.input.on("mouseclicked", (coords) => {

    //     const pickResult = store.state.viewer.scene.pick({
    //         canvasPos: coords,
    //         pickSurface: true  // <<------ This causes picking to find the intersection point on the entity
    //     });

    //     if (pickResult) {
    //         console.log(pickResult)
    //         const annotation = annotations.createAnnotation({
    //             id: "myAnnotation" + i,
    //             pickResult: pickResult, // <<------- initializes worldPos and entity from PickResult
    //             //occludable: true,       // Optional, default is true
    //             markerShown: true,      // Optional, default is true
    //             labelShown: true,       // Optional, default is true
    //             values: {               // HTML template values
    //                 glyph: "A" + i,
    //                 title: "My annotation " + i,
    //                 description: "My description " + i
    //             },
    //         });

    //         i++;
    //     }
    // });

    annotations.createAnnotation({
        id: "myAnnotation3",
        /////////////////////////////////////////  Entity
        worldPos: [1838785.5556059808,17.394586391943115,-5156526.983405757	],
        //occludable: true,
        markerShown: true,
        labelShown: false,

        labelHTML: "<div class='annotation-label' style='background-color: {{labelBGColor}};'>\
            <div class='annotation-title'>{{title}}</div>\
            <div class='annotation-desc'>{{description}}</div>\
            <br><img alt='myImage' width='150px' height='100px' src='{{imageSrc}}'>\
            </div>",

        values: {
            glyph: "A3",
            title: "The West wall",
            description: "Annotations can contain<br>custom HTML like this<br>image:",
            markerBGColor: "red",
            imageSrc: "https://xeokit.io/img/docs/BIMServerLoaderPlugin/schependomlaan.png"
        }
    });
}