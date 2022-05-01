<script>
import HeaderView from '@/components/HeaderView.vue'
export default {
  name: 'App',

  data: () => ({
  }),
  components: {
    HeaderView
  },
  created () {
    console.log(this.$router.currentRoute)
  },
  computed: {
    isHeaderNeed () {
      return !(this.$router.currentRoute.name === 'Registration')
    }
  }
};
</script>

<template lang="pug">

v-app
  HeaderView(v-bind:isHeaderNeed="isHeaderNeed").mb-6
  v-main
    router-view

  v-footer(app='')
    img(:src="require('./assets/special_force.png')" :width="256")


</template>
