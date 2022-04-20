import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
import * as floorView from "../features/floorView"

const store = new Vuex.Store({
  state: {
    // navbar drawer - dialog box control
    openDrawer: false,

    // 3d model viewer 
    viewer: null
  },
  actions: {
  

  }
})
export default store;