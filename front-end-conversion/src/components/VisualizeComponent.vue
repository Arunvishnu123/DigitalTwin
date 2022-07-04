<template>
<div>
    <Header />
    <TabMenu />
    <InputText type="text" class="link" v-model="value3" placeholder="Enter the Link to Visualise the Knowledge Graphs" />
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
.link {
    width: 100%
}
</style>
