import Vue from 'vue';
import Router from 'vue-router';
import CotizadorPrincipal from '@/components/CotizadorPrincipal.vue';
import Admin from '@/components/Admin.vue';

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'CotizadorPrincipal',
      component: CotizadorPrincipal
    },
    {
      path: '/admin',
      name: 'Admin',
      component: Admin
    }
  ]
});

export default router;
