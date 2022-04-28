import {OBJLoaderPlugin} from "@xeokit/xeokit-sdk"
import store from "../store/index"

export function objectLoader(){
    const objLoader = new OBJLoaderPlugin(store.state.viewer);

    const modelObj = objLoader.load({
        id: "objectModel",
        src: "src/assets/test.obj",
        edges: true,
      //  position: [-5, -1, 0],
        scale: [0.2, 0.2, 0.2],
    });

}