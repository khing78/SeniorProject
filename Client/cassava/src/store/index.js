import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    name:"",
    path:[]
  },
  getters:{
    getName(state){
      return state.name
    },
    getPath(state){
      return state.path
    }
  },
  mutations: {
    setName(state ,payload){
      state.name = payload.name
  },
    setPath(state ,payload){
    state.path = payload.path
},
  },
  actions: {
  },
  modules: {
  }
})
