import Vue from 'vue'
import VueRouter from 'vue-router'
import PinDetail from '../views/PinDetail.vue'
import DataSave from '../views/DataSave.vue'
import AreaDetailChart from '../views/AreaDetailChart.vue'
import EditArea from '../views/EditArea.vue'
import AddArea from '../views/AddArea.vue'
import ShowAllArea from '../views/ShowAllArea.vue'
import ShowArea from '../views/ShowArea.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Forgetpassword from '../views/ForgetPassword.vue'
import ChartAllArea from '../views/ChartAllArea.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/pin-detail',
    name: 'pinDetail',
    component: PinDetail
  },
  {
    path: '/data-save',
    name: 'dataSave',
    component: DataSave
  },
  {
    path: '/area-detail-chart',
    name: 'areadetailchart',
    component: AreaDetailChart
  },
  {
    path: '/edit-area',
    name: 'editarea',
    component: EditArea
  },
  {
    path: '/add-area',
    name: 'addarea',
    component: AddArea
  },
  {
    path: '/show-all-area',
    name: 'showallarea',
    component: ShowAllArea
  },
  {
    path: '/show-area',
    name: 'showarea',
    component: ShowArea
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/forgetpassword',
    name: 'forgetpassword',
    component: Forgetpassword
  },
  {
    path: '/chart-all-area',
    name: 'chartAllArea',
    component: ChartAllArea
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
