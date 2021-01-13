import Vue from 'vue'
import Vuex from 'vuex'
import Axios from "axios";

let mongo_api = "http://127.0.0.1:8000/farms/";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    idfarm:"Hellow",
    name:"",
    path:[],
    province: [
      "กระบี่",
      "กรุงเทพมหานคร",
      "กาญจนบุรี",
      "กาฬสินธุ์",
      "กำแพงเพชร",
      "ขอนแก่น",
      "จันทบุรี",
      "ฉะเชิงเทรา",
      "ชลบุรี",
      "ชัยนาท",
      "ชัยภูมิ",
      "ชุมพร",
      "เชียงราย",
      "เชียงใหม่",
      "ตรัง",
      "ตราด",
      "ตาก",
      "นครนายก",
      "นครปฐม",
      "นครพนม",
      "นครราชสีมา",
      "นครศรีธรรมราช",
      "นครสวรรค์",
      "นนทบุรี",
      "นราธิวาส",
      "น่าน",
      "บึงกาฬ",
      "บุรีรัมย์",
      "ปทุมธานี",
      "ประจวบคีรีขันธ์",
      "ปราจีนบุรี",
      "ปัตตานี",
      "พระนครศรีอยุธยา",
      "พะเยา",
      "พังงา",
      "พัทลุง",
      "พิจิตร",
      "พิษณุโลก",
      "เพชรบุรี",
      "เพชรบูรณ์",
      "แพร่",
      "ภูเก็ต",
      "มหาสารคาม",
      "มุกดาหาร",
      "แม่ฮ่องสอน",
      "ยโสธร",
      "ยะลา",
      "ร้อยเอ็ด",
      "ระนอง",
      "ระยอง",
      "ราชบุรี",
      "ลพบุรี",
      "ลำปาง",
      "ลำพูน",
      "เลย",
      "ศรีสะเกษ",
      "สกลนคร",
      "สงขลา",
      "สตูล",
      "สมุทรปราการ",
      "สมุทรสงคราม",
      "สมุทรสาคร",
      "สระแก้ว",
      "สระบุรี",
      "สิงห์บุรี",
      "สุโขทัย",
      "สุพรรณบุรี",
      "สุราษฎร์ธานี",
      "สุรินทร์",
      "หนองคาย",
      "หนองบัวลำภู",
      "อ่างทอง",
      "อำนาจเจริญ",
      "อุดรธานี",
      "อุตรดิตถ์",
      "อุทัยธานี",
      "อุบลราชธานี",
    ],
  },
  getters:{
    getName(state){
      return state.name
    },
    getPath(state){
      return state.path
    },
    getProvince(state){
      return state.province
    },
    getIdFarm(state){
      return state.idfarm
    }
  },
  mutations: {
    setName(state ,payload){
      state.name = payload.name
  },
    setPath(state ,payload){
    state.path = payload.path
  },
    setIdFarm(state ,payload){
      state.idfarm = payload.idfarm
    }
  },
  actions: {
    async fetchFood({ commit }) {
      await Axios.get(mongo_api)
        .then(res => commit("fetchFood", { res }))
        .catch(err => alert(err));
    },
  },
  modules: {
  }
})
