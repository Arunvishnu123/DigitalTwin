<template>
<div>
    <w-app class="mainBody">
        <nav-bar></nav-bar>
        <Display3d />
        <TemperatureMonitoring />
        <LuminanceMonitoring />
        <HumidityMonitoring />
        <RoomMontoring />
        <TerminalDialog />
        <RealTimeTemperature />
        <DisplayPersonData />
        <DisplayWindowStatus />
        <Tooltip />    
    </w-app>
</div>
</template>

<script>
import NavBar from "../components/Header.vue";
import Display3d from "../components/View3DModel.vue";
import TemperatureMonitoring from "../components/TemperatureMontioring.vue";
import LuminanceMonitoring from "../components/LuminanceMonitoring.vue";
import HumidityMonitoring from "../components/HumidityMonitoring.vue";
import RoomMontoring from "../components/RoomDetails.vue";
import TerminalDialog from "../components/TerminalDialogBox.vue";
import RealTimeTemperature from "../components/TemperatureRealTime.vue";
import DisplayPersonData from "../components/TablePersonDetails.vue";
import DisplayWindowStatus from "../components/WindowControl.vue";
import Tooltip from "../components/Tooltip.vue"

export default {
    components: {
        Display3d,
        NavBar,
        TemperatureMonitoring,
        LuminanceMonitoring,
        HumidityMonitoring,
        RoomMontoring,
        TerminalDialog,
        RealTimeTemperature,
        DisplayPersonData,
        DisplayWindowStatus,
        Tooltip
    },
    data: () => ({

    }),
    computed: {},
    methods: {
        test(){
            console.log("test")
        }
    },
};
</script>

<style scoped>
.mainBody {
    height: 100%;
    overflow-x: hidden;
    overflow-y: hidden;
}
.toolTip{
    height:100%;
    width: 100%;
}

</style>
