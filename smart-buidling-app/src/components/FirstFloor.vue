<template>
<div>
    <canvas id="Canvas">
    </canvas>
</div>
</template>

<script>
import * as floorView from "../features/floorView"
export default {
    mounted() {
        const viewer = new Viewer({
            canvasId: "myCanvas",
        });

        floorView.floorView("3_b98WEDT7feUaJ_WJeW_M",viewer)
    }
}
</script>

<style scoped>

</style>
