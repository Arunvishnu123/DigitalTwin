<template>
    <div>
        <h1>Arun R S </h1>
        <router-link to="/test1">Arun</router-link>
        <button @click="test()" >test</button>
    </div>
</template>

<script>
import router from "../router/index"
export default {
    methods:{
        test(){
            console.log("tests")
            router.push("/test")
        }
    }

}
</script>
<style scoped>

</style>