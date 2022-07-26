<template>
<div>
    <w-app class="mainBody">
        <nav-bar></nav-bar>
        <Display3d />
        <TerminalDialog />
        <DisplayPersonData />
        <DisplayWindowStatus />
        <Tooltip />
        <ViewKnowledgeGraphVue />
        <CreateNewThing />
        <createEmployee />

    </w-app>
</div>
</template>

<script>
import NavBar from "../components/header/Header.vue";
import Display3d from "../components/bimModel/View3DModel.vue";
import TerminalDialog from "../components/terminalBox/TerminalDialogBox.vue";
import Tooltip from "../components/bimModel/Tooltip.vue"
import ViewKnowledgeGraphVue from "../components/viewKnowledgeGraph/ViewKnowledgeGraph.vue";
import CreateNewThing from "../components/CreateKnowledgeGraphs/CreateThing.vue";
import createEmployee from "../components/CreateKnowledgeGraphs/createEmployee.vue";

import {
    TreeViewPlugin
} from "@xeokit/xeokit-sdk/";
import store from "../store/index"
export default {
    components: {
        Display3d,
        NavBar,
        TerminalDialog,
        Tooltip,
        ViewKnowledgeGraphVue,
        CreateNewThing,
        createEmployee

    },
    data: () => ({
        h: [1838785.4837244658, 17.222810247329033, -5156526.853220375]
    }),
    computed: {},
    methods: {
        test() {
            console.log("test")
        }
    },

};
</script>

<style scoped>
.mainBody {
    height: 100%;
    overflow-x: hidden;
    overflow-y: hidden;
}

.toolTip {
    height: 100%;
    width: 100%;
}
</style>
