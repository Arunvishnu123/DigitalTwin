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
        <Test1 :position="h"/>
        <EmployeeData />
        <Windowtest />
        <RoomData />
    </w-app>
</div>
</template>

<script>
import NavBar from "../components/header/Header.vue";
import Display3d from "../components/bimModel/View3DModel.vue";
import TemperatureMonitoring from "../components/historicalMonitoring/TemperatureMontioring.vue";
import LuminanceMonitoring from "../components/historicalMonitoring/LuminanceMonitoring.vue";
import HumidityMonitoring from "../components/historicalMonitoring/HumidityMonitoring.vue";
import RoomMontoring from "../components/roomMonitoring/RoomDetails.vue";
import TerminalDialog from "../components/terminalBox/TerminalDialogBox.vue";
import RealTimeTemperature from "../components/realTimeMonitoring/TemperatureRealTime.vue";
import DisplayPersonData from "../components/roomMonitoring/TablePersonDetails.vue";
import DisplayWindowStatus from "../components/realTimeMonitoring/WindowControl.vue";
import Tooltip from "../components/bimModel/Tooltip.vue"
import Test1 from "../widgets/createLabel/SensorData.vue"
import EmployeeData from "../widgets/createLabel/EmployeeInformation.vue"
import Windowtest from "../widgets/createLabel/WindowInformation.vue"
import RoomData from "../widgets/createLabel/RoomData.vue"

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
        Tooltip,
        Test1,
        EmployeeData,
        Windowtest,
        RoomData
    },
    data: () => ({
           h:[1838785.4837244658,17.222810247329033,-5156526.853220375]
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
