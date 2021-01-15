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
          ><v-btn id="addbutton" rounded @click="moveto('pin')"
            >+ เพิ่มข้อมูลมันสำปะหลัง</v-btn
          ></v-col
        >
        <v-col cols="12" md="2" sm="3" class="text-center"> </v-col>
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
              @input="menu2 = false"
            ></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
      <v-row id="everythingisonfire">
        <v-col cols="12" md="9">
          <gmap-map
            ref="mapRef"
            :center="mapcenter"
            :zoom="17"
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
          <v-row align="center">
            <v-col cols="12" md="3" sm="3"
              ><v-img id="pin" src="../assets/Agradeicon.png"></v-img></v-col
            >เกรด A</v-row
          >
          <v-row align="center">
            <v-col cols="12" md="3" sm="3"
              ><v-img id="pin" src="../assets/Bgradeicon.png"></v-img></v-col
            >เกรด B</v-row
          >
          <v-row align="center">
            <v-col cols="12" md="3" sm="3"
              ><v-img id="pin" src="../assets/Cgradeicon.png"></v-img></v-col
            >เกรด C</v-row
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
          <v-btn id="backbutton" rounded @click="moveto('back')"
            >ย้อนกลับ</v-btn
          >
          <v-btn color="#FFB200" rounded @click="moveto('editarea')"
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
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    iconsetting: {
      url: require("../assets/Agradeicon.png"),
      size: { width: 46, height: 46, f: "px", b: "px" },
      scaledSize: { width: 23, height: 28, f: "px", b: "px" },
    },
    agreenmarker: "../assets/Agradeicon.png",
    byellowmarker: "../assets/Bgradeicon.png",
    credmarker: "../assets/Cgradeicon.png",
    gradeAtotal: 10,
    gradeBtotal: 50,
    gradeCtotal: 40,
    totalstarch: 50,
    mvcPath: null,
    mapcenter: { lat: 16.466022, lng: 102.898313 },
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
  async created() {
    this.fetchdatafromdatabase();
  },
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
  updated() {
    this.totalstarchfinder();
  },
  mounted() {
    this.totalstarchfinder();
  },
  methods: {
    fetchdatafromdatabase() {
      var avgstarch = 0;
      var starch = 0;
      var lengthstach = 0;
      var m = 0;
      var i = 0;
      var cassavaareaidlist = [];
      var datadetail = [];
      this.datapin = [];
      this.markers = [];
      axios
        .get("http://127.0.0.1:8000/area-check/")
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
          this.mapcenter = cassavaareaidlist[0].position
        })
        .catch((err) => {
          console.error(err);
        });
      axios
        .get("http://127.0.0.1:8000/cassava-check/")
        .then((response) => {
          i = 0;
          while (i < cassavaareaidlist.length) {
            var listcassava = [];
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
                listcassava.push({
                  dategetdata,
                  starchPercentage,
                  humidity,
                  temperature,
                });
              }
              m++;
            }
            cassavaareaidlist[i].datadetail = listcassava;
            if(cassavaareaidlist[i].datadetail.length !== 0 ){
              cassavaareaidlist[i].avgstarch = starch / lengthstach;
            }
            starch = 0;
            lengthstach = 0;
            i++;
          }
           console.log(cassavaareaidlist)
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
          scaledSize: { width: 23, height: 40, f: "px", b: "px" },
        };
      } else if (colormarker == "yellow") {
        return {
          url: require("../assets/Bgradeicon.png"),
          scaledSize: { width: 23, height: 40, f: "px", b: "px" },
        };
      } else if (colormarker == "red") {
        return {
          url: require("../assets/Cgradeicon.png"),
          scaledSize: { width: 23, height: 40, f: "px", b: "px" },
        };
      }
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
  size: 10px;
  line-height: 2.5;
}
#showmap {
  width: 100%;
  height: 100%;
}
#pin {
  max-width: 1vw;
  min-width: 1vw;
  max-height: 4vh;
  min-height: 4vh;
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
</style>