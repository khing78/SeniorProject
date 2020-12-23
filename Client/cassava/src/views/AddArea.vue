<template>
  <v-main class="add-area">
    <v-container>
      <v-row>
        <!-- For Map -->
        <v-col cols="12" md="9">
          <gmap-map
            id="map"
            :center="mapcenter"
            :zoom="18"
            style="width: 100%; height: 500px"
            map-type-id="terrain"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="true"
              @click="checkmap(m.position)"
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
        <v-col cols="12" md="3">
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
                label="วัน/เดือน/ปี ที่ปลูก"
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
            label="ความกว้าง (เมตร)"
          ></v-text-field>
          <v-text-field
            v-model="mapcenter.long"
            hint="กรุณาใส่ความยาว"
            label="ความยาว (เมตร)"
          ></v-text-field>
          <v-col cols="12">
            <v-btn @click="changepositionmap(mapcenter.lat, mapcenter.lng ,mapcenter.wide,mapcenter.long)"
              >ตั้งจุดใหม่</v-btn
            >
          </v-col>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn rounded style="margin-end: 10px" @click="moveto('back')"
            >ยกเลิก</v-btn
          >
          <v-btn color="#1CE227" rounded @click="moveto('save')">บันทึก</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from "vuex"
export default {
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    mapcenter: { lat: 16.4411261, lng: 102.8644933, wide: 100, long: 100 },
    //lat = กว้าง lng = ยาว
    path: [],
    newpath:[],
    positiona: {},
    markers: [
      { Id: 1, name: "1", position: { lat: 16.466022, lng: 102.898313 } },
    ],
    areaname: "",
    selectprovince: "",
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เวียงเก่า", "บ้านแฮด", "บ้านฝาง"],
  }),
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
        vm.$router.push("/show-all-area");
      } else if (i == "save") {
        // ส่งข้อมูลไปที่ Database เพื่อเก็บข้อมูล
        vm.$router.push("/show-all-area");
      }
    },
    changefrommetertolatlong(width,long) {
      //เปลี่ยน กว้างยาว เป็น lat long
      var R = 6371e3; // Radius of the Earth in meter
      var rlat1 = this.path[2].lat * (Math.PI/180); // Convert degrees to radians
      var rlat2 = this.path[1].lat * (Math.PI/180); // Convert degrees to radians
      var difflat = rlat2-rlat1; // Radian difference (latitudes)
      var difflon = (this.path[1].lng - this.path[2].lng) * (Math.PI/180); // Radian difference (longitudes)

      var d = 2 * R * Math.asin(Math.sqrt(Math.sin(difflat/2)*Math.sin(difflat/2)+Math.cos(rlat1)*Math.cos(rlat2)*Math.sin(difflon/2)*Math.sin(difflon/2)));
      
      var rationlat = width/d
      var rationlng = long/d
      console.log(rationlat)
      console.log(rationlng)
      var newlat = this.path[1].lat + ((this.path[0].lat - this.path[1].lat)*rationlat)
      var newlng = this.path[1].lng + ((this.path[2].lng - this.path[1].lng)*rationlng)
      this.newpath = [
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
            lng: newlng //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
            ,
          },
        ],
        this.markers = [
          { Id: 1, name: "1", position: { lat: newlat, lng: this.path[0].lng } },
          { Id: 2, name: "2", position: { lat: this.path[1].lat, lng: this.path[1].lng } },
          { Id: 3, name: "3", position: { lat: this.path[2].lat, lng: newlng } },
        ]
        
    },
    formatDate(date) {
      if (!date) return null;

      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
    },
    changepositionmap(newlat, newlng, wide, long) {
      this.mapcenter.lat = Number(newlat);
      this.mapcenter.lng = Number(newlng);
      this.path = [
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
            lng: Number(newlng) + 0.00094 //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
            ,
          },
        ],
      // Function calculation new distance
      this.changefrommetertolatlong(wide,long)
    },
    checkmap(k) {
      this.positiona = k;
      console.log(k);
    },
  },
  created() {
    navigator.geolocation.getCurrentPosition((position) => {
      (this.mapcenter = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
        wide: 100,
        long: 100,
      }),
        (this.markers = [
          {
            Id: 1,
            name: "1",
            position: {
              lat: position.coords.latitude - 0.0009,
              lng: position.coords.longitude,
            },
          },
          {
            Id: 2,
            name: "2",
            position: {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            },
          },
          {
            Id: 3,
            name: "3",
            position: {
              lat: position.coords.latitude,
              lng: position.coords.longitude + 0.00094,
            },
          },
        ]),
        (this.path = [
          {
            lat: position.coords.latitude - 0.0009, // = 100 meter
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude + 0.00094, // = 100 meter
          },
        ]),
        (this.newpath = [
          {
            lat: position.coords.latitude - 0.0009, // = 100 meter
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude + 0.00094, // = 100 meter
          },
        ]),
        console.log(this.markers);
    });
    if (this.mapcenter.lat == null) {
      this.mapcenter.lat = 16.4411261;
      this.mapcenter.lng = 102.8644933;
    }
  },
};
</script>
<style scoped>
#addpinbutton {
  color: #ffffff;
  background-color: #2643b6;
  margin-bottom: 1vh;
}
</style>