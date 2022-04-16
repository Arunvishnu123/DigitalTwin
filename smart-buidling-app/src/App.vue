<template>
<div>
    <router-view></router-view>

</div>
</template>

<script>
export default {
unmounted(){
    console.log("test")
}
}
</script>

<style scoped>
html,
body {
    margin: 0;
    height: 100%;
    position: relative;
    overflow-y: hidden;
    overflow-x: hidden;
}
</style>
