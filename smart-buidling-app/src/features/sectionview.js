import { StoreyViewsPlugin, math } from "@xeokit/xeokit-sdk/";

export function sectionview(viewer, id) {

    viewer.scene.highlightMaterial.edgeColor = [1, 1, 0];
    const storeyViewsPlugin = new StoreyViewsPlugin(viewer);

    window.viewer = viewer;
}
