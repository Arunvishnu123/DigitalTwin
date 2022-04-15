<template>
<div>
    <splitpanes class="default-theme" horizontal style="height: 100%">
        <pane min-size="20" max-size="70">
            <splitpanes :push-other-panes="false">
                <pane>
                    <w-app>
                        <div>
                            <w-tag @click="test()" xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Entresol</w-tag>
                         <entresol-floor></entresol-floor>
                        </div>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - RDC</w-tag>
                    <rdc-floor></rdc-floor>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - SSOL</w-tag>
                        <ssol-floor></ssol-floor>
                    </w-app>
                </pane>
            </splitpanes>
        </pane>
        <pane>
            <splitpanes :push-other-panes="false">
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 1</w-tag>
                        <first-floor></first-floor>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 2</w-tag>
                        <second-floor></second-floor>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 3</w-tag>
                        <third-floor></third-floor>
                    </w-app>
                </pane>
            </splitpanes>
        </pane>
        <pane max-size="70">
            <splitpanes :push-other-panes="false">
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 4</w-tag>
                        <fourth-floor></fourth-floor>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 5</w-tag>
                        <fifth-floor></fifth-floor>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                        <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 6</w-tag>
                        <sixth-floor></sixth-floor>
                    </w-app>
                </pane>
            </splitpanes>
        </pane>
    </splitpanes>
</div>
</template>

<script>
import {
    Splitpanes,
    Pane
} from "splitpanes";
import "splitpanes/dist/splitpanes.css";
import FirstFloor from "../components/FirstFloor.vue"
import SecondFloor from "../components/SecondFloor.vue"
import ThirdFloor from "../components/ThirdFloor.vue"
import FourthFloor from "../components/FourthFlour.vue"
import FifthFloor from "../components/FifthFloor.vue"
import SixthFloor from "../components/SixthFloor.vue"
import EntresolFloor from "../components/EntresolFloor.vue"
import RDCFloor from "../components/RDCFloor.vue"
import SSOLFloor from "../components/SSOLFloor.vue"

import router from "../router/index"
export default {
    components: {
        Splitpanes,
        Pane,
        FirstFloor,
        SecondFloor,
        ThirdFloor,
        FourthFloor,
        FifthFloor,
        SixthFloor,
        EntresolFloor,
        RDCFloor,
        SSOLFloor
    },
    methods: {
        test() {
            console.log("test")
            router.push("/firstfloor")
        }
    }
}
</script>

<style scoped>
.floor1 {
    width: 100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
</style>
