<template>
<div>
    <router-view></router-view>
    <display-3d v-if="viewDisplay3d"></display-3d>
</div>
</template>

<script>
import Display3d from "./views/Display3d.vue"
import FirstFloor from "./views/FirstFloor.vue"
import FloorView from "./views/FloorView.vue"
export default {
    data: () => ({
        viewDisplay3d: true,
        viewFloorView: false,
        viewFirstFloor: false
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
