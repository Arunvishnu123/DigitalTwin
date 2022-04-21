<template>
<div>
    <w-app class="mainBody">
        <nav-bar></nav-bar>
        <Display3d />
        <TemperatureMonitoring />
      
    </w-app>
</div>
</template>

<script>
import NavBar from "../components/Header.vue";
import Display3d from "../components/View3DModel.vue";
import TemperatureMonitoring from "../components/TemperatureMontioring.vue"

export default {
    components: {
        Display3d,
        NavBar,
        TemperatureMonitoring
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
