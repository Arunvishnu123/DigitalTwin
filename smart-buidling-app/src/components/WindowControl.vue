<template>
<div class="test5">
    <w-dialog v-model="$store.state.windowOpenDialog" overlay-color="rgba(85, 121, 129, 0.5)" :width="500" persistent title-class="primary-light1--bg white">
        <template #title>
            <w-icon class="mr2">mdi mdi-tune</w-icon>
            Window Control and Status
        </template>
        <div class="mainWindow">
            <w-button @click="$store.state.windowOpenDialog = false" sm outline round bg-color="white" absolute icon="wi-cross">
            </w-button>
            <w-image class="image1 mr5" :src="$store.state.windowImage" width="90%" :ratio="1" height="90%">
            </w-image>
            <w-tag xl class="window mr4" v-if="$store.state.windowOpen421FD" color="white" bg-color="green">Window in Open Position</w-tag>
            <w-tag xl class="window1 mr4" v-if="$store.state.windowOpen421FD == false" color="white" bg-color="red">Window in closed position</w-tag>
            <w-flex justify-center>
                <w-switch class="mr6" v-model="value"></w-switch>
                <span class="title3 mb0">
                    Window Open:
                    <code class="ml2">{{ $store.state.windowOpen421FD }}</code>
                </span>
            </w-flex>
        </div>
    </w-dialog>
</div>
</template>

<script>
export default {
    data: () => ({
        value: false,
        test: "close",
    }),
    methods: {},
};
</script>

<style scoped>
.window {
    top: 10px;
    width: 99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.window1 {
    top: -20px;
    width: 99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.control {
    width: 99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

/* Adapt text color according to the background color. */
.w-switch__track {
    color: #666;
}
.image2{
    top:-20px;
}

.w-switch--on .w-switch__track {
    color: #fff;
}

/* Wider switch. */
.w-switch--wide .w-switch__input {
    width: 55px;
}

.w-switch--wide .w-switch__track {
    width: 35px;
    text-align: center;
}

.image1 {
    overflow: hidden;
}

.mainWindow {
    overflow: hidden;
}
</style>
