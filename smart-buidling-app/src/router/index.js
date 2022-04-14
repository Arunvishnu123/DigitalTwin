import Vue from "vue";
import VueRouter from "vue-router";
import test1 from "../components/SecondFloor.vue"
import first from "../components/View3DModel.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/test",
    name: "test",
    component: first
  },
  {
    path:"/",
    name:"test1",
    component:test1
  }
]

const router = new VueRouter({
  routes,
  mode: "history",
// base: process.env.BASE_URL,

});



export default router;
