<template>
<div>
    <w-dialog v-model="$store.state. windowOpenDialog" overlay-color="rgba(85, 121, 129, 0.5)" :width="460" persistent title-class="primary-light1--bg white">
        <template #title>
            <w-icon class="mr2">mdi mdi-tune</w-icon>
            Real-Time Temperature Data
        </template>

        <w-button @click="$store.state.windowOpenDialog = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>

        <w-tag xl class="realTemp mr4" bg-color="primary">Temperature in degree Celsius - {{$store.state.readTemperature}} </w-tag>
    </w-dialog>
</div>
</template>

<script>
export default {

}
</script>

<style scoped>
.realTemp {
    width: 95%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
</style>
