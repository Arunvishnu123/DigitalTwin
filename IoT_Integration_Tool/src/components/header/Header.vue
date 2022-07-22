<template>
  <div>
    <w-app class="main">
      <w-tag xl height="2em" class="label mr4" bg-color="primary"
        >Mines Saint-Etienne Espace Fauriel Building - New Knowledge Integration Tool</w-tag
      >
      <w-button @click="$store.state.display.openDrawer = 'left'" class="bnavbar">
        <font-awesome-icon :icon="['fa', 'bars']"></font-awesome-icon>
      </w-button>
      <nav-bar-contents> </nav-bar-contents>
    </w-app>
  </div>
</template>

<script>
import NavBarContents from "./NavBarContents.vue";

export default {
  components: {
    NavBarContents,
  },
  data: () => ({
    openDrawer: false,
  }),
  computed: {},
  methods: {},
};
</script>

<style scoped>
.label {
  width: 100%;
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  z-index: 200001;
  color: red;
}

.bnavbar {
 position: absolute;
  z-index: 200081;
  left:5px;
  top:2px
}

.dialogbox {
  z-index: 200001;
}

.floorview {
  position: absolute;
  top: 40px;
  width: 100%;
}
.main {
  height: 100%;
  overflow: hidden;
}
.treeBar{
  position: absolute;
  z-index: 200080;
   left:35px;
   top:2px;
}
@media only screen and  (max-width: 1100px) {
  .bnavbar {
    left: -736px;
    top: -30px;
    size: 30px;
    z-index: 200001;
  }
}
</style>
