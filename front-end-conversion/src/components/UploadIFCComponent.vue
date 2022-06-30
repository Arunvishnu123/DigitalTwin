<template>
<div>
    <div>
        <Header />
        <TabMenu />
    </div>
    <FileUpload name="demo[]" url="./upload">
        <template #empty>
            <p>Drag and drop files to here to upload.</p>
        </template>
    </FileUpload>
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
}
</script>

<style scoped>

</style>
