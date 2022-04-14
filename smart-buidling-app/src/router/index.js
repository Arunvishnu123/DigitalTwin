import Vue from "vue";
import VueRouter from "vue-router";

import App from "../App.vue"
Vue.use(VueRouter);
import first from "../components/View3DModel.vue";

const routes = [
    {
      path: "/test",
      name: "App",
      component: App
    },
    {
      path:"/gg",
      name:"test",
      component:first
    }
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
   routes 
  });


  
  export default router;
  