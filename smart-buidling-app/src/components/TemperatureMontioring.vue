<template>
<div>
 
    <w-drawer width="120em" class="tempDialogBox" v-model="$store.state.tempdisplay" :[position]="true">
        <w-button @click="$store.state.tempdisplay = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
         <w-tag xl height="2em" class="temp" bg-color="primary">Temperature Monitoring</w-tag>
    </w-drawer>

</div>
</template>

<script>
import store from "../store/index"
export default {
    data: () => ({
       
    }),
    computed: {
        position() {
            return store.state.tempdisplay || "right";
        },
    },
};
</script>

<style scoped>
.tempDialogBox{
    z-index: 2000010;
    width:100%
}
.temp{
    width:100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
.main1
{
 
    overflow: hidden; 
}
</style>
