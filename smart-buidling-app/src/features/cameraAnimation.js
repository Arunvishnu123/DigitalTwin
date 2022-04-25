import { CameraPath, CameraPathAnimation } from "@xeokit/xeokit-sdk";
import store from "../store/index"

export function cameraPathAnimation() {

    const positions = [
        {
            t: 0,
            "eye": [
                1838806.1036860247, 9.44347287346586, -5156481.191867573
            ],
            "look": [
                1838784.2194265071, 11.599380180651577, -5156512.788618103
            ],
            "up": [
                0.03188734217413631, 0.9984305577024861, 0.04603931857632314
            ]
        },

        {
            t: 1,
            "eye": [
                1838638.09141941, 16.63892062799461, -5156415.647451761
            ],
            "look": [
                1838743.3832992106, -2.855939872361038, -5156468.065794597
            ],
            "up": [
                0.14637950457008364, 0.9865406817877824, -0.07287334093833114
            ]
        },

        {
            t: 2,
            "eye": [
                1838806.1036860247, 9.44347287346586, -5156481.191867573
            ],
            "look": [
                1838784.2194265071, 11.599380180651577, -5156512.788618103
            ],
            "up": [
                0.03188734217413631, 0.9984305577024861, 0.04603931857632314
            ]
        },

    ]
    var cameraPath = new CameraPath(store.state.viewer.scene, {
        frames: positions
    });

    cameraPath.smoothFrameTimes(1);

    var cameraPathAnimation = new CameraPathAnimation(store.state.viewer.scene, {
        cameraPath: cameraPath,
        playingRate: 0.015
    });

    setTimeout(function () {
        cameraPathAnimation.play(0);
    }, 1000);
}