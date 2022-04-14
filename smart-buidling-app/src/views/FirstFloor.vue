<template>
<div>
    <w-app>
        <w-tag xl height="2em" class="label mr4" bg-color="primary">Three Dimensional View of Fifth Floor - Ecole Des Mines in Saint-Etienne</w-tag>
        <first-floor></first-floor>
    </w-app>
</div>
</template>

<script>
import FirstFloor from "../components/FirstFloorFull.vue"
export default {
    components: {
        FirstFloor
    },
}
</script>

<style scoped>
.label {
    width: 100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
</style>
