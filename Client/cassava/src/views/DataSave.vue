<template>
  <v-main class="data-save">
    <v-container>
      <v-row>
        <v-col cols="12" md="3" sm="3"> ข้อมูลผลตรวจคุณภาพ</v-col>
        <v-col class="text-right">
          <v-btn
            id="removebutton"
            rounded
            @click="deleteArea()"
            :disabled="deletebuttonmode"
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
            v-model="latposition"
            hint="กรุณาใส่ละติจูด"
            label="ละติจูด"
          ></v-text-field
        ></v-col>
        <v-col cols="12" md="3" sm="3"
          ><v-text-field
            v-model="lngposition"
            hint="กรุณาใส่ลองจิจูด"
            label="ลองจิจูด"
          ></v-text-field
        ></v-col>
        <v-col cols="12" md="3" sm="3"
          ><v-btn
            id="setmodebutton"
            rounded
            @click="changeMode()"
            :disabled="buttonmode"
            >{{ modename }}</v-btn
          ></v-col
        >
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
              :clickable="clickmode"
              :draggable="dragemode"
              :icon="selectedMarkerIcon(m.iconmarker)"
              @dragend="
                changePositionMap($event.latLng.lat(), $event.latLng.lng())
              "
              @click="selectMode(index)"
            ></gmap-marker>
          </gmap-map>
        </v-col>
        <v-col cols="12">
          <v-btn id="savebutton" rounded @click="addCassava()"
            >เพิ่มหัวมันสำปะหลัง +</v-btn
          >
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
                      @click="removeCassava(index)"
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
          <v-btn
            id="backbutton"
            rounded
            @click="moveTo('back')"
            style="font-size: 18px"
            >ยกเลิก</v-btn
          >
        </v-col>
        <v-col class="text-right">
          <v-btn
            id="savebutton"
            rounded
            @click="moveTo('save'), sendData()"
            style="font-size: 18px"
            >บันทึก</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>
<script>
import axios from "axios";
import { mapGetters } from "vuex";

export default {
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    selectedidarea: "",
    mode: 1,
    menu: false,
    modal: false,
    menu2: false,
    buttonmode: false,
    deletebuttonmode: true,
    clickmode: true,
    modename: "ตั้งต้นใหม่",
    dragemode: false,
    alreadyhaveid: [],
    deletecassavaid: [],
    lenghtofarea: 5,
    latposition: 0,
    lngposition: 0,
    mapcenter: { lat: 16.466022, lng: 102.898313 },
    datapin: [
      // ดึงข้อมูลมาจากฐานข้อมูล
      {
        id: 0,
        position: { lat: 16.466022, lng: 102.898313 },
      },
    ],
    xdata: [
      /*
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
      },*/
    ],
  }),
  computed: {
    ...mapGetters({
      idfarm: "getIdFarm",
      areaname: "getNameArea",
      path: "getPath",
      positionarea: "getPosition",
      editmode: "getEditMode",
      selectedarea: "getSelectedArea",
      selectdate: "getSelectedDate",
    }),
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },
  created() {
    if (this.newidfarm == ""){
        this.$router.push("/show-all-area");
      }
    if (this.editmode == false) {
      this.deletebuttonmode = true;
      this.createNewCassava();
    } else 
    if (this.editmode == true){
      this.mode = 3;
      this.buttonmode = true
      this.deletebuttonmode = false;
      this.starteditCassava();
    }
  },
  methods: {
    async createNewCassava() {
      this.mapcenter = this.positionarea;
      var i = 0;
      var newpindata = [];
      await axios
        .get("http://127.0.0.1:8000/area-check/")
        .then((response) => {
          while (i < response.data.length) {
            if (response.data[i].farm_store == this.idfarm) {
              var idarea = response.data[i].cassava_area_id;
              var position = {
                lat: Number(response.data[i].tree_latitude),
                lng: Number(response.data[i].tree_longtitude),
              };
              var iconmarker = "";
              newpindata.push({ idarea, position, iconmarker });
            }
            i++;
          }
          if (newpindata.length == 0) {
            this.datapin = [
              {
                id: 0,
                position: { lat: this.mapcenter.lat, lng: this.mapcenter.lng },
                iconmarker: "",
              },
            ];
            this.buttonmode = true;
            this.changeMode();
          } else {
            this.datapin = newpindata;
            this.latposition = this.datapin[0].position.lat;
            this.lngposition = this.datapin[0].position.lng;
            this.datapin[0].iconmarker = "selected";
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    async starteditCassava() {
      this.date = this.selectdate;
      this.dragemode = true;
      var i = 0;
      var newpindata = [];
      await axios.get("http://127.0.0.1:8000/area-check/").then((response) => {
        while (i < response.data.length) {
          if (response.data[i].cassava_area_id == this.selectedarea) {
            var idarea = response.data[i].cassava_area_id;
            var position = {
              lat: Number(response.data[i].tree_latitude),
              lng: Number(response.data[i].tree_longtitude),
            };
            var iconmarker = "";
            newpindata.push({ idarea, position, iconmarker });
          }
          i++;
        }
        console.log(position.lat);
        this.latposition = position.lat;
        this.lngposition = position.lng;
        this.mapcenter = position;
        this.datapin = newpindata;
      });
      i = 0;
      var newxdata = [];
     await axios
        .get("http://127.0.0.1:8000/cassava-check/")
        .then((response) => {
          while (i < response.data.length) {
            if (
              response.data[i].cassava_area == this.selectedarea &&
              response.data[i].check_date.substr(0, 10) == this.selectdate
            ) {
              var id = response.data[i].id;
              var x1 = response.data[i].spectrum1;
              var x2 = response.data[i].spectrum2;
              var x3 = response.data[i].spectrum3;
              var x4 = response.data[i].spectrum4;
              var x5 = response.data[i].spectrum5;
              var x6 = response.data[i].spectrum6;
              var temputure = response.data[i].temperature;
              var humidity = response.data[i].humidity;
              this.alreadyhaveid.push(id);
              newxdata.push({
                id,
                x1,
                x2,
                x3,
                x4,
                x5,
                x6,
                temputure,
                humidity,
              });
            }
            i++;
          }
          this.xdata = newxdata;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    changeMode() {
      if (this.mode == 1) {
        this.mode = 2;
        this.clickmode = false;
        this.dragemode = true;
        this.modename = "เพิ่มจากต้นเดิม";
        this.latposition = this.positionarea.lat;
        this.lngposition = this.positionarea.lng;
        this.datapin = [
          {
            id: 0,
            position: {
              lat: this.positionarea.lat,
              lng: this.positionarea.lng,
            },
            iconmarker: "",
          },
        ];
        this.selectedidarea = "";
        this.mapcenter = this.positionarea;
      } else {
        this.mode = 1;
        this.latposition = this.datapin[0].position.lat;
        this.lngposition = this.datapin[0].position.lng;
        this.createNewCassava();
        this.clickmode = true;
        this.dragemode = false;
        this.modename = "ตั้งต้นใหม่";
      }
    },
    selectMode(i) {
      if (this.mode == 1) {
        this.selectArea(i);
      }
    },
    selectedMarkerIcon(iconmarker) {
      if (iconmarker == "selected") {
        return {
          url: require("../assets/Agradeicon.png"),
          scaledSize: { width: 28, height: 60, f: "px", b: "px" },
        };
      } else {
        return {
          url: require("../assets/Cgradeicon.png"),
          scaledSize: { width: 28, height: 60, f: "px", b: "px" },
        };
      }
    },
    selectArea(i) {
      var q = 0;
      this.selectedidarea = this.datapin[i].idarea;
      this.latposition = this.datapin[i].position.lat;
      this.lngposition = this.datapin[i].position.lng;
      while (q < this.datapin.length) {
        this.datapin[q].iconmarker = "";
        q++;
      }
      this.datapin[i].iconmarker = "selected";
      this.$store.commit({
        type: "setIdArea",
        idarea: this.datapin[i].idarea,
      });
    },
   async saveEditCassava() {
      var i = 0;
      var g = 0;
      var p = 0;
     await axios
        .put("http://127.0.0.1:8000/area-check/" + this.selectedarea + "/", {
          farm_store: this.idfarm,
          starch_percentage: 45,
          tree_latitude: this.latposition,
          tree_longtitude: this.lngposition,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      while (i < this.xdata.length) {
        p = 0;
        g = 0;
        while (g < this.alreadyhaveid.length) {
          if (this.xdata[i].id == this.alreadyhaveid[g]) {
           await axios
              .put(
                "http://127.0.0.1:8000/cassava-check/" + this.xdata[i].id + "/",
                {
                  cassava_area: this.selectedarea,
                  check_date: this.date,
                  latitude: this.latposition,
                  longtitude: this.lngposition,
                  spectrum1: this.xdata[i].x1,
                  spectrum2: this.xdata[i].x2,
                  spectrum3: this.xdata[i].x3,
                  spectrum4: this.xdata[i].x4,
                  spectrum5: this.xdata[i].x5,
                  spectrum6: this.xdata[i].x6,
                  temperature: this.xdata[i].temputure,
                  starchPercentage: "25",
                  humidity: this.xdata[i].humidity,
                }
              )
              .then((response) => {
                console.log(response);
              })
              .catch((error) => {
                console.log(error);
              });
            p = 1;
          }
          g++;
        }
        if (p == 0) {
         await axios
            .post("http://127.0.0.1:8000/cassava-check/", {
              cassava_area: this.selectedarea,
              check_date: this.date,
              latitude: this.latposition,
              longtitude: this.lngposition,
              spectrum1: this.xdata[i].x1,
              spectrum2: this.xdata[i].x2,
              spectrum3: this.xdata[i].x3,
              spectrum4: this.xdata[i].x4,
              spectrum5: this.xdata[i].x5,
              spectrum6: this.xdata[i].x6,
              temperature: this.xdata[i].temputure,
              starchPercentage: "25",
              humidity: this.xdata[i].humidity,
            })
            .catch((error) => {
              console.log(error);
            });
        }
        i++;
      }
      var m = 0;
      console.log(this.deletecassavaid)
      while (m < this.deletecassavaid.length) {
        axios.delete(
          "http://127.0.0.1:8000/cassava-check/" + this.deletecassavaid[m] + "/",
          {}
        );
        m++;
      }
    },
   async addNewArea() {
      console.log("//////////////////////" + this.idfarm);
     await axios
        .post("http://127.0.0.1:8000/area-check/", {
          farm_store: this.idfarm,
          starch_percentage: 45,
          tree_latitude: this.latposition,
          tree_longtitude: this.lngposition,
        })
        .then((response) => {
          this.selectedidarea = response.data.cassava_area_id;
          var i = 0;
          while (i < this.xdata.length) {
            axios
              .post("http://127.0.0.1:8000/cassava-check/", {
                cassava_area: this.selectedidarea,
                check_date: this.date,
                latitude: this.latposition,
                longtitude: this.lngposition,
                spectrum1: this.xdata[i].x1,
                spectrum2: this.xdata[i].x2,
                spectrum3: this.xdata[i].x3,
                spectrum4: this.xdata[i].x4,
                spectrum5: this.xdata[i].x5,
                spectrum6: this.xdata[i].x6,
                temperature: this.xdata[i].temputure,
                starchPercentage: "25",
                humidity: this.xdata[i].humidity,
              })
              .catch((error) => {
                console.log(error);
              });
            i++;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async postData() {
      var i = 0;
      while (i < this.xdata.length) {
       await axios
          .post("http://127.0.0.1:8000/cassava-check/", {
            cassava_area: this.selectedidarea,
            check_date: this.date,
            latitude: this.latposition,
            longtitude: this.lngposition,
            spectrum1: this.xdata[i].x1,
            spectrum2: this.xdata[i].x2,
            spectrum3: this.xdata[i].x3,
            spectrum4: this.xdata[i].x4,
            spectrum5: this.xdata[i].x5,
            spectrum6: this.xdata[i].x6,
            temperature: this.xdata[i].temputure,
            starchPercentage: "25",
            humidity: this.xdata[i].humidity,
          })
          .catch((error) => {
            console.log(error);
          });
        i++;
      }
    },
    sendData() {
      if (this.mode == 2) {
        this.addNewArea();
      } else if (this.mode == 3) {
        this.saveEditCassava();
      } else {
        this.postData();
      }
        this.$router.push("/show-area");
    },
    moveTo(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/show-area");
      }
    },
    removeCassava(index) {
      this.deletecassavaid.push(this.xdata[index].id);
      console.log(index + 1);
      this.xdata.splice(index, 1);
    },
    addCassava() {
      this.xdata.push({
        x1: 0,
        x2: 0,
        x3: 0,
        x4: 0,
        x5: 0,
        x6: 0,
        temputure: 0,
      });
    },
    deleteArea() {
      //เอา ID ของหมุดไปลบออกจาก Database แล้วกลับไปหน้า Showarea
      axios.delete(
          "http://127.0.0.1:8000/area-check/" + this.selectedarea + "/",
          {}
        );
      const vm = this;
      vm.$router.push("/show-area");
    },
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },
    changePositionMap(newlat, newlng) {
      this.mapcenter.lat = Number(newlat);
      this.mapcenter.lng = Number(newlng);
      this.latposition = Number(newlat);
      this.lngposition = Number(newlng);
    },
  },
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