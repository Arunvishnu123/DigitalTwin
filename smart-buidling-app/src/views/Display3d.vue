<template>
<div>
    <w-app>
        <w-flex column>
            <w-tag xl height="2em" class="label mr4" bg-color="primary">Three Dimensional View of Ecole Des Mines in Saint-Etienne</w-tag>

            <w-button @click="openDrawer = 'left'" class="bnavbar">
                <font-awesome-icon :icon="['fa', 'bars']"></font-awesome-icon>
            </w-button>
            <Display3d />

            <w-drawer class="dialogbox" v-model="openDrawer" :[position]="true">
                <w-button @click="openDrawer = false" sm outline round absolute icon="wi-cross">
                </w-button>
                <w-flex>
                    <w-button @click="goToFloorView()" class="floorview grow"> Floor View </w-button>
                </w-flex>
            </w-drawer>
        </w-flex>
    </w-app>
</div>
</template>

<script>
import Display3d from "../components/View3DModel.vue";
import router from "../router/index"
export default {
    components: {
        Display3d,
    },
    data: () => ({
        openDrawer: false,
    }),
    computed: {
        position() {
            return this.openDrawer || "right";
        },
    },
    methods: {
        goToFloorView() {
            router.push("/floorview")
        }
    }
};
</script>

<style scoped>
.label {
    width: 100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    z-index: 200001;
}

.bnavbar {
    left: -730px;
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
