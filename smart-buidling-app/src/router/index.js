import Vue from "vue";
import VueRouter from "vue-router";
import test1 from "../components/SecondFloor.vue"
import DModel from "../views/display3d.vue";
import te from "../components/test.vue"
import g from "../views/FloorView.vue"
import h from "../views/FirstFloor.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "3DModel",
    component: DModel
  },
  {
    path: "/sdf",
    name: "3D",
    component: te
  },
  {
    path: "/sdf",
    name: "3Dsdghf",
    component: g
  },
  {
    path:"/floor",
    name:"floorwisedisplay",
    component:test1
  },
  {
    path:"/d",
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
