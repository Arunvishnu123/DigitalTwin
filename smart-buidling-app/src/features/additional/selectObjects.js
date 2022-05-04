export function selectObects(viewer) {
    var lastEntity = null;

    viewer.scene.input.on("picked", function (coords) {

        var hit = viewer.scene.pick({
            canvasPos: coords
        });

        if (hit) {

            if (!lastEntity || hit.entity.id !== lastEntity.id) {

                if (lastEntity) {
                    lastEntity.selected = false;
                }

                lastEntity = hit.entity;
                hit.entity.selected = true;
            }
        } else {

            if (lastEntity) {
                lastEntity.selected = false;
                lastEntity = null;
            }
        }
    });
}