<template>
<w-dialog class="dialog" v-model="$store.state.tablepersonDialog" overlay-color="rgba(135, 121, 199, 0.5)" :width="460" title-class="primary-light1--bg white">
    <template  #title>
        <font-awesome-icon class="userIcon" :icon="['fa', 'user']"></font-awesome-icon>
           Employee Details
    </template>

    <w-button class="closePerson"  @click="$store.state.tablepersonDialog = false" sm outline round bg-color="white" absolute icon="wi-cross">
    </w-button>
    <w-image class="image mr5" :src="$store.state.person.imageLink" :width="150" :height="150">
    </w-image>
    <w-tag xl class="personName mr4" bg-color="primary">Name - {{$store.state.person.name}}<br /> Position - {{$store.state.person.postion}} <br /> Email-ID - {{$store.state.person.emailID}}</w-tag>

</w-dialog>
</template>

<script>
export default {

}
</script>

<style scoped>
.personName {
    top: 10px;
    width:99%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    margin-bottom: 10px;
}

.image {
    left: 130px
}
.dialog{
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    padding: 10px;
    border-color: red;
    z-index: 900013;
}
.userIcon{
    padding-right: 10px;
}
.closePerson{
    top:10px
}
</style>
