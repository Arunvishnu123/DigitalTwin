<template>
<div>
    <w-dialog class="tempTitle" v-model="$store.state.temeperatureRealTime" overlay-color="rgba(85, 121, 129, 0.5)" :width="460" persistent title-class="primary-light1--bg white">
        <template #title>
            <font-awesome-icon class="tempIcon" :icon="['fa', 'thermometer']"></font-awesome-icon>
            Real-Time Temperature Data
        </template>

        <w-button @click="$store.state.temeperatureRealTime = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <knob-control class="tempKnob" :size="120" :animation="{
          animated: true,
          animateValue: true,
          animationDuration: '1000',
          animationFunction: 'linear',
        }" :min="0" :max="40" :stroke-width="8" v-model="$store.state.readTemperature"></knob-control>

        <w-tag xl class="realTemp mr4" bg-color="primary">Temperature in degree Celsius - {{ $store.state.readTemperature }}
        </w-tag>
    </w-dialog>
</div>
</template>

<script>
import KnobControl from "vue-knob-control";
export default {
    data: () => ({
        tes: 56,
    }),
    components: {
        KnobControl,
    },
};
</script>

<style scoped>
.realTemp {
    width: 99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
     overflow-x: hidden;
    overflow-y:hidden;
}

.tempTitle {
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
     overflow-x: hidden;
    overflow-y:hidden;
}
.tempKnob{
    margin-left:150px;
    overflow-x: hidden;
    overflow-y:hidden;
}
.tempIcon{
    margin-right:10px
}
</style>
