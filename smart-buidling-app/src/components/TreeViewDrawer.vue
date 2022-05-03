<template>
<div>
    <w-drawer class="treeView" v-model="$store.state.openTreeView" :[position]="true">
        <w-flex column>
            <w-tag xl height="2em" class="label1" bg-color="primary">Floor Selection</w-tag>
            <w-button class="cross" @click="$store.state.openTreeView = null" bg-color="white" outline absolute round icon="wi-cross">
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
.treeView
{
    z-index:200084;
}
</style>