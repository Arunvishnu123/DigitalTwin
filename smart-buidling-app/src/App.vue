<template>
<div>
    <router-view></router-view>
</div>
</template>

<script>
import store from "./store/index"
import * as floorView from "./features/floorView/floorView"
export default {
    data: () => ({}),

    methods: {
        et4() {
            console.log("test")
            floorView.floorView("3_b98WEDT7feUaJ_WJeW$i", store.state.viewer, store.state.model);
            store.state.viewer.camera.eye = [1838782.7620401978, 49.39158880749794, -5156520.24746262];
            store.state.viewer.camera.look = [1838782.6567345671, 15.693182129143608, -5156520.397415988];
            store.state.viewer.camera.up = [-0.5746921936192545, 0.005437435123431921, -0.818351585134634];
        }
    }
};
</script>

<style scoped>
html,
body {
    margin: 0;
    height: 10%;
    overflow-y: hidden;
    overflow-x: hidden;
}
</style>
