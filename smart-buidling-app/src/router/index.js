import Vue from "vue";
import VueRouter from "vue-router";
import test1 from "../components/SecondFloor.vue"
import DModel from "../views/display3d.vue";

import FloorView from "../views/FloorView.vue"
import h from "../views/FirstFloor.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/dsd",
    name: "3DModel",
    component: DModel
  },

  {
    path: "/floorview",
    name: "floorview",
    component: FloorView
  },
  {
    path:"/floor",
    name:"floorwisedisplay",
    component:test1
  },
  {
    path:"/firstfloor",
    name:"firstfloor",
    component:h
  }
]

const router = new VueRouter({
  routes,
  mode: "history",
  history: true,
 base: process.env.BASE_URL,

});



export default router;
