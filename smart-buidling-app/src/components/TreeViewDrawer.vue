<template>
<div>
    <w-drawer class="dialogbox" v-model="$store.state.openDrawer" :[position]="true">
        <w-flex column>
            <w-tag xl height="2em" class="label1" bg-color="primary">Floor Selection</w-tag>
            <w-button class="cross" @click="$store.state.openDrawer = false" bg-color="white" outline absolute round icon="wi-cross">
            </w-button>
        </w-flex>
    </w-drawer>
</div>
</template>
<script>
export default {
    
}
</script>

<style scoped>

</style>