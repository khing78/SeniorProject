import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import VueThailandAddress from 'vue-thailand-address';
import * as VueGoogleMaps from 'gmap-vue'
import firebase from 'firebase'

Vue.config.productionTip = false

Vue.use(VueGoogleMaps,{
  load:{
    key:'AIzaSyCyoUxesPldKEQINItocHKt7ELaGfXSHWc',
    libraries: 'places,drawing',
  },
})
Vue.use(VueThailandAddress)
const firebaseConfig = {
  apiKey: "AIzaSyBeronCsNPS_TdrgUPV-3nYK68PKnq0WMM",
  authDomain: "cassava-8ae86.firebaseapp.com",
  projectId: "cassava-8ae86",
  storageBucket: "cassava-8ae86.appspot.com",
  messagingSenderId: "672705670329",
  appId: "1:672705670329:web:a38dfa7392ecef56dfff68",
  measurementId: "G-TMZ7M1SJ9G"
};
firebase.initializeApp(firebaseConfig);
firebase.analytics();

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
