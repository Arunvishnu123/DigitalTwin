<template>
<div>
    <w-drawer width="120em" class="tempDialogBox" v-model="$store.state.tempdisplay" :[position]="true">
        <w-button @click="$store.state.tempdisplay = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
            <w-tag xl height="2em" class="temp" bg-color="primary">Historical Data</w-tag>
            <iframe src="http://193.49.165.77:8080/analyzer/?items=emse_fayol_4ET_409_knx_current_temperature&chartType=&coordSystem=" width="100%" height="100%">
            </iframe>
            <w-tag xl height="2.5em" class="hide5" color="white" bg-color="primary">Temperature Monitoring</w-tag>
        </w-flex>
    </w-drawer>
</div>
</template>

<script>
import store from "../store/index";
export default {
    data: () => ({}),
    computed: {
        position() {
            return store.state.tempdisplay || "right";
        },
    },
};
</script>

<style scoped>
.tempDialogBox {
    z-index: 2000010;
    width: 100%;
}

.temp {
    width: 100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.main1 {
    overflow: hidden;
}
.hide5{
   z-index: 20000056;
    position: absolute;
    top: 35px;
    width: 100%;
    border-radius: 3px;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;  
}
</style>
