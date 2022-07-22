<template>
<div>
    <w-drawer width="120em" class="humiditydisplayDialogBox" v-model="$store.state.humiditydisplay" :[position]="true">
        <w-button @click="$store.state.humiditydisplay = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
            <w-tag xl height="2em" class="humidity" bg-color="primary">{{$store.state.url}}</w-tag>
            <iframe class="fr" :src="$store.state.url">
            </iframe>
        </w-flex>
    </w-drawer>
</div>
</template>

<script>
import store from "../../store/index";
export default {
    data: () => ({
    
    }),
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
.fr{
    height:100%;
    width:100%
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
