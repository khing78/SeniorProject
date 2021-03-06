import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import * as VueGoogleMaps from 'gmap-vue'
import firebase from 'firebase'
import VueAxios from "vue-axios";
import axios from "axios";

Vue.config.productionTip = false

Vue.use(VueGoogleMaps,{
  load:{
    key:'AIzaSyCtY2jTVBVhJhvs3NC17WZc5UYTY74jf48',
    libraries: 'places,drawing',
  },
})
Vue.use(VueAxios, axios);
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
