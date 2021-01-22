import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    uid:"",
    username:"",
    idfarm:"",
    namearea:"",
    selectedarea:"",
    selecteddate:"",
    dateplant:"",
    detailarea:[],
    path:[],
    position:{},
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
    getUid(state){
      return state.uid
    },
    getPosition(state){
      return state.position
    },
    getUserName(state){
      return state.username
    },
    getNameArea(state){
      return state.namearea
    },
    getPath(state){
      return state.path
    },
    getProvince(state){
      return state.province
    },
    getIdFarm(state){
      return state.idfarm
    },
    getDetailArea(state){
      return state.detailarea
    },
    getSelectedArea(state){
      return state.selectedarea
    },
    getSelectedDate(state){
      return state.selecteddate
    },
    getDatePlant(state){
      return state.dateplant
    }
  },
  mutations: {
    setUid(state,payload){
      state.uid = payload.uid
    },
    setPosition(state, payload){
      state.position = payload.position
    },
    setUserName(state, payload){
      state.username = payload.username
    },
    setNameArea(state ,payload){
      state.namearea = payload.namearea
  },
    setPath(state ,payload){
    state.path = payload.path
  },
    setIdFarm(state ,payload){
      state.idfarm = payload.idfarm
  },
    setDetailArea(state ,payload){
      state.detailarea = payload.detailarea
  },
    setSelectedArea(state, payload){
      state.selectedarea = payload.selectedarea
  },
    setSelectedDate(state, payload){
      state.selecteddate = payload.selecteddate
  },
    setDatePlant(state, payload){
      state.dateplant = payload.dateplant
    }
  },
  actions: {
  },
  modules: {
  }
})
