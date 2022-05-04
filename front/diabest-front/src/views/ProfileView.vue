

<script>
import VueApexCharts from 'vue-apexcharts'
  export default {
    name: 'ProfileView',
    data: function () {
      return {
        ingredients_list: [],
        items: ['213', '312'],
        amount: ['чайных ложек', 'стаканов', 'грамм', 'штук'],
        series: [44, 55, 13, 43, 22],
        chartOptions: {
          chart: {
            width: 380,
            type: 'pie',
          },
          labels: ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'],
          responsive: [{
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              },
              legend: {
                position: 'bottom'
              }
            }
          }]
        },
        tab: 'tab-3',
        inner_tab: 'tab-11',
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
    components: {
      apexchart: VueApexCharts,
    },
    props: {
      isHeaderNeed: {
      }
    },
    watch: {
    },
    created () {
      console.log(this.$user.utoken)
    },
    methods: {
      addIngredient () {
        let temp
        this.ingredients_list.push(temp)
      },
      clearIngredients () {
        this.ingredients_list = []
      }
    }
  }
</script>


<template lang="pug">
span
  v-card(elevation="0")
    v-tabs(:dark='1' v-model='tab' color="basil" background-color='rgba(188, 224, 138, 0)' centered='' dark='' icons-and-text='')
      v-tabs-slider()
      v-tab(href='#tab-1' style={color: '#2A4480'}).px-6
        | Stats
        v-icon(color='#2A4480') mdi-chart-bar
      v-tab(href='#tab-2' style={color: '#2A4480'}).px-6
        | Favorites
        v-icon(color='#2A4480') mdi-heart
      v-tab(href='#tab-3' style={color: '#2A4480'}).px-6
        | By yourself
        v-icon(color='#2A4480') mdi-account-box
    v-tabs-items(v-model='tab')
      v-tab-item(v-for='i in 3' :key='i' :value="'tab-' + i")
        template(v-if="i == 1")
          v-card(flat='')
            v-card-text.justify-center.d-flex
              #chart
                apexchart(type='pie' width='380' :options='chartOptions' :series='series')
            v-card-text.justify-center.d-flex 123
        template(v-if="i == 3")
          v-tabs(:dark='1' v-model='inner_tab' color="basil" background-color='rgba(188, 224, 138, 0)' centered='' dark='' icons-and-text='').mt-6
            v-tabs-slider()
            v-spacer
            v-spacer
            v-tab(href='#tab-11' style={color: '#2A4480'}).inner-tabs
              | Общая информация
            v-tab(href='#tab-22' style={color: '#2A4480'}).inner-tabs
              | Инструкция
            v-spacer
            v-spacer
          v-tabs-items(v-model='inner_tab')
            v-tab-item(v-for='i in 2' :key='i' :value="'tab-' + i + i")
              template(v-if="i == 1")
                form.form-limit
                  v-text-field(v-model='name' :error-messages='nameErrors' :counter='30' label='Name' required='' @input='$v.name.$touch()' @blur='$v.name.$touch()')
                  v-text-field(v-model='email' :error-messages='emailErrors' label='E-mail' required='' @input='$v.email.$touch()' @blur='$v.email.$touch()')
                  v-select(v-model='select' :items='items' :error-messages='selectErrors' label='Item' required='' @change='$v.select.$touch()' @blur='$v.select.$touch()')

                  v-container.elevation-4.mb-4
                    div
                      v-btn(@click="addIngredient")
                        | add
                      v-btn(@click='clearIngredients')
                        | remove all
                    div(v-for="n in ingredients_list", key="n").d-flex.justify-center
                      div.d-flex.justify-center
                        v-select(v-model='select' :items='items' :error-messages='selectErrors' label='Ингредиент' required='' @change='$v.select.$touch()' @blur='$v.select.$touch()')
                        v-text-field(label='Количество').mx-4
                        v-select(v-model='select' :items='amount' :error-messages='selectErrors' label='Единица измерения' required='' @change='$v.select.$touch()' @blur='$v.select.$touch()')
                        v-icon.ml-2 mdi-delete-outline

                  v-checkbox(v-model='checkbox' :error-messages='checkboxErrors' label='Do you agree?' required='' @change='$v.checkbox.$touch()' @blur='$v.checkbox.$touch()')
                  v-btn.mr-4(@click='submit')
                    | submit
                  v-btn(@click='clear')
                    | clear
                v-card-text.justify-center.d-flex 123

        template(v-else)
          v-card(flat='')
            v-card-text {{ text }}



</template>



<style>

.inner-tabs {
  margin-left: 50px;
  margin-right: 50px;
}


.form-limit {
  width: 40%;
  margin: auto;
}

.basil {
background-color: #2A4480 !important;
}
.basil--text {
color: #2A4480 !important;
}

.tabsa {
 color: red;
 background: green;
}

</style>
