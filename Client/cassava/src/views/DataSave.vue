<template>
  <v-main class="data-save">
    <v-container>
      <v-row>
        <v-col cols="12" md="3" sm="3"> ข้อมูลผลตรวจคุณภาพ</v-col>
        <v-col class="text-right">
          <v-btn id="removebutton" rounded @click="deletearea()"
            >ลบข้อมูล</v-btn
          >
        </v-col>
      </v-row>
      <v-row class="text-center" justify="start">
        <v-col cols="12" md="3" sm="3"
          ><v-menu
            v-model="menu2"
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="5vw"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="computedDateFormatted"
                label="วัน/เดือน/ปี ที่บันทึก"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="date"
              @input="menu2 = false"
            ></v-date-picker> </v-menu
        ></v-col>
        <v-col cols="12" md="3" sm="3"
          ><v-text-field
            v-model="this.datapin[0].position.lat"
            hint="กรุณาใส่ละติจูด"
            label="ละติจูด"
          ></v-text-field
        ></v-col>
        <v-col cols="12" md="3" sm="3"
          ><v-text-field
            v-model="this.datapin[0].position.lng"
            hint="กรุณาใส่ลองจิจูด"
            label="ลองจิจูด"
          ></v-text-field
        ></v-col>
      </v-row>
      <v-row>
        <v-col cols="12">
          <gmap-map
            id="map"
            :center="mapcenter"
            :zoom="18"
            style="width: 100%; height: 500px"
            map-type-id="terrain"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in datapin"
              :position="m.position"
              :clickable="true"
              :draggable="true"
              @dragend="
                changepositionmap($event.latLng.lat(), $event.latLng.lng())
              "
              @click="checkmap(m.position)"
            ></gmap-marker>
          </gmap-map>
        </v-col>
        <v-col cols="12">
          <v-btn id="savebutton" rounded @click="addcassava()">เพิ่มหัวมันสำปะหลัง +</v-btn>
        </v-col>
      </v-row>
      <v-simple-table fixed-header height="50vh" id="table">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-center" style="background-color: #ffa9a9"></th>
            </tr>
          </thead>
          <tbody>
            <tr
              class="text-left"
              v-for="(item, index) in xdata"
              :key="item.name"
            >
              <td>
                <v-row>
                  <v-col class="text-right"
                    ><v-btn
                      rounded
                      id="removebutton"
                      @click="removecassava(index)"
                      >ลบ</v-btn
                    ></v-col
                  >
                </v-row>
                <v-row>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field
                      v-model="item.x1"
                      hint="X1"
                      label="X1"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field
                      v-model="item.x2"
                      hint="X2"
                      label="X2"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field
                      v-model="item.x3"
                      hint="X3"
                      label="X3"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field
                      v-model="item.temputure"
                      hint="อุณหภูมิ"
                      label="อุณหภูมิ"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field
                      v-model="item.x4"
                      hint="X4"
                      label="X4"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field
                      v-model="item.x5"
                      hint="X5"
                      label="X5"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="3" md="3">
                    <v-text-field
                      v-model="item.x6"
                      hint="X6"
                      label="X6"
                    ></v-text-field>
                  </v-col>
                  <v-col>
                    <v-text-field
                      v-model="item.humidity"
                      hint="ความชื้นสัมพันท์"
                      label="ความชื้นสัมพันท์"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
      <v-row>
        <v-col class="text-left">
          <v-btn id="backbutton" rounded @click="moveto('back')">ยกเลิก</v-btn>
        </v-col>
        <v-col class="text-right">
          <v-btn id="savebutton" rounded @click="moveto('save'), addNewArea()">บันทึก</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import axios from 'axios';
import { mapGetters } from "vuex";

export default {
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    lenghtofarea: 5,
    mapcenter: { lat: 16.466022, lng: 102.898313 },
    datapin: [
      // Marker เป็นตัวบอกคุณภาพ
      // ดึงข้อมูลมาจากฐานข้อมูล
      {
        id: 0,
        position: { lat: 16.466022, lng: 102.898313 },
        dategetdata: "26/12/2563",
        icon: "green",
      },
    ],
    xdata: [
      {
        id: 1,
        x1: 0.7568462,
        x2: 5.370551,
        x3: 10.28535,
        x4: 12.38871,
        x5: 24.18566,
        x6: 21.58091,
        temputure: 32.02,
        humidity: 16,
      },
      {
        id: 2,
        x1: 1.892033,
        x2: 10.74111,
        x3: 20.5706,
        x4: 20.89075,
        x5: 36.91494,
        x6: 27.83622,
        temputure: 31.01,
        humidity: 18,
      },
      {
        id: 3,
        x1: 1.922431,
        x2: 9.398447,
        x3: 17.14219,
        x4: 20.49366,
        x5: 38.69703,
        x6: 34.09154,
        temputure: 29.42,
        humidity: 14,
      },
      {
        id: 4,
        x1: 2.270401,
        x2: 6.713198,
        x3: 15.1423,
        x4: 14.57496,
        x5: 31.8232,
        x6: 23.4575,
        temputure: 30.31,
        humidity: 16,
      },
    ],
  }),
  computed: {
    ...mapGetters({
      newidfarm: "getIdFarm",
      areaname: "getNameArea",
      path: "getPath",
    }),
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },
  methods: {
    addNewArea(){
      axios
        .post("http://127.0.0.1:8000/area-check/", {
          farm_store: this.newidfarm,
          starch_percentage: 45,
          tree_latitude: 54613183512,
          tree_longtitude: 13513541831,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
    },
    postData(){
      axios
        .post("http://127.0.0.1:8000/cassava-check/", {
          latitude: '18.466022',
          longtitude: '142.898313',
          spectrum1: '1.922431',
          spectrum2: '9.398447',
          spectrum3: '17.14219',
          spectrum4: '20.49366',
          spectrum5: '38.69703',
          spectrum6: '34.09154',
          temperature: '19.42',
          starchPercentage: '55',
          humidity: '6',
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        })
    },
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/show-area");
      }
      if (i == "save") {
        vm.$router.push("/show-area");
      }
    },
    removecassava(index) {
      console.log(index + 1);
      this.xdata.splice(index,1)
    },
    addcassava(){
      this.xdata.push({
        id: this.xdata.length+1,
        x1: 0,
        x2: 0,
        x3: 0,
        x4: 0,
        x5: 0,
        x6: 0,
        temputure: 0,})
    },
    deletearea() {
      //เอา ID ของหมุดไปลบออกจาก Database แล้วกลับไปหน้า Showarea
      const vm = this;
      vm.$router.push("/show-area");
    },
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },
    changepositionmap(newlat, newlng) {
      this.mapcenter.lat = Number(newlat);
      this.mapcenter.lng = Number(newlng);
      this.datapin[0].position.lat = Number(newlat);
      this.datapin[0].position.lng = Number(newlng);
  },
  }
};
</script>
<style scoped>
#backbutton {
  background-color: #f2f2f2;
}
#savebutton {
  background-color: #1ce227;
}
#removebutton {
  background-color: #e21c1c;
}
#table {
  padding-bottom: 2vh;
  padding-top: 2vh;
}
#indexhead {
  padding-right: 2vw;
}
</style>