<template>
<div>
    <Header />
    <TabMenu />
   <img class="image" alt="Image Text"  src="https://lh3.googleusercontent.com/d/1Gmh3Aqm9ufDz_tqaYkNeIKimsmts4eSC?authuser=0" />
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
    data() {
        return {
     
        }
    }
};
</script>
<style scoped>
.image{
    position:absolute;
    width:90% ;
    overflow: hidden;
    margin-left:5%;
    margin-top:20px
    }
</style>
