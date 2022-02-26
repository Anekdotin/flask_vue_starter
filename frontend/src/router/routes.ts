import { RouteRecordRaw } from 'vue-router';
import { createRouter, createWebHistory } from 'vue-router'


const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/Index.vue') }],

  },

  {
    path: '/login',
    name: 'login',
    component: () => import('layouts/HeaderPlain.vue'),
    children: [{ path: '', component: () => import('pages/auth/Login.vue') }],

  },

  {
    path: '/register',
    name: 'register',
    component: () => import('layouts/HeaderPlain.vue'),
    children: [{ path: '', component: () => import('pages/auth/Register.vue') }],

  },
    {
    path: '/forgotpassword',
    name: 'forgotpassword',
    component: () => import('layouts/HeaderPlain.vue'),
    children: [{ path: '', component: () => import('pages/auth/ForgotPassword.vue') }],

  },
    {
    path: '/profile',
    name: 'profile',
  component: () => import('layouts/HeaderPlain.vue'),
    children: [{ path: '', component: () => import('pages/auth/Profile.vue') }],

  },
  {
    path: '/changepassword',
    name: 'changepassword',
    component: () => import('layouts/HeaderPlain.vue'),
    children: [{ path: '', component: () => import('pages/auth/ChangePassword.vue') }],

  },
    {
    path: '/account-seed',
    name: 'accountseed',
    component: () => import('layouts/HeaderPlain.vue'),
    children: [{ path: '', component: () => import('pages/auth/AccountSeed.vue') }],

  },
      {
    path: '/account-seed-confirm',
    name: 'accountseedconfirm',
    component: () => import('layouts/HeaderPlain.vue'),
    children: [{ path: '', component: () => import('pages/auth/AccountSeedConfirm.vue') }],

  },
  {
    path: '/logout',
    name: 'logout',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/Index.vue') }],

  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/error/Error404.vue'),
  },



];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/login', '/home'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  // try to access a restricted page + not logged in
  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
});



export default routes;
