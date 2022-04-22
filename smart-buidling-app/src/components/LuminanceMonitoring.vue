<template>
<div>
 
    <w-drawer width="120em" class="luminanceDialogBox" v-model="$store.state.luminancedisplay" :[position]="true">
        <w-button @click="$store.state.luminancedisplay = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
         <w-tag xl height="2em" class="luminance" bg-color="primary">Luminance Monitoring</w-tag>
         <iframe src="http://193.49.165.77:8080/analyzer/?items=emse_fayol_4ET_408_mqtt_light&chartType=&coordSystem=" width="100%" height="100%">
</iframe>
        </w-flex>
    </w-drawer>

</div>
</template>

<script>
import store from "../store/index"
export default {
    data: () => ({
       
    }),
    computed: {
        position() {
            return store.state.luminancedisplay || "right";
        },
    },
};
</script>

<style scoped>
.luminanceDialogBox{
    z-index: 2000010;
    width:100%
}
.luminance{
    width:100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

</style>
