<template>
<div>
    <w-dialog class="windowTitle" v-model="$store.state.windowOpenDialog" overlay-color="rgba(85, 121, 129, 0.5)" :width="500" persistent title-class="primary-light1--bg white">
        <template #title>
           <font-awesome-icon class="windowClass" icon="fa-solid fa-window-maximize" />
            Window Control and Status
        </template>
        
            <w-button @click="$store.state.windowOpenDialog = false" sm outline round bg-color="white" absolute icon="wi-cross">
            </w-button>
            <img class="image1" :src="$store.state.windowImage" />            
            <w-tag xl class="status" color="white" :bg-color="$store.state.windowStatus  ? 'green' : 'red'">{{ $store.state.windowOpen421FD }}</w-tag>   
    </w-dialog>
</div>
</template>

<script>
export default {
    data: () => ({
        value: false,
    }),
    methods: {},
};
</script>

<style scoped>

.image1 {
    margin-left:160px
}
.status{
    top:10px;
    width:100%;
    margin-bottom: 10px;
     font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
    
}
.windowClass{
    margin-right:10px;
    
}

.windowTitle{
 font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;

}

</style>
