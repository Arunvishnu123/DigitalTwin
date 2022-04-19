<template>
<div>
    <w-app>
        <w-flex column>
            <nav-bar></nav-bar>
            <Display3d />
        </w-flex>
    </w-app>
</div>
</template>

<script>
import NavBar from "../components/Header.vue";
import Display3d from "../components/View3DModel.vue";

export default {
    components: {
        Display3d,
        NavBar,
    },
    data: () => ({}),
    computed: {},
    methods: {},
};
</script>

<style scoped>
</style>
