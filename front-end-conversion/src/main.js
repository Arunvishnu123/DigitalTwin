import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import PrimeVue from 'primevue/config';
import Tag from 'primevue/tag';
import TabMenu from 'primevue/tabmenu';
import FileUpload from 'primevue/fileupload';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Editor from 'primevue/editor';
const app = createApp(App);

import "primevue/resources/themes/saga-blue/theme.css"       //theme
import "primevue/resources/primevue.min.css"                 //core css
import "primeicons/primeicons.css"                          //icons


app.use(PrimeVue);
app.use(store).use(router).mount('#app')
app.component('Tag', Tag);
app.component('TabMenu', TabMenu);
app.component("FileUpload" , FileUpload)
app.component("InputText" , InputText)
app.component("Button" , Button)
app.component("Editor" , Editor )