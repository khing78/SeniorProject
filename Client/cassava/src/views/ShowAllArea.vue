<template>
  <v-main class="show-all-area">
    <v-container fluid>
      <v-row>
        <v-col>
          <v-btn color="#1CE227" rounded @click="moveto('addarea')"
            >+ เพิ่มแปลงใหม่</v-btn
          >
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-combobox
            v-model="selectprovince"
            :items="allprovince"
            label="จังหวัด"
            outlined
            dense
          ></v-combobox>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field
            v-model="selectdistrict"
            label="อำเภอ"
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-btn id="filterprovincebutton" @click="selectfilter(selectprovince,selectdistrict)"> ค้นหา </v-btn>
          <v-btn id="showeverything" @click="showeveryarea()"> ทั้งหมด </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="8" sm="8">
          <gmap-map
            :center="mapcenter"
            :zoom="16"
            style="width: 100%; height: 500px"
            map-type-id="satellite"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in areashow"
              :position="m.position"
              :clickable="true"
              :draggable="false"
              @click="moveto('Accepted', m.id)"
            ></gmap-marker>
          </gmap-map>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="4" sm="4">
          <v-simple-table fixed-header id="table">
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center" id="areaname">ชื่อแปลง</th>
                  <th class="text-center" id="areaname">รายละเอียด</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="elevation-1"
                  v-for="item in areashow"
                  :key="item.Id"
                  style="text: center"
                  @click="moveto(item.id)"
                >
                  <td>{{ item.name }}</td>
                  <td>{{ item.desciption }}</td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
          <v-col class="text-center">
            <v-btn @click="moveto('Accepted')">ตกลง</v-btn>
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from "vuex";
import firebase from "firebase/app";
import "firebase/auth";
import axios from "axios";
export default {
  data: () => ({
    selectprovince: "",
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เวียงเก่า", "บ้านแฮด", "บ้านฝาง"],
    selectgrade: "",
    mapcenter: { lat: 16.4411261, lng: 102.8644933 },
    detailarea: [
      {
        id: 0,
        name: "แปลงสมชาย",
        province: "ขอนแก่น",
        district: "เมือง",
        desciption: "อ.เมือง จ.ขอนแก่น",
        position: { lat: 18.466022, lng: 102.898313 },
        uid: "",
      },
      {
        id: 1,
        name: "แปลงสมศรี",
        province: "ขอนแก่น",
        district: "เวียงเก่า",
        desciption: "อ.เวียงเก่า จ.ขอนแก่น",
        position: { lat: 16.466037, lng: 99.899724 },
        uid: "",
      },
      {
        id: 2,
        name: "แปลงมารี",
        province: "ขอนแก่น",
        district: "บ้านแฮด",
        desciption: "อ.บ้านแฮด จ.ขอนแก่น",
        position: { lat: 15.465616, lng: 102.899717 },
        uid: "",
      },
    ],
    areashow: [
      {
        id: 0,
        name: "แปลงสมชาย",
        province: "ขอนแก่น",
        district: "เมือง",
        desciption: "อ.เมือง จ.ขอนแก่น",
        position: { lat: 18.466022, lng: 102.898313 },
        uid: "",
      },
      {
        id: 1,
        name: "แปลงสมศรี",
        province: "ขอนแก่น",
        district: "เวียงเก่า",
        desciption: "อ.เวียงเก่า จ.ขอนแก่น",
        position: { lat: 16.466037, lng: 99.899724 },
        uid: "",
      },
      {
        id: 2,
        name: "แปลงมารี",
        province: "ขอนแก่น",
        district: "บ้านแฮด",
        desciption: "อ.บ้านแฮด จ.ขอนแก่น",
        position: { lat: 15.465616, lng: 102.899717 },
        uid: "",
      },
    ],
  }),
  created() {
    //ทุกครั้งที่เข้าหน้ามาให้โหลดข้อมูลแปลงทั้งหมดจาก Database ใหม่
    axios
    .get("http://127.0.0.1:8000/farms/",
     { params: {UId: firebase.auth().currentUser} })
    .then(response => {
      console.log(firebase.auth().currentUser + "response: ", response)
    })
    .catch(err => {
      console.error(err)
    })
  },
  computed: {
    ...mapGetters({
      allprovince: "getProvince",
    }),
  },
  methods: {
    selectfilter(province, district) {
      console.log(district)
      console.log(province)
      //กรองเฉพาะที่เป็นจังหวัดนี้, อำเภอที่เลือก
      var i = 0
      this.areashow = []
      if (district != ""){
        while (i < this.detailarea.length){
        if (province == this.detailarea[i].province && district == this.detailarea[i].district){
          this.areashow.push(this.detailarea[i])
        }
        i++
      }
      }
      else {
        while (i < this.detailarea.length){
        if (province == this.detailarea[i].province){
          this.areashow.push(this.detailarea[i])
        }
        i++
      }
      }
    },
    showeveryarea(){
      this.areashow = this.detailarea
    },
    moveto(i) {
      console.log(i);
      console.log(this.mapcenter.lat, this.mapcenter.lng);
      const vm = this;
      if (i == "addarea") {
        vm.$router.push("/add-area");
      } else if (typeof i == "number") {
        this.mapcenter = this.detailarea[i].position;
      } else if (i == "Accepted") {
        //เอ่ข้อมูลID ของแปลงไปดึงแปลงใน Database
        vm.$router.push("/show-area");
      }
    },
  },
};
</script>
<style scoped>
#table {
  height: 400px;
  padding-bottom: 20px;
}
#areaname {
  background-color: #ffa9a9;
}
#filterprovincebutton{
  margin-right: 1vw;
}
</style>