<template>
<div>
    <div>
        <Header />
        <TabMenu />
    </div>
    <span class="p-input-icon-left test">
        <InputText type="text" class="test" v-model="value3" placeholder="Enter the Destination Folder Address" />
    </span>
    <FileUpload name="demo[]" url="./upload">
        <template #empty>
            <p>Choose the IFC File to Convert</p>
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
.test{
    width:100%
}
</style>
