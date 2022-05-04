import Vue from 'vue'
import VueRouter from 'vue-router'
import RegistrationPage from '../components/RegistrationPage.vue'
import IndexView from '../components/IndexView.vue'
import ProductCard from '../views/ProductCard.vue'
import ProfileView from '../views/ProfileView.vue'
import SingleCardView from '../views/SingleCardView.vue'
import WikiView from '../views/WikiView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/registration/', // legacy
    name: 'Registration',
    component: RegistrationPage
  },
  {
    path: '/product/:id', // карточка продукта
    name: 'SingleCard',
    component: SingleCardView,
    props: true
  },
  {
    path: '/profile/', // профиль пользователя
    name: 'Profile',
    component: ProfileView
  },
  {
    path: '/:phoneProp&:codeProp', // ссылка на регистрацию
    name: 'IndexViewProps',
    component: IndexView,
    props: true
  },
  {
    path: '/', // главная страница
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
    path: '/wiki/', // wiki
    name: 'WikiView',
    component: WikiView,
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
    path: '/pcard/', // test
    name: 'ProductCard',
    component: ProductCard,
  },]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
