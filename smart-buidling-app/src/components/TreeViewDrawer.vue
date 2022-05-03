<template>
<div>
    <w-drawer class="treeView" v-model="$store.state.openTreeView" :[position]="right">
        <w-flex column>
            <w-tag xl height="2em" class="label1" bg-color="primary">Tree View</w-tag>
            <w-button class="cross" @click="$store.state.openTreeView = false" bg-color="white" outline absolute round icon="wi-cross">
            </w-button>
            <div>
                <div id="treeViewContainer"></div>
            </div>
        </w-flex>
    </w-drawer>
</div>
</template>

<script>
import {
    TreeViewPlugin
} from "@xeokit/xeokit-sdk/";
import store from "../store/index"
export default {
    computed: {
        position() {
            return store.state.openTreeView || 'right'
        }
    },
    mounted() {
        const test = document.getElementById("treeViewContainer");
        console.log("sdsahdsgadgsad", test)
        const treeView = new TreeViewPlugin(store.state.viewer, {
            containerElement: "treeViewContainer",
            autoExpandDepth: 1,
            hierarchy: "storeys",
            sortNodes: true,
            sortableStoreysTypes: ["IfcWall", "IfcWallStandardCase", "IfcSlab", "IfcFurniture", "IfcFurnishingElement", "IfcDoor", "IfcRoof"]
        });

    }
}
</script>

<style scoped>
.treeView {
    z-index: 200084;
}

#treeViewContainer {
    pointer-events: all;
    height: 100%;
    overflow-y: scroll;
    overflow-x: hidden;
    position: absolute;
    background-color: rgba(255, 255, 255, 0.2);
    color: black;
    top: 80px;
    z-index: 200000;
    float: left;
    left: 0;
    padding-left: 10px;
    font-family: 'Roboto', sans-serif;
    font-size: 15px;
    user-select: none;
    -ms-user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    width: 350px;
}

#treeViewContainer ul {
    list-style: none;
    padding-left: 1.75em;
    pointer-events: none;
}

#treeViewContainer ul li {
    position: relative;
    width: 500px;
    pointer-events: none;
    padding-top: 3px;
    padding-bottom: 3px;
    vertical-align: middle;
}

#treeViewContainer ul li a {
    background-color: #eee;
    border-radius: 50%;
    color: #000;
    display: inline-block;
    height: 1.5em;
    left: -1.5em;
    position: absolute;
    text-align: center;
    text-decoration: none;
    width: 1.5em;
    pointer-events: all;
}

#treeViewContainer ul li a.plus {
    background-color: #ded;
    pointer-events: all;
}

#treeViewContainer ul li a.minus {
    background-color: #eee;
    pointer-events: all;
}

#treeViewContainer ul li a:active {
    top: 1px;
    pointer-events: all;
}

#treeViewContainer ul li span:hover {
    color: white;
    cursor: pointer;
    background: black;
    padding-left: 2px;
    pointer-events: all;
}

#treeViewContainer ul li span {
    display: inline-block;
    width: calc(100% - 50px);
    padding-left: 2px;
    pointer-events: all;
    height: 23px;
}

#treeViewContainer .highlighted-node {
    /* Appearance of node highlighted with TreeViewPlugin#showNode() */
    border: black solid 1px;
    background: yellow;
    color: black;
    padding-left: 1px;
    padding-right: 5px;
    pointer-events: all;
}
</style>
