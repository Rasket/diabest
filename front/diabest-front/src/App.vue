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
  }
};
</script>

<template lang="pug">

v-app
  HeaderView().mb-6
  v-main
    router-view



</template>
