<script>
  export default {
    name: 'HeaderView',
    data: function () {
      return {
        searchRequest: '',
        placehld: 'Ваш запрос...'
      }
    },
    components: {

    },
    props: {
      isHeaderNeed: {
      }
    },
    watch: {
      searchRequest () {
        console.log(this.searchRequest)
      }
    },
    created () {

    },
    methods: {
      chanegPlac () {
      }
    }
  }
</script>


<template lang="pug">
div(v-if="isHeaderNeed")
  v-app-bar(color='#bce08a' dense='' dark='' height='72px')
    img(:src="require('../assets/special_force.png')" :width="78")
    .search-box
      button.btn-search
        v-icon(color=' 	#a4dad2') mdi-magnify
        i.fas.fa-search
      input.input-search(v-on:click="chanegPlac" type='text' v-bind:placeholder="placehld")
    v-spacer
    v-btn(icon='')
      v-icon mdi-heart


    v-menu(left='' bottom='')
      template(v-slot:activator='{ on, attrs }')
        v-btn(icon='' v-bind='attrs' v-on='on')
          v-icon mdi-dots-vertical
      v-list
        v-list-item(v-for='n in 5' :key='n' @click='() => {}')
          v-list-item-title Option {{ n }}

</template>


<style>
*{
  box-sizing: border-box;
}
body{
  font-family: 'Lato' !important;
}
.search-box{
  width: fit-content;
  height: fit-content;
  position: relative;
}
.input-search{
  height: 40px;
  width: 40px;
  text-align: center;
  border-style: none;
  margin-top: -5px;
  font-size: 18px;
  letter-spacing: 2px;
  outline: none;
  border-radius: 20px;
  transition: all .5s ease-in-out;
  background-color: #569099;
  padding-right: 40px;
  color: #569099;
  caret-color: black;
  border-bottom:1px solid  #2A4480;
}
.input-search::placeholder{
  color: #2A4480;
  font-size: 18px;
  letter-spacing: 2px;
}

.input-search:focus::placeholder{
  color: transparent;
}
.btn-search{
  height: 40px;
  width: 40px;
  border-style: none;
  font-size: 20px;
  font-weight: bold;
  outline: none;
  cursor: pointer;
  margin-top: -6px;
  border-radius: 50%;
  position: absolute;
  right: 0px;
  color:#06266F ;
  background-color:transparent;
  pointer-events: painted;
}
.btn-search:focus ~ .input-search{
  width: 600px;
  border-radius: 0px;
  background-color: transparent;
  border-bottom:1px solid  #2A4480;
  transition: all 1000ms;
}
.input-search:focus{
  width: 600px;
  border-radius: 0px;
  background-color: transparent;
  border-bottom:1px solid  #2A4480;
  transition: all 1000ms cubic-bezier(0, 0.110, 0.35, 2);
}


</style>
