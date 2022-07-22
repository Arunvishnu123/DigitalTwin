import Vue from "vue";
import VueRouter from "vue-router";

import Display3d from "../views/Display3d.vue"
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "3DModel",
    component: Display3d
  },

 
]

const router = new VueRouter({
  routes,
  mode: "history",
  history: true,
 base: process.env.BASE_URL,

});



export default router;
