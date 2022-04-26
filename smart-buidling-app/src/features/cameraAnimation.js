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
                1838738.5290765269, 21.20976049878403, -5156490.9168121675
            ],
            "look": [
                1838758.8951321803, 16.501684955901034, -5156504.959348367
            ],
            "up": [
                0.15391989267645648, 0.9823672113893178, -0.10612883032259861
            ]
        },

        {
            t: 2,
            "eye": [
                1838757.3375947007, 24.355400368251654, -5156561.132067046
            ],
            "look": [
                1838782.255334538, 17.473155339749738, -5156534.925380357
            ],
            "up": [
                0.12882785169279748, 0.9823672113906944, 0.13549186917556835
            ]
        },
        {
            t: 3,
            "eye": [
                1838831.5685177208, 18.36568653028283, -5156553.648102304
            ],
            "look": [
                1838803.1619314884, 13.93106005969587, -5156531.538640526
            ],
            "up": [
                -0.0964894425554531, 0.9924967525528229, 0.07509982454998589
            ]
        },
        
        {
            t: 4,
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
            t: 5,
            "eye": [
                1838787.4421306136, 2.9807394271300933, -5156505.816099132
            ],
            "look": [
                1838783.941890359, 3.3255623139271067, -5156510.86978706
            ],
            "up": [
                0.03188734217413631, 0.9984305577024861, 0.04603931857632314
            ]
        },
        {
            t: 6,
            "eye": [
                1838782.1071327217, 1.973507329778077, -5156512.891041257   
            ],
            "look": [
                1838778.9972338777, 2.2798761055023467, -5156517.381149249
            ],
            "up": [
                0.03188734217413631, 0.9984305577024861, 0.04603931857632314
            ]
        },

        {
            t: 7,
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
        playingRate: 0.05
    });

    setTimeout(function () {
        cameraPathAnimation.play(0);
    }, 1000);
}