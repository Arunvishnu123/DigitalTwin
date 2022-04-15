import { StoreyViewsPlugin, XKTLoaderPlugin }
    from "@xeokit/xeokit-sdk/";

export function floorView(objectID, viewer) {

    viewer.camera.eye = [-2.56, 8.38, 8.27];
    viewer.camera.look = [13.44, 3.31, -14.83];
    viewer.camera.up = [0.10, 0.98, -0.14];
    viewer.camera.orbitPitch(20);
    const xktLoader = new XKTLoaderPlugin(viewer);
    const model = xktLoader.load({
        id: "myModel",
        src: "src/assets/MINES.xkt",
        metaModelSrc: "src/assets/final.json",
        edges: true
    });
    const eye = viewer.camera.eye 
    console.log(eye)
    const storeyViewsPlugin = new StoreyViewsPlugin(viewer);

    model.on("loaded", () => {

        setTimeout(() => {

            storeyViewsPlugin.showStoreyObjects(objectID, {
                hideOthers: true,
                useObjectStates: false
            });

        }, 1000);
    });
}