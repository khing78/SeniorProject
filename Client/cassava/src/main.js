import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import * as VueGoogleMaps from 'gmap-vue'

Vue.config.productionTip = false

Vue.use(VueGoogleMaps,{
  load:{
    key:'AIzaSyBroHHjH5L5ukvmefyYx9qfkrAjJn2Y0a0',
    libraries: 'places,drawing',
  },
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
