<script>
import ProductCard from '../views/ProductCard.vue'

  export default {
    name: 'IndexView',
    data: function () {
      return {
        alignments: [
          'start',
          'center',
          'end',
        ],
      }
    },
    components: {
      ProductCard
    },
    props: {

    },
    watch: {
      searchRequest () {
        console.log(this.searchRequest)
      }
    },
    created () {

    },
    methods: {

    }
  }
</script>


<template lang="pug">
.asdf
    v-container.d-flex.justify-xl-space-around.fill-height.grey.lighten-5.mb-6(fluid='' :key='align')
      v-row(align='center' justify='space-around' no-gutters='' style='height: 150px; width: 150px;')
        span(v-for='n in 4' :key='n')
          v-flex
            v-col()
              ProductCard().pa-2.ma-2
            v-spacer



</template>


<style>

.asdf {
  width: 80%;
  margin: auto;
}

</style>
