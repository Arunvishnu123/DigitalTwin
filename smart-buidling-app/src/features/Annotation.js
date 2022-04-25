import store from "../store/index"
import {
    AnnotationsPlugin
} from "@xeokit/xeokit-sdk/";

export function createAnnotation() {
    const annotations = new AnnotationsPlugin(store.state.viewer,{

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

    store.state.model.on("loaded", () => {
        annotations.createAnnotation({
            id: "Annotation1",
            worldPos:[1838784.159,16,-5156527.90],
            occludable: true,
            markerShown: true,
            labelShown: true,
            values: {
                glyph: "A2",
                title: "Kitchen bench",
                description: "This annotation becomes visible<br>whenever you can see its marker<br>through the window",
                markerBGColor: "blue"
            }
        });
    })
}