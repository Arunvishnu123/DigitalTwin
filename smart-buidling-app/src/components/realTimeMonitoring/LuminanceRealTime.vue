<template>
<div>
    <Luminance />
    <w-button xl class="realLum mr4" @click="$store.state.luminancedisplay = true" bg-color="primary">Click to View Historical Luminanace
    </w-button>
</div>
</template>

<script>
import Luminance from "../../widgets/Luminance.vue"
export default {
    data: () => ({
    }),
    components: {
        Luminance,
    },
};
</script>

<style scoped>
.realLum {
    width: 99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    overflow-x: hidden;
    overflow-y: hidden;
}
</style>
