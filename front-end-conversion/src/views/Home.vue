<template>
<div>
    <Header />
    <TabMenu />
</div>
</template>

<script>
import Header from "../components/HeaderComponent.vue";
import TabMenu from "../components/TabMenuComponent.vue";
export default {
    components: {
        Header,
        TabMenu,
    },
};
</script>
