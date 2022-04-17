export function selectObects(viewer) {
    var lastEntity = null;
    viewer.scene.highlightMaterial.edgeColor = [1, 1, 0];
    viewer.scene.highlightMaterial.fill = true;
    viewer.scene.highlightMaterial.edges = true;
    viewer.scene.input.on("mousemove", function (coords) {

        var hit = viewer.scene.pick({
            canvasPos: coords
        });

        if (hit) {

            if (!lastEntity || hit.entity.id !== lastEntity.id) {

                if (lastEntity) {
                    lastEntity.highlighted = false;
                }

                lastEntity = hit.entity;
                hit.entity.highlighted = true;
            }
        } else {

            if (lastEntity) {
                lastEntity.highlighted = false;
                lastEntity = null;
            }
        }
    });
}