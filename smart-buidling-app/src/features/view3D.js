import {
    XKTLoaderPlugin
} from "@xeokit/xeokit-sdk/";

export function display3d(viewer) {
    viewer.camera.eye = [1838806.1036860247, 9.44347287346586, -5156481.191867573];
    viewer.camera.look = [1838784.2194265071, 11.599380180651577, -5156512.788618103];
    viewer.camera.up = [0.03188734217413631, 0.9984305577024861, 0.04603931857632314];
    const xktLoader = new XKTLoaderPlugin(viewer, {

        objectDefaults: { // <<----- Only override color of IfcSpace elements, keep other original IFC colors

            IfcSpace: {

            },

            IfcWindow: {
                pickable: false,
                opacity: 0.1
            },
            IfcSlab: {
                colorize: [0.337255, 0.303922, 0.870588], // Blue
                opacity: 0.3
            },
        }
    });
    const model = xktLoader.load({
        id: "myModel",
        src: 'src/assets/MINES.xkt',
        saoEnabled: true,
        metaModelSrc: "src/assets/final.json",
        excludeTypes: ["IfcSpace"],
        objectDefaults: {
            IfcSlab: {
                colorize: [150, 146, 146], // Blue
            },
    
        },
    });
viewer.cameraControl.followPointer = true;
viewer.scene.highlightMaterial.fill = false;
viewer.scene.highlightMaterial.fillAlpha = 0.3;
viewer.scene.highlightMaterial.edgeColor = [1, 1, 1];

return model 
}