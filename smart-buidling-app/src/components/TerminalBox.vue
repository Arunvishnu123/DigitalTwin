<template>
<div class="terminalBox">
    <v-shell class="terminal" :banner="banner" :shell_input="send_to_terminal" :commands="commands" @shell_output="prompt"></v-shell>
</div>
</template>

<script>
import {
    StoreyViewsPlugin
} from "@xeokit/xeokit-sdk/";
import store from "../store/index";
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
                    link: "src/assets/test.png",
                    width: 150,
                    height: 150,
                },
            },
            commands: [{
                    name: "info",
                    get() {
                        // this.test()

                        const storeyViewsPlugin = new StoreyViewsPlugin(store.state.viewer);
                        storeyViewsPlugin.showStoreyObjects("3_b98WEDT7feUaJ_WJe3S2", {
                            hideOthers: true,
                            useObjectStates: false,
                        });
                        console.log("test");
                        return `<p>With ❤️ By Salah Bentayeb @halasproject.</p>`;
                    },
                },
                {
                    name: "uname",
                    get() {
                        return navigator.appVersion;
                    },
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
    left:0px;
    top:50px;
    margin-left:360px;
    margin-right:30px

}
.terminalBox{
    overflow-x: scroll;
    overflow-y: scroll;
}
</style>
