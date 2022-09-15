import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
import * as floorView from "../features/floorViews/floorView"
import display from './componentModule/display';


const store = new Vuex.Store({



  state: {
    // navbar drawer - dialog box control
   // openDrawer: false,
   createThing:false,
    // 3d model viewer 
    viewer: null,
    model: null,
    id:null, 
    class:null , 
    url:null, 
    createEmployee:false,

    thingIfcId:null , 
    thingifcClass:null , 

    //floor wise selection 
    selection: null,

    //context menu switch 
    contextMenuSelection: false,

    //context menu object
    objectContextMenu: null,

    //temperature montioring open drawer
    tempdisplay:false,

    //luminance montioring 
    luminancedisplay: false,

    //humidity
    humiditydisplay: false,
    //room display
    roomdisplay: false,
    //terminal dialog box open
    terminalDialog:false,

   //temperature realtime montioring 
   temeperatureRealTime:false,

   readTemperature:0,

   ///table person toggle

   tablepersonDialog:false,

   //window open close dialog

   windowOpenDialog:false,

   //person details
   person :{
        name: null,
        postion:null,
        emailID:null,
        imageLink:null

   },

   ///window1 status room 421
   windowOpen421FD: "Window Closed",
   windowImage:"src/assets/windowClosed.PNG",
   windowStatus:false,

   // room details 

    roomCapacity:null,

    //roomDialog

    roomDialog:false,

    // tree view 

    openTreeView:false





  },
  actions: {

    createFloorView() {
      console.log(this.state.selection)

      if (this.state.selection == 1) {
        floorView.floorView("3_b98WEDT7feUaJ_WJe3S2", this.state.viewer, this.state.model);

      }
      if (this.state.selection == 2) {
        floorView.floorView("3_b98WEDT7feUaJ_WJe2lo", this.state.viewer, this.state.model);

      }
      if (this.state.selection == 3) {
        floorView.floorView("3_b98WEDT7feUaJ_WJe22_", this.state.viewer, this.state.model);

      }
      if (this.state.selection == 4) {
        floorView.floorView("3_b98WEDT7feUaJ_WJeWog", this.state.viewer, this.state.model);
    
      }
      if (this.state.selection == 5) {
        floorView.floorView("3_b98WEDT7feUaJ_WJeWmQ", this.state.viewer, this.state.model);
      }
      if (this.state.selection == 6) {
        floorView.floorView("3_b98WEDT7feUaJ_WJeW$O", this.state.viewer, this.state.model);
      }
      if (this.state.selection == 7) {
        floorView.floorView("3_b98WEDT7feUaJ_WJeW$i", this.state.viewer, this.state.model);
        this.state.viewer.camera.eye = [1838782.7620401978,  49.39158880749794,-5156520.24746262];
        this.state.viewer.camera.look = [1838782.6567345671, 15.693182129143608, -5156520.397415988];
        this.state.viewer.camera.up = [-0.5746921936192545, 0.005437435123431921, -0.818351585134634];
        this.state.display.openDrawer = false
      }
      if (this.state.selection == 8) {
        floorView.floorView("3_b98WEDT7feUaJ_WJeW_M", this.state.viewer, this.state.model);
      }
      if (this.state.selection == 9) {
        floorView.floorView("3_b98WEDT7feUaJ_WJecOD", this.state.viewer, this.state.model);
      }


    },
    readTemeprature421(){
      
  }
  },
  modules:{
            display
  }
})

store.state.a
export default store;