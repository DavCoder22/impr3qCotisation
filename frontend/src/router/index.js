import Vue from 'vue';
import Router from 'vue-router';
import CotizadorPrincipal from '@/components/CotizadorPrincipal.vue'; // Asegúrate de que la ruta sea correcta

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'CotizadorPrincipal',
      component: CotizadorPrincipal
    }
  ]
});
