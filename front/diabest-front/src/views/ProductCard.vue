<script>
export default {
  name: 'ProductCard',

  data: () => ({
  }),
  components: {
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

div.container-limits
  v-img(lazy-src='https://picsum.photos/id/11/10/6' max-height='300' max-width='250' src='https://picsum.photos/id/11/500/300')
  span 'Те1кст'
  a 'сСЫЛКА'
</template>


<style>



.container-limits {
  height: 450px;
  width: 250px;
}

</style>
