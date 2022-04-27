import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);
import * as ReadMqtt from "../features/mqtt"

const store1 = new Vuex.Store({

    state:{
          readTemperature:null
    },
    actions:{
         readTemeprature421(){
             let temp = ReadMqtt.readMQTT("emse/fayol/device/P8/temperature")
             console.log(temp)
         }
    }

})

export default store1;
