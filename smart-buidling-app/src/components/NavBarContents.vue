<template>
<div>
    <w-app>
        <w-drawer class="dialogbox" v-model="$store.state.openDrawer" :[position]="true">
            <w-button class = "cross" @click="$store.state.openDrawer = false" sm outline round absolute icon="wi-cross">
            </w-button>
            <w-flex>
               
            </w-flex>
        </w-drawer>
    </w-app>
</div>
</template>

<script>
import store from "../store/index"
export default {
     data: () => ({
    
    }),
    computed: {
        position() {
            return store.state.openDrawer || "right";
        },
    },
};
</script>

<style scoped>
.floorview {
    position: absolute;
    top: 40px;
    width: 100%;
}
.dialogbox {
    z-index: 200001;
}

</style>
