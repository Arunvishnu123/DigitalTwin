<template>
<div>
 
    <w-drawer width="120em" class="roomDialogBox" v-model="$store.state.roomdisplay" :[position]="true">
        <w-button @click="$store.state.roomdisplay = false" sm outline round bg-color="white" absolute icon="wi-cross">
        </w-button>
        <w-flex column>
         <w-tag xl height="2em" class="room" bg-color="primary">Room Monitoring</w-tag>
        </w-flex>
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
            return store.state.roomdisplay || "right";
        },
    },
};
</script>

<style scoped>
.roomDialogBox{
    z-index: 2000010;
    width:100%
}
.room{
    width:100%;
    font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}
.main1
{
 
    overflow: hidden; 
}
</style>
