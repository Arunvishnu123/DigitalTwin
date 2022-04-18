<template>
<div>
    <router-view></router-view>
    <display-3d v-if="$store.state.viewDisplay3d"></display-3d>
    <floor-view v-if ="$store.state.viewFloorView"></floor-view>
    <first-floor v-if ="$store.state.viewFirstFloor"></first-floor>
</div>
</template>

<script>

import Display3d from "./views/Display3d.vue"
import FirstFloor from "./views/FirstFloor.vue"
import FloorView from "./views/FloorView.vue"
export default {
    data: () => ({
       
    }),
    components: {
        Display3d,
        FirstFloor,
        FloorView
    },
    unmounted() {
        console.log("test")
    }
}
</script>

<style scoped>
html,
body {
    margin: 0;
    height: 100%;
    position: relative;
    overflow-y: hidden;
    overflow-x: hidden;
}
</style>
