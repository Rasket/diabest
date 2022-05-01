<template lang="pug">
div
  hello-world
  v-form
    v-container
      v-row
        v-col(cols='12' sm='6' md='3')
          v-text-field(label='Regular')

</template>

<script>
  import HelloWorld from '../components/HelloWorld'

  export default {
    name: 'HomeView',

    components: {
      HelloWorld,
    },
  }
</script>
