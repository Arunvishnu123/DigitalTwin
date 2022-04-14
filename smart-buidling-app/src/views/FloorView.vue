<template>
<div>
    <splitpanes class="default-theme" horizontal style="height: 100%">
        <pane min-size="20" max-size="70">
            <splitpanes :push-other-panes="false">
                <pane>
                    <w-app>
                        <div>
                       <w-tag   @click="test()" xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 1</w-tag>
                       <first-floor></first-floor>
                        </div>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 2</w-tag>
                    </w-app>
                </pane>
                <pane>
                    <w-app>
                <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 3</w-tag>
                    </w-app>
                </pane>
            </splitpanes>
        </pane>
        <pane>
            <splitpanes :push-other-panes="false">
                <pane>
                    <w-app>
                     <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 1</w-tag>
                    </w-app>
                </pane>
                <pane>
                     <w-app>
                <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 1</w-tag>
                    </w-app>
                </pane>
                <pane>
                       <w-app>
                <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 1</w-tag>
                    </w-app>
                </pane>
            </splitpanes>
        </pane>
        <pane max-size="70">
         <splitpanes :push-other-panes="false">
                <pane>
                       <w-app>
                <w-tag xl height="1.5em" class="floor1 mr4" bg-color="primary">Section View - Floor 1</w-tag>
                    </w-app>
                </pane>
                <pane>
                     <w-app>
                <w-tag xl height="1.5em"  class="floor1 mr4" bg-color="primary">Section View - Floor 2</w-tag>
                    </w-app>
                </pane>
                <pane>
                      <w-app>
                <w-tag xl height="1.5em"  class="floor1 mr4" bg-color="primary">Section View - Floor 3</w-tag>
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
import router from "../router/index"
export default {
    components: {

        Splitpanes,
        Pane,
        FirstFloor,

    },
    methods:{
        test(){
            console.log("test")
            router.push("/firstfloor")
        }
    }
}
</script>

<style scoped>
.floor1{
    width:100%;
     font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

</style>
