export function selectObects(viewer) {
    var lastEntity = null;
    var lastColorize = null;

    viewer.cameraControl.on("hover", (pickResult) => {

        console.log(pickResult.entity.id);

        if (!lastEntity || pickResult.entity.id !== lastEntity.id) {

            if (lastEntity) {
                lastEntity.colorize = lastColorize;
            }

            lastEntity = pickResult.entity;
        

            pickResult.entity.colorize = [0, 1.0, 1.0];
        }
    });

    viewer.cameraControl.on("hoverOff", (e) => {

        if (lastEntity) {
            lastEntity.colorize = lastColorize;
        }

        lastEntity = null;
        lastColorize = null;
    });

}