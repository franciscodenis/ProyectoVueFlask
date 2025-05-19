import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedState from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'
import OpenLayersMap from "vue3-openlayers";
import "vue3-openlayers/styles.css";


const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedState)
app.use(pinia)
app.use(OpenLayersMap /* options */);
app.use(router)

app.mount('#app')
