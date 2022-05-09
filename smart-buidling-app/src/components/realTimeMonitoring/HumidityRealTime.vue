<template>
<div>
    <Humidity/>
    <w-button xl class="realHum mr4" @click="$store.state.humiditydisplay = true" bg-color="primary">Click to View Historical Humidity
    </w-button>
</div>
</template>

<script>
import Humidity from "../../widgets/Humidity.vue"
export default {
    data: () => ({
    }),
    components: {
        Humidity,
    },
};
</script>

<style scoped>
.realHum {
    width: 99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    overflow-x: hidden;
    overflow-y: hidden;
}
</style>
