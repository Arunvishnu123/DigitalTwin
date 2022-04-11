import { SectionPlanesPlugin } from "@xeokit/xeokit-sdk/";

export function sectionview(viewer, id) {

    const sectionPlanes = new SectionPlanesPlugin(viewer, {
        overviewCanvasId: id,
        overviewVisible: true
    });
    sectionPlanes.createSectionPlane({
        id: "mySectionPlane",
        pos: [1.04, 1.95, 9.74],
        dir: [1.0, 0.0, 0.0]
    });

    sectionPlanes.createSectionPlane({
        id: "mySectionPlane2",
        pos: [2.30, 4.46, 14.93],
        dir: [0.0, -0.09, -0.79]
    });

}
