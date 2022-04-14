import {
    
    XKTLoaderPlugin
} from "@xeokit/xeokit-sdk/";

export function display3d(viewer) {
   

    viewer.camera.eye = [-3.933, 2.855, 27.018];
    viewer.camera.look = [4.4, 3.724, 8.899];
    viewer.camera.up = [-0.018, 0.999, 0.039];

    const xktLoader = new XKTLoaderPlugin(viewer);

    const model = xktLoader.load({
        id: "myModel",
        src: 'src/assets/MINES.xkt',
        edges: true,
        backfaces: true
    });

    viewer.cameraControl.followPointer = true;
    viewer.scene.highlightMaterial.fill = false;
    viewer.scene.highlightMaterial.fillAlpha = 0.3;
    viewer.scene.highlightMaterial.edgeColor = [1, 1, 0];
    
 

    
   
}