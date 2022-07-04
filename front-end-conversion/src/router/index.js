import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home.vue"
import UploadFile from "../components/UploadIFCComponent.vue"
import AddKnowledge  from "../components/AddSparqlComponent.vue"
import UpdateKnowledge  from "../components/UpdateKnowldegeComponent.vue"
import Visualize from "../components/VisualizeComponent.vue"

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
  {
    path: '/addKnowledge',
    name: 'addknowledge',
    component: AddKnowledge
  },
  {
    path: '/updateknowledge',
    name: 'UpdateKnowledge ',
    component: UpdateKnowledge 
  },
  {
    path: '/visualizeGraph',
    name: 'visualizeGraph',
    component: Visualize 
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
