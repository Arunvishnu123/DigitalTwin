<template>
    <div>
        <Header />
        <TabMenu />
        <AddKnowledge />
    </div>
</template>

<script>
import Header from "../components/HeaderComponent.vue";
import TabMenu from "../components/TabMenuComponent.vue";
import AddKnowledge from "../components/AddKnowledge.vue"
export default {
      components: {
        Header,
        TabMenu,
        AddKnowledge
    },
}
</script>

<style scoped>

</style>