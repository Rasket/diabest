import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import user from './user'
import VueApexCharts from 'vue-apexcharts'

Vue.config.productionTip = false

Vue.use(vuetify);
Vue.use(VueApexCharts);

Vue.mixin({
  data () {
    return {
      $user: user
    }
  },
  beforeCreate () {
    this.$user = user
    this.$user.init()
  },
})

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
