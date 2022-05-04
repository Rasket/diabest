<scriptt
export default {
  name: 'WikiView',

  data: () => ({
  }),
  components: {
  },
  methods: {
    openCard () {
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
div.content
  h1 Это wiki страница сайта diabest, она будет дополняться по мере его улучшения
  h2 Общие положения
  p Данный сайт позволяет пользователям с различными заболеваниями, меняющими их рацион питания находить для себя блюда. На сайте будет реализован функционал позволяющий
  ul.mb-6
    li Регистрироваться
    li Находить блюда по фильтрам
    li Создавать свои блюда
    li Добавлять блюда избранное
    li Лайкать блюда
  p {{ 'На основной странице сайта, в правом верхнем углу есть кнопка для прохождения регистрации. Нажав на неё пользователь откроет мессенджер телеграмм с страницей бота. Ему предложат передать свои контакты и отправят ссылку, пройдя по которой его вернут на главную страницу, но уже зареганным. Теперь пользователю доступен весь функционал сайта. На главной странице можно открывать блюда и смотреть подробности о них. В правом верхнем углу расположен теперь профиль, а слева сверху иконка, по которой можно вернуться на главную страницу. Также справа находится ссылка на данный документ под названием "База данных".'}}
  h2 Профиль
  h2 Поиск
  h2 Создание блюд


</template>


<style>

.content {
  width: 60%;
  margin: auto;
}

.container-limits {
  height: 450px;
  width: 250px;
}

</style>
