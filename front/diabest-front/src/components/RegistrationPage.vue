<script>
import CodeInput from "vue-verification-code-input";
  export default {
    name: 'RegistrationPage',
    data: function () {
      return {
        value: '',
        phone: '',
        show: true,
        animation: false,
        texta: '',
        insideProp: '',
        codeConfirm: false,
        anim_name: 'bounce',
        showSendButton: false,
        innerCode: '',
        innerPhone: '',
        stroka: '',
        no_code: true
      }
    },
    components: {
      CodeInput
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
    created () {
      if (this.codeProp && this.phoneProp) {
        this.no_code = false
        this.codeConfirm = true
        this.insideProp = this.codeProp.split('')
        this.innerCode = this.codeProp
        this.innerPhone = this.phoneProp
        this.anim_name = ''
        this.showSendButton = !this.showSendButton
      } else {
        this.insideProp = ['', '', '', '', '', '']
      }
      this.confirmCode()
    },
    methods: {
      onChange() {
      },
      onComplete(v) {
        this.innerCode = v
        this.showSendButton = !this.showSendButton
      },
      acceptNumber(phone) {
          return (phone.length === 11)
      },
      animat () {
        fetch("http://127.0.0.1:5555/phone/register/" + this.innerPhone, {
            "method": "POST"
        })
        .then(() => {
            this.animation = true
            this.texta = 'Откройте телеграмм по ссылке: '
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
          })
        .catch(err => {
            console.log(err);
        })
      }
    }
  }
</script>


<template lang="pug">
div
  template(v-if="")
    span() {{ stroka }}
  template(v-if="no_code")
    a(href="https://t.me/begegg_bot", target="_blank")
      v-img(max-height='300' max-width='250' src='../assets/tele.png' )
  template(v-if="False")
    .input-phone-text
      div(v-if="!codeConfirm").text-h2 Введите свой номер телефона
    template(v-if="!codeConfirm")
      transition(v-bind:name="anim_name", v-if="!animation")
        div(v-if="!codeConfirm").d-flex.small-form.justify-center.flex-row.mb-6
          v-text-field.phone-input-field(:class="phone-input-field ", label='Номер телефона', v-model="innerPhone", v-bind:single-line="true")
          transition(name='fade')
            v-btn(v-if="acceptNumber(innerPhone)", @click="animat").button-input-line Получить код
    transition(name="fadespecial")
      div(v-if="animation || codeConfirm").main-telegram-text
        span.display-1 {{ texta }}
        a(v-if="!codeConfirm", href="https://t.me/begegg_bot", target="_blank") https://t.me/begegg_bot
        div.main-telegram-text
          span(v-if="!codeConfirm").main-telegram-text И введите полученный код
          span(v-else).main-telegram-text Полученный код
        div.code-input
          CodeInput(:valuesa="insideProp" :loading="false" class="input code-input" v-on:change="onChange" v-on:complete="onComplete").mb-6
          v-btn(v-if="showSendButton",@click="confirmCode").button-input-line Подтвердить

</template>


<style>

.v-input {
  max-width: 25%;
}

/deep/ .small-form div {
  max-width: 25%;
}

.phone-input-field {
  font-size: 48px;
  margin: auto;
  max-width: 50% !important;
}


.code-input {
  margin: auto
}

.fadespecial-enter-active, .fadespecial-leave-active {
  transition-delay: 250ms;
  transition-duration: 0;
  transition: opacity .5s;
}
.fadespecial-enter, .fadespecial-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  transition-delay: 250ms;
  transition-duration: 0;
  opacity: 0;
}

@keyframes appear-in {
  0% {
    opacity:  0;
  }
  50% {
    opacity:  0;
  }
  100% {
    opacity:  1;
  }
}

.additional {
  opacity:  0;
}

.main-telegram-text {
  font-size: 36px;
  position: relative;
  margin: auto;
  text-align: center;
}

.bounce-enter-active {
  animation: bounce-in .5s;
}
.bounce-leave-active {
  animation: bounce-in .5s reverse;
}
@keyframes bounce-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.5);
  }
  100% {
    transform: scale(1);
  }
}

.v-text-field input {
  font-size: 24px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}

.small-form {
  width: 40%;
  margin: auto;
}

.input-phone-text {
  position: relative;
  margin-top: 5%;
  margin-bottom: 5%;
  text-align: center;
}

.button-input-line {
  margin: auto;
  padding-left: 0;
  width: 250px;
}

.main-phone-text {
  font-size: 36px;
  display: inline-block;
  position: relative;
  margin: auto;
  width: 25%;
}


</style>
