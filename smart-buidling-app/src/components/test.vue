<template>
<div>
       <button class="test"><font-awesome-icon class="test1" @click="test()"  :icon="['fa', 'bars']"></font-awesome-icon></button>

       <i class="fabars"></i>
</div>
</template>

<script>
export default {
    methods:{
        test(){
            console.log("test")
        }
    }
}
</script>

<style scoped>
.test1{
    color:"white"
}
</style>