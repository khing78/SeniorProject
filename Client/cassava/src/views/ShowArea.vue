<template>
  <v-main id="show-area">
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <div id="namearea">แปลง {{ areaname }}</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="2" sm="3"
          ><v-btn
            id="addbutton"
            rounded
            @click="moveto('pin')"
            style="font-size: 18px"
            >+ เพิ่มข้อมูลมันสำปะหลัง</v-btn
          ></v-col
        >
        <v-col cols="12" md="2" sm="3" class="text-center"></v-col>
        <v-col cols="12" md="2" sm="3">
          <v-menu
            :close-on-content-click="true"
            :nudge-right="40"
            transition="scale-transition"
            offset-y
            min-width="290px"
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
              @input="changedatemarker(),menu2 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="12" md="4" sm="3">
          <v-btn id="selectdatebutton" rounded @click="resetsearch()"
            >ทั้งหมด</v-btn
          >
        </v-col>
      </v-row>
      <v-row id="everythingisonfire">
        <v-col cols="12" md="9">
          <gmap-map
            ref="mapRef"
            :center="mapcenter"
            :zoom="17"
            :options="{
              styles: hide,
            }"
            style="width: 100%; height: 500px"
            map-type-id="terrain"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :icon="changeocolormarker(m.avgstarch)"
              @click="moveto(m.cassavaareaid)"
            ></gmap-marker>
            <gmap-polyline
              v-if="path.length > 0"
              :path="path"
              :editable="false"
              ref="polyline"
            >
            </gmap-polyline>
          </gmap-map>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="3" sm="12">
          <v-row>
            <v-col cols="12" md="3" sm="3" id="framepinimg"
              ><v-img id="pin" src="../assets/Agradeicon.png"></v-img
            ></v-col>
            <div id="detailgrade">เกรด A</div></v-row
          >
          <v-row>
            <v-col cols="12" md="3" sm="3" id="framepinimg"
              ><v-img id="pin" src="../assets/Bgradeicon.png"></v-img
            ></v-col>
            <div id="detailgrade">เกรด B</div></v-row
          >
          <v-row>
            <v-col cols="12" md="3" sm="3" id="framepinimg"
              ><v-img id="pin" src="../assets/Cgradeicon.png"></v-img
            ></v-col>
            <div id="detailgrade">เกรด C</div></v-row
          >
          <div id="detailtext">
            คุณภาพโดยรวมทั้งแปลง
            <br />
            เกรด A: {{ gradeAtotal }} %
            <br />
            เกรด B: {{ gradeBtotal }} %
            <br />
            เกรด C: {{ gradeCtotal }} %
            <br />
            เปอร์เซ็นต์แป้งโดยเฉลี่ย
            <br />
            {{ totalstarch }} %
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn
            id="backbutton"
            rounded
            @click="moveto('back')"
            style="font-size: 18px"
            >ย้อนกลับ</v-btn
          >
          <v-btn
            color="#FFB200"
            rounded
            @click="moveto('editarea')"
            style="font-size: 18px"
            >จัดการแปลง</v-btn
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
    hide: [
      {
        featureType: "poi",
        stylers: [{ visibility: "off" }],
      },
      {
        featureType: "transit",
        elementType: "labels.icon",
        stylers: [{ visibility: "off" }],
      },
    ],
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    gradeAtotal: 10,
    gradeBtotal: 50,
    gradeCtotal: 40,
    totalstarch: 50,
    mdk: [],
    datapin: [
      {
        id: 0,
        position: { lat: 16.465522, lng: 102.898513 },
        dategetdata: "2020-12-26",
        qulitypercent: 31,
      },
      {
        id: 1,
        position: { lat: 16.465822, lng: 102.898513 },
        dategetdata: "2020-12-24",
        qulitypercent: 25,
      },
      {
        id: 2,
        position: { lat: 16.465522, lng: 102.898913 },
        dategetdata: "2020-12-22",
        qulitypercent: 19,
      },
    ],
    markers: [
      // Marker เป็นตัวบอกคุณภาพ
      // ดึงข้อมูลมาจากฐานข้อมูล
      {
        id: 0,
        position: { lat: 16.465522, lng: 102.898513 },
        dategetdata: "2020-12-26",
        qulitypercent: 31,
      },
      {
        id: 1,
        position: { lat: 16.465822, lng: 102.898513 },
        dategetdata: "2020-12-24",
        qulitypercent: 25,
      },
      {
        id: 2,
        idarea: "awfwafaw",
        position: { lat: 16.465522, lng: 102.898913 },
        dategetdata: "2020-12-22",
        qulitypercent: 19,
      },
    ],
  }),
  updated() {
    this.totalstarchfinder();
  },
  created() {
    if (this.newidfarm == "") {
      this.$router.push("/show-all-area");
    }
    this.fetchdatafromdatabase();
  },
  computed: {
    ...mapGetters({
      newidfarm: "getIdFarm",
      areaname: "getNameArea",
      path: "getPath",
      mapcenter: "getPosition",
    }),
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
  },
  methods: {
    async fetchdatafromdatabase() {
      var avgstarch = 0;
      var starch = 0;
      var lengthstach = 0;
      var m = 0;
      var i = 0;
      var cassavaareaidlist = [];
      var datadetail = [];
      this.datapin = [];
      this.markers = [];
      await axios
        .get("http://143.198.205.220:8000/area-check/")
        .then((response) => {
          var i = 0;
          while (i < response.data.length) {
            if (response.data[i].farm_store == this.newidfarm) {
              var cassavaareaid = response.data[i].cassava_area_id;
              var position = {
                lat: Number(response.data[i].tree_latitude),
                lng: Number(response.data[i].tree_longtitude),
              };
              cassavaareaidlist.push({
                cassavaareaid,
                position,
                datadetail,
                avgstarch,
              });
            }
            i++;
          }
        })
        .catch((err) => {
          console.error(err);
        });
      var newlistdata = [];
      await axios
        .get("http://143.198.205.220:8000/cassava-check/")
        .then((response) => {
          i = 0;
          while (i < cassavaareaidlist.length) {
            newlistdata = [];
            m = 0;
            while (m < response.data.length) {
              if (
                response.data[m].cassava_area ==
                cassavaareaidlist[i].cassavaareaid
              ) {
                var dategetdata = response.data[m].check_date.slice(0, 10);
                var starchPercentage = response.data[m].starchPercentage;
                var humidity = response.data[m].humidity;
                var temperature = response.data[m].temperature;
                starch += response.data[m].starchPercentage;
                lengthstach++;
                newlistdata.push({
                  dategetdata,
                  starchPercentage,
                  humidity,
                  temperature,
                });
                this.date = dategetdata
              }
              m++;
            }
            cassavaareaidlist[i].datadetail = newlistdata;
            if (cassavaareaidlist[i].datadetail.length != 0) {
              cassavaareaidlist[i].avgstarch = starch / lengthstach;
            }
            starch = 0;
            lengthstach = 0;
            i++;
          }
        })
        .catch((err) => {
          console.error(err);
        });
      this.$store.commit({
        type: "setDetailArea",
        detailarea: cassavaareaidlist,
      });
      this.datapin = cassavaareaidlist;
      this.markers = cassavaareaidlist;
      console.log(this.markers);
      this.changedatemarker();
    },
    changedatemarker() {
      var i;
      var m;
      var newavgstarch;
      var datainside = [];
      this.markers = [];
      for (i = 0; i < this.datapin.length; i++) {
        datainside = [];
        newavgstarch = 0;
        for (m = 0; m < this.datapin[i].datadetail.length; m++) {
          if (this.datapin[i].datadetail[m].dategetdata == this.date) {
            datainside.push(this.datapin[i].datadetail[m]);
            newavgstarch += this.datapin[i].datadetail[m].starchPercentage;
          }
        }
        if (datainside.length != 0) {
          var cassavaareaid = this.datapin[i].cassavaareaid;
          var position = this.datapin[i].position;
          var datadetail = datainside;
          var avgstarch = newavgstarch / datainside.length;
          this.markers.push({ avgstarch, datadetail, position, cassavaareaid });
        }
      }
    },
    totalstarchfinder() {
      var i = 0;
      var totalqulity = 0;
      var red = 0;
      var yellow = 0;
      var green = 0;
      if (this.markers.length == 0) {
        this.gradeAtotal = 0;
        this.gradeBtotal = 0;
        this.gradeCtotal = 0;
        this.totalstarch = 0;
      } else {
        while (i < this.markers.length) {
          totalqulity += this.markers[i].avgstarch;
          if (this.markers[i].avgstarch < 25) {
            red++;
          } else if (this.markers[i].avgstarch < 30) {
            yellow++;
          } else if (this.markers[i].avgstarch >= 30) {
            green++;
          }
          i++;
        }
        this.gradeAtotal = ((green * 100) / this.markers.length).toFixed(2);
        this.gradeBtotal = ((yellow * 100) / this.markers.length).toFixed(2);
        this.gradeCtotal = ((red * 100) / this.markers.length).toFixed(2);
        this.totalstarch = (totalqulity / this.markers.length).toFixed(2);
      }
    },
    changeocolormarker(qulity) {
      var colormarker = "";
      if (qulity < 25) {
        colormarker = "red";
      } else if (qulity < 30) {
        colormarker = "yellow";
      } else if (qulity >= 30) {
        colormarker = "green";
      }
      if (colormarker == "green") {
        return {
          url: require("../assets/Agradeicon.png"),
          scaledSize: { width: 28, height: 60, f: "px", b: "px" },
        };
      } else if (colormarker == "yellow") {
        return {
          url: require("../assets/Bgradeicon.png"),
          scaledSize: { width: 28, height: 60, f: "px", b: "px" },
        };
      } else if (colormarker == "red") {
        return {
          url: require("../assets/Cgradeicon.png"),
          scaledSize: { width: 28, height: 60, f: "px", b: "px" },
        };
      }
    },
    resetsearch() {
      this.markers = this.datapin;
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },
    moveto(i) {
      const vm = this;
      if (i == "pin") {
        vm.$store.commit({
          type: "setEditMode",
          editmode: false,
        });
        vm.$router.push("/data-save");
      } else if (i == "addarea") {
        vm.$router.push("/add-area");
      } else if (i == "editarea") {
        vm.$router.push("/edit-area");
      } else if (i == "back") {
        vm.$router.push("/show-all-area");
      } else if (i == "chart") {
        vm.$router.push("/area-detail-chart");
      } else {
        vm.$store.commit({
          type: "setSelectedArea",
          selectedarea: i,
        });
        vm.$store.commit({
          type: "setSelectedDate",
          selecteddate: this.date,
        });
        vm.$router.push("/pin-detail");
      }
    },
  },
};
</script>
<style scoped>
#detailtext {
  text-align: center;
  font-size: 20px;
  line-height: 2.5;
}
#showmap {
  width: 100%;
  height: 100%;
}
#pin {
  max-width: 30px;
  min-width: 18px;
  max-height: 70px;
  min-height: 23px;
}
#backbutton {
  margin-right: 1vw;
  border-radius: 10vh;
}
#addbutton {
  background-color: #1ce227;
}
#marginaddbutton {
  margin-right: 1vw;
}
#selectdatebutton {
  margin-right: 1vw;
  margin-bottom: 1vh;
}
#detailgrade {
  font-size: 18px;
  padding: 3vh;
}
#framepinimg {
  height: 1vh;
  width: 1vw;
}
#namearea {
  font-size: 28px;
}
</style>