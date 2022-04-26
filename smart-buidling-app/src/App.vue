<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data: () => ({}),
  mounted(){
const input = prompt("which floor you need to go");
console.log("test",input)
  },
  components: {},
};
</script>

<style scoped>
html,
body {
  margin: 0;
  height: 10%;
  overflow-y: hidden;
  overflow-x: hidden;
}
</style>
