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
        innerCode: '',
        innerPhone: '',
        stroka: '',
        utoken: '',
        cards: []
      }
    },
    components: {
      ProductCard
    },
    props: {
      phoneProp: {
        String,
        default: ''
      },
      codeProp: {
        String,
        default: ''
      }
    },
    watch: {
      searchRequest () {
        console.log(this.searchRequest)
      }
    },
    created () {
      this.init()
    },
    methods: {
      init () {
        if (this.codeProp && this.phoneProp) {
          this.innerCode = this.codeProp
          this.innerPhone = this.phoneProp
          this.confirmCode()
          this.$user.setToken()
        }
        this.getRandomCards()
      },
      getRandomCards () {
        fetch("http://127.0.0.1:5555/cards/random/", {
            "method": "GET"
        })
        .then(response => {
            if (response.status === 200) {
              response.json().then(data => {
                console.log(data)
                this.cards = data
              })
            } else {
              console.log("No server connection!")
            }
          })
        .catch(err => {
            console.log(err);
        })
      },
      confirmCode () {
        fetch("http://127.0.0.1:5555/phone/confirm/" + this.innerPhone + '/' + this.innerCode, {
            "method": "GET"
        })
        .then(response => {
          if (!this.$user.utoken) {
              if (response.status === 200) {
                let token = ''
                this.stroka = 'Поздравляю с регистрацией'
                response.json().then(data => {
                  token = (data['token'])
                  localStorage.setItem('utoken', token)
                })
              } else {
                this.stroka = 'Вам нужно попросить бота новую ссылку'
              }
            }
          })
        .catch(err => {
            console.log(err);
        })
      }
    }
  }
</script>


<template lang="pug">
.asdf
    span() {{ stroka }}
    v-container.d-flex.justify-xl-space-around.fill-height.grey.lighten-5.mb-6.pa-0(fluid='' :key='align')
      v-row(align='center' justify='space-around' no-gutters='' style='height: 150px; width: 150px; background: white;')
        span(v-for='c in cards' :key='n')
          v-flex
            v-col()
              ProductCard(v-bind:Image="c.photo", v-bind:ShortDescription="c.name").pa-2.ma-2
            v-spacer



</template>


<style>

.asdf {
  width: 80%;
  margin: auto;
}

</style>
