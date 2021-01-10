<template>
  <v-main id="show-area">
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <div id="namearea">แปลง {{ areaname }}</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="3" sm="3"
          ><v-btn id="addbutton" rounded @click="moveto('pin')"
            >+ เพิ่มข้อมูลมันสำปะหลัง</v-btn
          ></v-col
        >
        <v-col cols="12" md="3" sm="3" class="text-center">
          <v-btn rounded @click="moveto('chart')">กราฟ</v-btn>
        </v-col>
        <v-col cols="12" md="2" sm="2">
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
        <v-col cols="12" md="3" sm="3">
          <v-btn
            rounded
            id="selectdatebutton"
            @click="changedate(computedDateFormatted)"
          >
            ค้นหา
          </v-btn>
          <v-btn rounded id="showallpin" @click="showallpindate()">
            ทั้งหมด
          </v-btn>
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
              :icon="changeocolormarker(m.qulitypercent)"
              @click="moveto('pindetail')"
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
        <v-col cols="12" md="3" sm="3">
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
    areaname: "สมชาย",
    gradeAtotal: 10,
    gradeBtotal: 50,
    gradeCtotal: 40,
    totalstarch: 50,
    path: [
      //ดึงข้อมูลจากฐานข้อมูล วาดรูปแปลง
      { lat: 16.466022, lng: 102.898313 },
      { lat: 16.465022, lng: 102.898313 },
      { lat: 16.465022, lng: 102.899313 },
      { lat: 16.466022, lng: 102.899313 },
      { lat: 16.466022, lng: 102.898313 },
    ],
    mvcPath: null,
    mapcenter: { lat: 16.466022, lng: 102.898313 },
    datapin: [
      {
        id: 0,
        position: { lat: 16.465522, lng: 102.898513 },
        dategetdata: "26/12/2563",
        qulitypercent: 31,
      },
      {
        id: 1,
        position: { lat: 16.465822, lng: 102.898513 },
        dategetdata: "24/12/2563",
        qulitypercent: 25,
      },
      {
        id: 2,
        position: { lat: 16.465522, lng: 102.898913 },
        dategetdata: "22/12/2563",
        qulitypercent: 19,
      },
    ],
    markers: [
      // Marker เป็นตัวบอกคุณภาพ
      // ดึงข้อมูลมาจากฐานข้อมูล
      {
        id: 0,
        position: { lat: 16.465522, lng: 102.898513 },
        dategetdata: "26/12/2563",
        qulitypercent: 31,
      },
      {
        id: 1,
        position: { lat: 16.465822, lng: 102.898513 },
        dategetdata: "26/12/2563",
        qulitypercent: 25,
      },
      {
        id: 2,
        position: { lat: 16.465522, lng: 102.898913 },
        dategetdata: "26/12/2564",
        qulitypercent: 19,
      },
    ],
  }),
  computed: {
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
    totalstarchfinder() {
      var i = 0;
      var totalqulity = 0;
      var red = 0
      var yellow = 0
      var green = 0
      if (this.markers.length == 0){
        this.gradeAtotal = 0
        this.gradeBtotal = 0
        this.gradeCtotal = 0
        this.totalstarch = 0
      }else {
        while (i < this.markers.length) {
        totalqulity += this.markers[i].qulitypercent;
        if (this.markers[i].qulitypercent < 25) {
          red++
        } else if (this.markers[i].qulitypercent < 30) {
          yellow++
        } else if (this.markers[i].qulitypercent >= 30) {
          green++
        }
        i++;
      }
      this.gradeAtotal = (green*100/this.markers.length).toFixed(2)
      this.gradeBtotal = (yellow*100/this.markers.length).toFixed(2)
      this.gradeCtotal = (red*100/this.markers.length).toFixed(2)
      this.totalstarch = (totalqulity / this.markers.length).toFixed(2)
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
      } else if (i == "pindetail") {
        vm.$router.push("/pin-detail");
      }
    },
    changedate(selectdate) {
      var i = 0;
      this.markers = [];
      while (i < this.datapin.length) {
        if (this.datapin[i].dategetdata == selectdate) {
          this.markers.push(this.datapin[i]);
        }
        i++;
      }
    },
    showallpindate() {
      this.markers = this.datapin;
    },
  },
};
</script>
<style scoped>
#detailtext {
  text-align: center;
  size: 10px;
}
#showmap {
  width: 100%;
  height: 100%;
}
#pin {
  max-width: 1vw;
  min-width: 1vw;
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