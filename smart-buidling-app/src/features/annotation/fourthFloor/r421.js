import {AnnotationsPlugin } from "@xeokit/xeokit-sdk";
import "../../assets/styles/annotation.css"


export function annotation(){
    const annotations = new AnnotationsPlugin(viewer, {

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
}