<template>
<div>
    <w-app>
        <w-drawer class="dialogbox" v-model="$store.state.openDrawer" :[position]="true">
             
            <w-flex column>  
                <w-tag xl height="2em" class="label1" bg-color="primary">Features</w-tag>
                <w-button class="cross" @click="$store.state.openDrawer = false" bg-color="white" outline absolute round icon="wi-cross">
                </w-button>
            </w-flex>
        </w-drawer>
    </w-app>
</div>
</template>

<script>
import store from "../store/index";
export default {
    data: () => ({}),
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
    z-index: 200002;
}

.cross {
    position: absolute;
    z-index: auto;
    top:5px                        
}

.label1 {
    position: absolute;
    z-index: auto;
    width: 100%;
}
</style>
