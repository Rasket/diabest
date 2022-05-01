import Vue from 'vue'
import VueRouter from 'vue-router'
import RegistrationPage from '../components/RegistrationPage.vue'
import IndexView from '../components/IndexView.vue'
import ProductCard from '../views/ProductCard.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/registration/',
    name: 'Registration',
    component: RegistrationPage
  },
  {
    path: '/',
    name: 'IndexView',
    component: IndexView
  },
  {
    path: '/registration/:phoneProp&:codeProp',
    name: 'RegistrationProps',
    component: RegistrationPage,
    props: true
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/pcard/',
    name: 'ProductCard',
    component: ProductCard,
  },]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
