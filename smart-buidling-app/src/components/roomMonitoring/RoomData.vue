<template>
<div>
    <w-drawer width="120em" class="tempDialogBox" v-model="$store.state.roomDialog" :[position]="true">
        <w-button @click="$store.state.roomDialog = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
            <w-tag xl height="2em" class="temp" bg-color="primary">Room Details</w-tag>
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