import Vue from "vue";
import VueRouter from "vue-router";


Vue.use(VueRouter);
import App from "../App.vue";

const routes = [
    {
      path: "/test",
      name: "App",
      component: App
    },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
   routes 
  });


  
  export default router;
  