<template>
<div>
    <Header />
    <TabMenu />
    <span class="p-input-icon-left test">
        <InputText type="text" class="link" v-model="value3" placeholder="Enter the Link to Visualise the Knowledge Graphs" />
    </span>
</div>
</template>

<script>
import Header from "../components/HeaderComponent.vue";
import TabMenu from "../components/TabMenuComponent.vue";
export default {
    components: {
        Header,
        TabMenu
    },
}
</script>

<style scoped>
.link{
    width:100%
}
</style>
