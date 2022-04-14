<template>
<div>
    <w-app>
        <w-flex column>
            <w-tag xl height="2em" class="label mr4" bg-color="primary">Three Dimensional View of Ecole Des Mines in Saint-Etienne</w-tag>

            <w-button @click="openDrawer = 'left'" class="bnavbar">
                <font-awesome-icon :icon="['fa', 'bars']"></font-awesome-icon>
            </w-button>

            <Display3d />

            <w-drawer v-model="openDrawer" :[position]="true">
                <w-button @click="openDrawer = false" sm outline round absolute icon="wi-cross">
                </w-button>
            </w-drawer>

        </w-flex>
    </w-app>
</div>
</template>

<script>
import Display3d from "../components/View3DModel.vue";
export default {
    components: {
        Display3d,
    },
    data: () => ({
        openDrawer: false
    }),
    computed: {
        position() {
            return this.openDrawer || 'right'
        }
    }
};
</script>

<style scoped>
.label {
    width: 100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.bnavbar {
    left: -800px;
    top: -30px;
    size: 30px;
}
</style>
