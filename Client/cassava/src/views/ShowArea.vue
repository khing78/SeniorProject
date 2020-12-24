<template>
  <v-main id="show-area">
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <div id="namearea">แปลง {{ areaname }}</div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="4" sm="4"
          ><v-btn id="addbutton" rounded @click="moveto('pin')"
            >+ เพิ่มข้อมูลมันสำปะหลัง</v-btn
          ></v-col
        >
        <v-col cols="12" md="3" sm="3">
          <v-btn rounded @click="moveto('chart')">กราฟ</v-btn>
        </v-col>
        <v-col cols="12" md="3" sm="3">
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
              :draggable="false"
              @click="moveto('pindetail')"
            ></gmap-marker>
            <gmap-polyline
              v-if="path.length > 0"
              :path="path"
              :editable="false"
              @path_changed="updateEdited($event)"
              @rightclick="handleClickForDelete"
              ref="polyline"
            >
            </gmap-polyline>
          </gmap-map>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-row align="center">
            <v-col cols="3"
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
            เปอร์เซ็นต์แปลงโดยเฉลี่ย
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
    areaname: "สมชาย",
    gradeAtotal: 10,
    gradeBtotal: 50,
    gradeCtotal: 40,
    totalstarch: 50,
    path: [
      { lat: 16.466022, lng: 102.899313 },
      { lat: 16.466022, lng: 102.898313 },
      { lat: 16.465022, lng: 102.898313 },
    ],
    mvcPath: null,
    mapcenter: { lat: 16.466022, lng: 102.898313 },
    markers: [
      // Marker เป็นตัวบอกคุณภาพ
      // ดึงข้อมูลมาจากฐานข้อมูล
      {
        Id: 1,
        name: "1",
        position: { lat: 16.465522, lng: 102.898513 },
        wide: 100,
        long: 100,
      },
    ],
  }),
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
    polylinePath() {
      if (!this.mvcPath) return null;

      let path = [];
      for (let j = 0; j < this.mvcPath.getLength(); j++) {
        let point = this.mvcPath.getAt(j);
        path.push({ lat: point.lat(), lng: point.lng() });
      }
      return path;
    },
  },
  methods: {
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
    updateCenter: function (place) {
      this.center = {
        lat: place.geometry.location.lat(),
        lng: place.geometry.location.lng(),
      };
    },
    handleClickForDelete($event) {
      if ($event.vertex) {
        
        this.$refs.polyline.$polylineObject
          .getPaths()
          .getAt($event.path)
          .removeAt($event.vertex);
      }
    },
    updateEdited: function (mvcPath) {
      this.mvcPath = mvcPath;
    },
    readGeojson: function ($event) {
      try {
        this.polylineGeojson = $event.target.value;

        var v = JSON.parse($event.target.value);

        this.path = v.coordinates.map(([lng, lat]) => ({ lat, lng }));

        this.errorMessage = null;
      } catch (err) {
        this.errorMessage = err.message;
      }
    },
  },
  mounted() {
    //this Code not depandent in Mark map (can delete if you want)
    /*this.$refs.mapRef.$mapPromise.then((map) => {
      map.panTo({ lat: 1.38, lng: 103.8 });
    });*/
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
</style>