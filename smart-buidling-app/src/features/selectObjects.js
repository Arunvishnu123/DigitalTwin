export function selectObects(viewer) {
    var lastEntity = null;
    var lastColorize = null;

    viewer.cameraControl.on("picked", (pickResult) => {

        console.log(pickResult.entity.id);

        if (!lastEntity || pickResult.entity.id !== lastEntity.id) {

            if (lastEntity) {
                lastEntity.colorize = lastColorize;
            }

            lastEntity = pickResult.entity;
        

            pickResult.entity.colorize = [0,0,0];
        }
    });

    viewer.cameraControl.on("pickedNothing", (e) => {

        if (lastEntity) {
            lastEntity.colorize = lastColorize;
        }

        lastEntity = null;
        lastColorize = null;
    });

}