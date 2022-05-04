<script>
export default {
  name: 'SingleCardView',

  data: () => ({
  }),
  components: {
  },
  created () {
  },
  computed: {
  },
  props: {
    Image: {
      String,
      default: ''
    },
    ShortDescription: {
      String,
      default: ''
    },
    id: {

    }
  }
};
</script>

<template lang="pug">

div
  h1 {{ ShortDescription }}
  .d-flex.justify-center
    v-img(max-height='600' max-width='600' v-bind:src="Image")
  a


</template>
