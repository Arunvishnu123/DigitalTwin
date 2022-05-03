<template>
<div>
    <w-dialog bg-color="grey-light3" class="tempTitle" v-model="$store.state.temeperatureRealTime" overlay-color="rgba(85, 121, 129, 0)" :width="460" title-class="primary-light1--bg white">
        <template #title>
            <font-awesome-icon class="tempIcon" :icon="['fa', 'thermometer']"></font-awesome-icon>
            Real-Time Temperature Data
        </template>

        <w-button @click="$store.state.temeperatureRealTime = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <TempDial />

        <w-button xl class="realTemp mr4" @click="$store.state.tempdisplay = true" bg-color="primary">Click to View Historical Temperature
        </w-button>
    </w-dialog>
</div>
</template>

<script>
import TempDial from "../components/TempDial.vue"
export default {
    data: () => ({
        tes: 56,
        color: "red"
    }),
    components: {
        TempDial
    },
};
</script>

<style scoped>
.realTemp {
    width: 99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    overflow-x: hidden;
    overflow-y: hidden;
}

.tempTitle {
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    overflow-x: hidden;
    overflow-y: hidden;
}

.tempKnob {
    margin-left: 150px;
    overflow-x: hidden;
    overflow-y: hidden;
}

.tempIcon {
    margin-right: 10px;
}
</style>
