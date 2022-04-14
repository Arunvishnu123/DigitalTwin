import Vue from 'vue'
import App from './App.vue'
import router from "./router/index";
import store from './store/index';
import WaveUI from 'wave-ui';
import 'wave-ui/dist/wave-ui.css';
//import 'font-awesome/css/font-awesome.min.css';
import "./fa.config"

Vue.use(WaveUI)

const waveui = new WaveUI({
  // Some Wave UI options.
})

new Vue({
  router,
  store,
  waveui,
  render: (h) => h(App),
}).$mount("#app");
