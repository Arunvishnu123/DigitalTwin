import {
    XKTLoaderPlugin,math
} from "@xeokit/xeokit-sdk/";

export function display3d(viewer) {
    viewer.camera.eye = [1838806.1036860247, 9.44347287346586, -5156481.191867573];
    viewer.camera.look = [1838784.2194265071, 11.599380180651577, -5156512.788618103];
    viewer.camera.up = [0.03188734217413631, 0.9984305577024861, 0.04603931857632314];
    const xktLoader = new XKTLoaderPlugin(viewer, {
        objectDefaults: { // <<----- Only override color of IfcSpace elements, keep other original IFC colors
            IfcSpace: {

            },
            IfcWindow: {
                pickable: false,
                opacity: 0.1
            },
            IfcSlab: {
                colorize: [0.337255, 0.303922, 0.870588], // Blue
                opacity: 0.3
            },
        }
    });
    const model = xktLoader.load({
        id: "myModel",
        src: 'src/assets/MINES.xkt',
        saoEnabled: true,
        metaModelSrc: "src/assets/final.json",
        orgin:[0,0,0],
        excludeTypes: ["IfcSpace"],
        objectDefaults: {
            IfcSlab: {
                colorize: [150, 146, 146], // Blue
                pickable: true,
            },
        },
    });
    viewer.cameraControl.followPointer = true;
    viewer.scene.highlightMaterial.fill = false;
    viewer.scene.highlightMaterial.fillAlpha = 0.3;
    viewer.scene.highlightMaterial.edgeColor = [1, 1, 1];
    function projectLongLatToMercator(longitude, latitude, altitude = 0) {

        const EARTH_RADIUS = 6371008.8; // Meters
        const EARTH_CIRCUMFERENCE = 2 * Math.PI * EARTH_RADIUS; // Meters

        function mercatorXfromLng(longitude) {
            return (180 + longitude) / 360;
        }

        function mercatorYfromLat(latitude) {
            return (180 - (180 / Math.PI * Math.log(Math.tan(Math.PI / 4
                + latitude * Math.PI / 360)))) / 360;
        }

        function mercatorZfromAltitude(altitude, latitude) {
            return altitude / circumferenceAtLatitude(latitude);
        }

        function circumferenceAtLatitude(latitude) {
            return EARTH_CIRCUMFERENCE * Math.cos(latitude * Math.PI / 180);
        }

        function mercatorScaleAtLatitude(latitude) {
            return 1 / Math.cos(latitude * Math.PI / 180);
        }

        function latFromMercatorY(y) {
            const y2 = 180 - y * 360;
            return 360 / Math.PI * Math.atan(Math.exp(y2 * Math.PI / 180)) - 90;
        }

        // Returns the distance of 1 meter in Mercator coordinate units at the given latitude.
        function meterInMercatorCoordinateUnits(y) {
            return 1 / EARTH_CIRCUMFERENCE * mercatorScaleAtLatitude(latFromMercatorY(y));
        }

        const mercator = math.vec3([
            mercatorXfromLng(longitude),
            mercatorYfromLat(latitude),
            mercatorZfromAltitude(altitude, latitude)
        ]);

        const modelMercatorScale = meterInMercatorCoordinateUnits(mercator[1]);

        math.mulVec3Scalar(mercator, 1 / modelMercatorScale);
console.log("testmercator",mercator)
        return mercator;
    }
    return model
}