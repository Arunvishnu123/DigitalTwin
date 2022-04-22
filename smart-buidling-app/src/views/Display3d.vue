<template>
<div>
    <w-app class="mainBody">
        <nav-bar></nav-bar>
        <Display3d />
        <TemperatureMonitoring />
        <LuminanceMonitoring />
        <HumidityMonitoring />
        <RoomMontoring />
      
    </w-app>
</div>
</template>

<script>
import NavBar from "../components/Header.vue";
import Display3d from "../components/View3DModel.vue";
import TemperatureMonitoring from "../components/TemperatureMontioring.vue"
import LuminanceMonitoring from "../components/LuminanceMonitoring.vue" 
import HumidityMonitoring from "../components/HumidityMonitoring.vue"
import RoomMontoring from "../components/RoomDetails.vue"

export default {
    components: {
        Display3d,
        NavBar,
        TemperatureMonitoring,
        LuminanceMonitoring,
        HumidityMonitoring,
        RoomMontoring

    },
    data: () => ({}),
    computed: {},
    methods: {},
};
</script>

<style scoped>
.mainBody{
       height: 100%;
    overflow: hidden;
}
</style>
