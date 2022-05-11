<template>
<div>
    <w-dialog bg-color="grey-light3" class="tempTitle" v-model="$store.state.temeperatureRealTime" overlay-color="rgba(85, 121, 129, 0)" :width="460" title-class="primary-light1--bg white">
        <template #title>
            <font-awesome-icon class="tempIcon" :icon="['fa', 'thermometer']"></font-awesome-icon>
            Real-Time Monitoring
        </template>
        <w-button @click="$store.state.temeperatureRealTime = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <Temperature v-if="selection == 1" />
        <Humidity v-if="selection == 2" />
        <Luminance v-if="selection == 3" />
        <w-radios v-model="selection" color="green-dark2" class="selectors" :items="radioItems" inline></w-radios>
    </w-dialog>
</div>
</template>

<script>
import Temperature from "./TemperatureRealTime.vue";
import Humidity from './HumidityRealTime.vue'
import Luminance from "./LuminanceRealTime.vue"
export default {
    components: {
        Temperature,
        Humidity,
        Luminance
    },
    data: () => ({
        radioItems: [{
                label: "Temperature",
                value: 1
            },
            {
                label: "Humidity",
                value: 2
            },
            {
                label: "Luminanance",
                value: 3
            },
        ],
        selection: 1,
        labelRealTime: null
    }),

    mounted() {
        if (this.selection == 1) {
            this.labelRealTime = "Temperature"
        }

        if (this.selection == 2) {
            this.labelRealTime = "Relative Humidity"
        }

        if (this.selection == 3) {
            this.labelRealTime = "Luminance"
        }
    }
};
</script>

<style scoped>
.tempTitle {
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    overflow-x: hidden;
    overflow-y: hidden;
}

.tempIcon {
    margin-right: 10px;
}

.selectors {
    position: relative;
    padding: 0px;
    top: 10px;
    margin-bottom: 10px;
    margin-left: 50px;
    overflow-x: hidden;
    overflow-y: hidden;
}
</style>
