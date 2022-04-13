import Vue from "vue";
import VueRouter from "vue-router";


Vue.use(VueRouter);
import App from "../App.vue";

const routes1 = [
    {
      path: "/test",
      name: "App",
      component: App
    },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
    routes:[
      {
        path: "/test",
        name: "App",
        component: App
      },
  ],
  });


  
  export default router;
  