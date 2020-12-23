<template>
  <v-main class="edit-area">
    <v-container>
      <v-btn id="deletebutton" @click="deletearea()">ลบแปลง</v-btn>
      <v-row>
        <v-col cols="12" md="9" sm="9">
          <gmap-map
            :center="mapcenter"
            :zoom="18"
            style="width: 100%; height: 500px"
            map-type-id="terrain"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="false"
              :draggable="true"
              @click="center = m.position"
            ></gmap-marker>
            <gmap-polyline
              v-if="newpath.length > 0"
              :path="newpath"
              :editable="false"
              ref="polyline"
            >
            </gmap-polyline>
          </gmap-map>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="3" sm="3">
          <v-text-field
            v-model="areaname"
            hint="กรุณาใส่ชื่อแปลง"
            label="ชื่อแปลง"
          ></v-text-field>
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
                label="วัน/เดือน/ปี ที่เริ่มปลูก"
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
          <v-row>
            <v-container fluid>
              <v-row>
                <v-col>
                  <v-combobox
                    v-model="selectprovince"
                    :items="province"
                    label="จังหวัด"
                    outlined
                    dense
                  ></v-combobox>
                  <v-combobox
                    v-model="selectdistrict"
                    :items="itemsdistrict"
                    label="อำเภอ"
                    outlined
                    dense
                  ></v-combobox>
                </v-col>
              </v-row>
            </v-container>
          </v-row>
          <v-text-field
            v-model="mapcenter.lat"
            hint="กรุณาใส่ละติจูด"
            label="ละติจูด"
          ></v-text-field>
          <v-text-field
            v-model="mapcenter.lng"
            hint="กรุณาใส่ลองจิจูด"
            label="ลองจิจูด"
          ></v-text-field>
          <v-text-field
            v-model="mapcenter.wide"
            hint="กรุณาใส่ความกว้าง"
            label="ความกว้าง"
          ></v-text-field>
          <v-text-field
            v-model="mapcenter.long"
            hint="กรุณาใส่ความยาว"
            label="ความยาว"
          ></v-text-field>
          <v-col cols="12">
            <v-btn
              @click="
                changepositionmap(
                  mapcenter.lat,
                  mapcenter.lng,
                  mapcenter.wide,
                  mapcenter.long
                )
              "
              >ตั้งจุดใหม่</v-btn
            >
          </v-col>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn id="backbutton" rounded @click="moveto('back')"
            >ย้อนกลับ</v-btn
          >
          <v-btn id="savebutton" rounded @click="savedata()">บันทึก</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    mapcenter: { lat: 16.466022, lng: 102.898313, wide: 100, long: 100 },
    newpath: [
      { lat: 16.466022, lng: 102.899313 },
      { lat: 16.466022, lng: 102.898313 },
      { lat: 16.465022, lng: 102.898313 },
    ],
    path: [
      //ดึงข้อมูลจากDatabase มา
      { lat: 16.466022, lng: 102.899313 },
      { lat: 16.466022, lng: 102.898313 },
      { lat: 16.465022, lng: 102.898313 },
    ],
    areaname: "สมชาย",
    selectprovince: "ขอนแก่น",
    selectdistrict: "บ้านแฮด",
    itemsdistrict: ["เมือง", "เวียงเก่า", "บ้านแฮด", "บ้านฝาง"],
    markers: [
      { Id: 1, name: "1", position: { lat: 16.466022, lng: 102.899313 } },
      { Id: 2, name: "2", position: { lat: 16.466022, lng: 102.898313 } },
      { Id: 3, name: "3", position: { lat: 16.465022, lng: 102.898313 } },
    ],
  }),
  created:{
    //ดึงข้อมูลจาก Database
  },
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
    ...mapGetters({
      province: "getProvince",
    }),
  },
  methods: {
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/show-area");
      }
    },
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },
    deletearea() {
      //ทำการเอา ID ของแปลงลบแปลงออกจากDatabase และกลับไปที่หน้า Show all area
      const vm = this;
      vm.$router.push("/show-all-area");
    },
    savedata(){
      //ทำการใส่ข้อมูลใหม่เข้าไปแทนที่ใน Database และกลับไปหน้า Showa area
      const vm = this;
      vm.$router.push("/show-area");
    },
    changefrommetertolatlong(width, long) {
      //เปลี่ยน กว้างยาว เป็น lat long
      var R = 6371e3; // Radius of the Earth in meter
      var rlat1 = this.path[2].lat * (Math.PI / 180); // Convert degrees to radians
      var rlat2 = this.path[1].lat * (Math.PI / 180); // Convert degrees to radians
      var difflat = rlat2 - rlat1; // Radian difference (latitudes)
      var difflon = (this.path[1].lng - this.path[2].lng) * (Math.PI / 180); // Radian difference (longitudes)

      var d =
        2 *
        R *
        Math.asin(
          Math.sqrt(
            Math.sin(difflat / 2) * Math.sin(difflat / 2) +
              Math.cos(rlat1) *
                Math.cos(rlat2) *
                Math.sin(difflon / 2) *
                Math.sin(difflon / 2)
          )
        );

      var rationlat = width / d;
      var rationlng = long / d;
      console.log(rationlat);
      console.log(rationlng);
      var newlat =
        this.path[1].lat + (this.path[0].lat - this.path[1].lat) * rationlat;
      var newlng =
        this.path[1].lng + (this.path[2].lng - this.path[1].lng) * rationlng;
      (this.newpath = [
        {
          lat: newlat, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
          lng: this.path[0].lng,
        },
        {
          lat: this.path[1].lat,
          lng: this.path[1].lng,
        },
        {
          lat: this.path[2].lat,
          lng: newlng, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
        },
      ]),
        (this.markers = [
          {
            Id: 1,
            name: "1",
            position: { lat: newlat, lng: this.path[0].lng },
          },
          {
            Id: 2,
            name: "2",
            position: { lat: this.path[1].lat, lng: this.path[1].lng },
          },
          {
            Id: 3,
            name: "3",
            position: { lat: this.path[2].lat, lng: newlng },
          },
        ]);
    },
    changepositionmap(newlat, newlng, wide, long) {
      this.mapcenter.lat = Number(newlat);
      this.mapcenter.lng = Number(newlng);
      (this.path = [
        {
          lat: Number(newlat) - 0.0009, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
          lng: Number(newlng),
        },
        {
          lat: Number(newlat),
          lng: Number(newlng),
        },
        {
          lat: Number(newlat),
          lng: Number(newlng) + 0.00094, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
        },
      ]),
        // Function calculation new distance
        this.changefrommetertolatlong(wide, long);
    },
  },
};
</script>
<style scoped>
#addpinbutton {
  color: #ffffff;
  background-color: #2643b6;
}
#backbutton {
  margin-right: 2vw;
}
#savebutton {
  background-color: #1ce227;
}
#map {
  width: 100%;
  height: 500px;
}
</style>