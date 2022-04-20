import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
import * as floorView from "../features/floorView"

const store = new Vuex.Store({
  state: {
    // navbar drawer - dialog box control
    openDrawer: false,

    // 3d model viewer 
    viewer: null,
    model:null,

    //floor wise selection 
    selection:null
  },
  actions: {
  
createFloorView(){
  console.log(this.state.selection)
  floorView.floorView("3_b98WEDT7feUaJ_WJeWog", this.state.viewer,this.state.model);
}
  }
})
export default store;