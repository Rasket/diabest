<script>
export default {
  name: 'ProductCard',

  data: () => ({
  }),
  components: {
  },
  methods: {
    openCard () { // ccылка на открытие полной страницы
      this.$router.push({ name: 'SingleCard', params: {id: '1', Image: this.Image, ShortDescription: this.ShortDescription}})
    }
  },
  props: {
    Image: {
      String,
      default: ''
    },
    ShortDescription: {
      String,
      default: ''
    }
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
  v-img(max-height='300' max-width='250' v-bind:src="Image")
  a
    span(v-on:click="openCard") {{ ShortDescription }}
</template>


<style>



.container-limits {
  height: 450px;
  width: 250px;
}

</style>
