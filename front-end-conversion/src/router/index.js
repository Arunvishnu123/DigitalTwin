import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import UploadFile from"../components/UploadIFCComponent.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/uploadfile',
    name: 'uploadFile',
    component: UploadFile
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
