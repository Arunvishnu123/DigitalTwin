import {OBJLoaderPlugin} from "@xeokit/xeokit-sdk"
import store from "../../store/index"

export function objectLoader(){
    const objLoader = new OBJLoaderPlugin(store.state.viewer);

    const modelObj = objLoader.load({
        id: "objectModel",
        src: "src/assets/objects/test.obj",
        edges: true,
        position:[1838784.159,16,-5156527.90],
        scale: [0.05, 0.05, 0.05],
    });

}