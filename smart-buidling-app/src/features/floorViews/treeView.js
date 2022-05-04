
import store from "../../store/index"

export function treeView(){
    const treeView = new TreeViewPlugin(viewer, {
        containerElement: document.getElementById("treeViewContainer"),
        autoExpandDepth: 1,
        hierarchy: "storeys",
        sortNodes: true,
        sortableStoreysTypes: ["IfcWall", "IfcWallStandardCase", "IfcSlab", "IfcFurniture", "IfcFurnishingElement", "IfcDoor", "IfcRoof"]
    });
}