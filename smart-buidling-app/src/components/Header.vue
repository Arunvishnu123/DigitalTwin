<template>
<div>
    <w-app>
        <w-tag xl height="2em" class="label mr4" bg-color="primary">Three Dimensional View of Ecole Des Mines in Saint-Etienne</w-tag>
        <w-button @click="$store.state.openDrawer = 'left'" class="bnavbar">
            <font-awesome-icon :icon="['fa', 'bars']"></font-awesome-icon>
        </w-button>
        <nav-bar-contents> </nav-bar-contents>
    </w-app>
</div>
</template>

<script>
import NavBarContents from "./NavBarContents.vue";

export default {
    components: {
        NavBarContents
    },
    data: () => ({
        openDrawer: false,
    }),
    computed: {},
    methods: {},
};
</script>

<style scoped>
.label {
    width: 100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    z-index: 200001;
}

.bnavbar {
    left: -900px;
    top: -30px;
    size: 30px;
    z-index: 200001;
}

.dialogbox {
    z-index: 200001;
}

.floorview {
    position: absolute;
    top: 40px;
    width: 100%;
}
</style>
