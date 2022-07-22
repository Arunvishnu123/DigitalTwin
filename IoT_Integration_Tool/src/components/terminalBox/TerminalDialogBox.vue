<template>
<div>
    <w-overlay class="px4" v-model="$store.state.terminalDialog" bg-color="rgba(35, 71, 129, 0.4)">

        <w-button bg-color="primary" class="close" lg dark @click="$store.state.terminalDialog = false">
            <w-icon class="mr2">wi-cross</w-icon>
            Hide
        </w-button>
        <terminal-box></terminal-box>
    </w-overlay>
</div>
</template>

<script>
import store from "../../store/index";
import TerminalBox from "./TerminalBox.vue";
export default {
    data: () => ({}),
    components: {
        TerminalBox,
    },
    computed: {
        position() {
            return store.state.terminalDialog || "right";
        },
    },
};
</script>

<style scoped>
.roomDialogBox {
    z-index: 2000010;
    width: 100%;
}

.room1 {
    width: 100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.close {
    position: relative;
    top: -390px;
    left: 470px
}
</style>
