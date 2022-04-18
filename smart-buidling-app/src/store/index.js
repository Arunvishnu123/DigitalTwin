import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    viewDisplay3d: true,
    viewFloorView: false,
    viewFirstFloor: false
  },
  actions: {
    viewFloorView() {
      this.state.viewFloorView = true
      this.state.viewDisplay3d =false
      console.log("test")
      console.log(this.state.viewFloorView)
    },
    viewFirstFloor(){
      this.state.viewFirstFloor = true
      this.state.viewFloorView = false
    }
  }
})
export default store;