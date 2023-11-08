import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
      meta: { requiresAuth: true } // Esta ruta requiere autenticación
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminView.vue'),
      meta: { requiresAdmin: true },
    },
    {
      path: '/access-denied',
      name: 'access-denied',
      component:() => import('../views/AccessDenied.vue')
    },
    {
      path: '/checkout',
      name: 'checkout',
      component: () => import('../views/CheckoutView.vue'),
    },
    {
      path: '/product/:id',
      name: 'product-detail',
      component: () => import('../views/ProductView.vue'),
      props: true, // Pasar los parámetros como props al componente
    },
    {
      path: '/terms-and-conditions',
      name:'terms-and-conditions',
      component: () => import('../views/TermsAndConditions.vue'),
    },
    {
      path: '/request-cancellation',
      name: 'request-cancellation',
      component: () => import('../views/RequestCancellation.vue'),
    },
    {
      path: '/new-password/:token',
      name: 'new-password',
      component: () => import('../views/NewPassword.vue'),
    },
    {
      path: '/help',
      name: 'help',
      component: () => import('../views/Help.vue'),
    },
    {
      path: '/privacy-policy',
      name: 'privacy-policy',
      component: () => import('../views/PrivacyPolicy.vue'),
    },
    {
      path: '/restore-password',
      name: 'restore-password',
      component: () => import('../views/RestorePassword.vue'),
    },
    {
      path: '/buzos',
      name: 'buzos',
      component: () => import('../views/prendas/Buzos.vue'),
    },
    {
      path: '/camperas',
      name: 'camperas',
      component: () => import('../views/prendas/Camperas.vue'),
    },
    {
      path: '/pantalones',
      name: 'pantalones',
      component: () => import('../views/prendas/Pantalones.vue'),
    },
    {
      path: '/camisas',
      name: 'camisas',
      component: () => import('../views/prendas/Camisas.vue'),
    },
    {
      path: '/remeras',
      name: 'remeras',
      component: () => import('../views/prendas/Remeras.vue'),
    },
  ]
})

export default router
