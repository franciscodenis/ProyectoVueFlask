import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import BusquedaServicio from '../views/BusquedaServicio.vue'
import VisualizarServicio from '../views/VisualizarServicio.vue'
import SolicitarServicio from '../views/SolicitarServicio.vue'
import ListadoPedidos from '../views/ListadoPedidos.vue'
import AnalisisDatos from '../views/AnalisisDatos.vue'
import SesionView from '../views/SesionView.vue'
import DetallePedido from '../views/DetallePedido.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/Sesion',
      name: 'Sesion',
      component: SesionView
    },
    {
      path: '/BusquedaServicio',
      name: 'BusquedaServicio',
      component: BusquedaServicio
    },
    {
      path: '/VisualizarServicio',
      name: 'VisualizarServicio',
      component: VisualizarServicio
    },
    {
      path: '/SolicitarServicio',
      name: 'SolicitarServicio',
      component: SolicitarServicio
    },
    {
      path: '/DetallePedido/:id',
      name: 'DetallePedido',
      component: DetallePedido,
    },
    {
      path: '/ListadoPedidos',
      name: 'ListadoPedidos',
      component: ListadoPedidos
    },
    {
      path: '/AnalisisDatos',
      name: 'AnalisisDatos',
      component: AnalisisDatos
    }




  ]
})

export default router
