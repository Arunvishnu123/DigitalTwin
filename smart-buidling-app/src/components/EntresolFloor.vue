<template>
<div>
    <canvas id="Canvas"> </canvas>
</div>
</template>

<script>
import * as floorView from "../features/floorView";
import {
    Viewer
} from "@xeokit/xeokit-sdk/";
export default {
    mounted() {
        const viewer = new Viewer({
            canvasId: "Canvas",
        });

        floorView.floorView("3_b98WEDT7feUaJ_WJeW_M", viewer);
    },
};
</script>

<style scoped>
</style>
