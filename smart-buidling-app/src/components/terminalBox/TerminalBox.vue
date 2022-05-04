<template>
<div class="terminalBox">
    <v-shell class="terminal" :banner="banner" :shell_input="send_to_terminal" :commands="commands" @shell_output="prompt"></v-shell>
</div>
</template>

<script>
import {
    StoreyViewsPlugin
} from "@xeokit/xeokit-sdk/";
import store from "../../store/index";
export default {
    data() {
        return {
            send_to_terminal: "",
            banner: {
                header: "Ecole Des Mines in Sain-Etienne",
                subHeader: "Smart Building Project",
                helpHeader: 'Enter "help" for more information.',
                emoji: {
                    first: "",
                    second: "",
                    time: 750,
                },
                sign: "SmartBuilding $",
                img: {
                    align: "left",
                    link: "src/assets/images/test.png",
                    width: 150,
                    height: 150,
                },
            },
            commands: [{
                    name: "et4",
                    get() {
                        const storeyViewsPlugin = new StoreyViewsPlugin(store.state.viewer);
                        storeyViewsPlugin.showStoreyObjects("3_b98WEDT7feUaJ_WJeW$i", {
                            hideOthers: true,
                            useObjectStates: false,
                        });
                        store.state.viewer.camera.eye = [
                            1838782.7620401978, 49.39158880749794, -5156520.24746262,
                        ];
                        store.state.viewer.camera.look = [
                            1838782.6567345671, 15.693182129143608, -5156520.397415988,
                        ];
                        store.state.viewer.camera.up = [
                            -0.5746921936192545, 0.005437435123431921, -0.818351585134634,
                        ];
                        console.log("test");
                        return `<p>Fourth Floor Successfully Separated</p>`;
                    }
                }, {
                    name: "r421",
                    get() {
                        return `<p>Fourth Floor Successfully Separated</p>`;
                    }
                },
        
        ],
    };
},
methods: {
    prompt(value) {
        if (value == "node -v") {
            this.send_to_terminal = process.versions.node;
        }
    },

    test() {
        console.log("test");
    },
},
};
</script>

<style>
.terminal {
    position: absolute;
    height: 1000px;
    width: 1000px;
    left: 0px;
    top: 50px;
    margin-left: 360px;
    margin-right: 30px;
}

.terminalBox {
    overflow-x: scroll;
    overflow-y: scroll;
}
</style>
