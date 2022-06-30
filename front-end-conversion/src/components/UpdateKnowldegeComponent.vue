<template>
    <div>
        <Header />
        <TabMenu />
        <UpdateKnowledge />
    </div>
</template>

<script>
import Header from "../components/HeaderComponent.vue";
import TabMenu from "../components/TabMenuComponent.vue";
import UpdateKnowledge from "../components/UpdateKnowledge.vue"
export default {
      components: {
        Header,
        TabMenu,
        UpdateKnowledge
    },
}
</script>

<style scoped>

</style>