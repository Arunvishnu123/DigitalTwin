<template>
<div>
    <w-drawer width="120em" class="humiditydisplayDialogBox" v-model="$store.state.humiditydisplay" :[position]="true">
        <w-button @click="$store.state.humiditydisplay = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
            <w-tag xl height="2em" class="humidity" bg-color="primary">Historical Data</w-tag>
            <iframe src="http://193.49.165.77:8080/analyzer/?items=emse_fayol_4ET_408_mqtt_humidity&chartType=&coordSystem=" width="100%" height="100%">
            </iframe>
            <w-tag xl height="2.5em" class="hide1" color="white" bg-color="primary">408 Humidity Monitoring</w-tag>
        </w-flex>
    </w-drawer>
</div>
</template>

<script>
import store from "../../store/index";
export default {
    data: () => ({}),
    computed: {
        position() {
            return store.state.humiditydisplay || "right";
        },
    },
};
</script>

<style scoped>
.humiditydisplayDialogBox {
    z-index: 2000010;
    width: 100%;
}

.humidity {
    width: 100%;

    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.main1 {
    overflow: hidden;
}

.hide1 {
    z-index: 20000050;
    position: absolute;
    top: 35px;
    width: 100%;
    border-radius: 3px;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
</style>
