import { StoreyViewsPlugin}
    from "@xeokit/xeokit-sdk/";

export function floorView(objectID, viewer,model) {

    const storeyViewsPlugin = new StoreyViewsPlugin(viewer);

    model.on("loaded", () => {
        storeyViewsPlugin.showStoreyObjects(objectID, {
            hideOthers: true,
            useObjectStates: false
        });


    });
}