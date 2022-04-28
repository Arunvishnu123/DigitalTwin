<template>
<w-dialog v-model="$store.state.tablepersonDialog" overlay-color="rgba(85, 121, 129, 0.5)" :width="460" persistent title-class="primary-light1--bg white">
    <template class="test" #title>
        <w-icon class="mr2">mdi mdi-tune</w-icon>
        Person Details
    </template>

    <w-button @click="$store.state.tablepersonDialog = false" sm outline round bg-color="white" absolute icon="wi-cross">
    </w-button>
    <w-image class="image mr5" :src="$store.state.person.imageLink" :width="150" :height="150">
    </w-image>
    <w-tag xl class="personName mr4" bg-color="primary">Name -  {{$store.state.person.name}}<br /> Position - {{$store.state.person.postion}} <br /> Email-ID - {{$store.state.person.emailID}}</w-tag>

</w-dialog>
</template>

<script>
export default {

}
</script>

<style scoped>
.personName {
    top:10px;
    width: 95%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
.image{
    left:130px
}
</style>
