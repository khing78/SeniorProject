import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    name:""
  },
  getters:{
    getname(state){
      return state.name
    }
  },
  mutations: {
    setUsername(state ,payload){
      state.username = payload.username
  },
  },
  actions: {
  },
  modules: {
  }
})
