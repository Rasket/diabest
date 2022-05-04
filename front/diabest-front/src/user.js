let user = {
  utoken: '',
  kako: '123',
  setToken() {
    this.utoken = localStorage.getItem('utoken')
  },
  init () {
    this.setToken()
  }
}

export default user
