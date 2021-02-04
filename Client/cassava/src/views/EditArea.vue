<template>
  <v-main class="edit-area">
    <v-container>
      <v-row>
        <!-- For Map -->
        <v-col cols="12" md="9">
          <gmap-map
            id="map"
            :center="mapcenter"
            :zoom="18"
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
              :draggable="true"
              @dragend="
                changepositionmap(
                  $event.latLng.lat(),
                  $event.latLng.lng(),
                  mapcenter.wide,
                  mapcenter.long
                )
              "
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
                  <v-text-field
                    v-model="selectdistrict"
                    hint="กรุณาใส่อำเภอ"
                    label="อำเภอ"
                    outlined
                    dense
                  ></v-text-field>
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
          <v-btn rounded style="margin-end: 10px" @click="moveto('back')"
            >ยกเลิก</v-btn
          >
          <v-btn color="#1CE227" rounded @click="savedata()">บันทึก</v-btn>
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
    menu: false,
    modal: false,
    menu2: false,
    date: "2020-11-16",
    idfarm: "",
    mapcenter: { lat: 16.466022, lng: 102.898313, wide: 100, long: 100 },
    newpath: [
      { lat: 16.466022, lng: 102.898313 },
      { lat: 16.466022, lng: 102.899313 },
      { lat: 16.465022, lng: 102.899313 },
      { lat: 16.465022, lng: 102.898313 },
      { lat: 16.466022, lng: 102.898313 },
    ],
    path: [
      //ดึงข้อมูลจากDatabase มา
      { lat: 16.466022, lng: 102.898313 },
      { lat: 16.465122, lng: 102.898713 },
    ],
    areaname: "สมชาย",
    selectprovince: "ขอนแก่น",
    selectdistrict: "บ้านแฮด",
    markers: [
      { Id: 1, name: "1", position: { lat: 16.466022, lng: 102.898313 } },
    ],
  }),
  computed: {
    computedDateFormatted() {
      return this.formatDate(this.date);
    },
    ...mapGetters({
      newidfarm: "getIdFarm",
      province: "getProvince",
      selectedidfarm: "getIdFarm",
      uid: "getUid",
    }),
  },
  async created() {
    if (this.newidfarm == "") {
      this.$router.push("/show-all-area");
    }
    //ดึงข้อมูลจาก Database
    this.startshow();
  },
  methods: {
    startshow() {
      this.markers = [];
      axios
        .get("http://127.0.0.1:8000/farms/")
        .then((response) => {
          var i = 0;
          while (i < response.data.length) {
            if (response.data[i].farm_id == this.selectedidfarm) {
              var idfarm = response.data[i].farm_id;
              var plantingDate = response.data[i].planting_date;
              var name = response.data[i].farm_name;
              var province = response.data[i].province;
              var district = response.data[i].district;
              var latitude = response.data[i].latitude;
              var longtitude = response.data[i].longtitude;
              var width = response.data[i].farm_width;
              var long = response.data[i].farm_long;
              var position = { lat: Number(latitude), lng: Number(longtitude) };
              var path = [
                { lat: Number(latitude), lng: Number(longtitude) },
                {
                  lat: Number(response.data[i].latitude_mark3),
                  lng: Number(response.data[i].longtitude_mark3),
                },
              ];

              this.areaname = name;
              this.mapcenter = {
                lat: Number(latitude),
                lng: Number(longtitude),
                wide: width,
                long: long,
              };
              console.log(this.mapcenter);
              this.selectprovince = province;
              this.selectdistrict = district;
              this.path = path;
              this.date = plantingDate;
              this.idfarm = idfarm;
              this.markers.push(position);

              break;
            }
            i++;
          }
          this.changepositionmap(latitude, longtitude, width, long);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/show-area");
      }
    },
    formatDate(date) {
      console.log(date);
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      this.newdate = `${day}/${month}/${newyear}`;
      return `${day}/${month}/${newyear}`;
    },
    changeformatdateback(date) {
      const [day, month, year] = date.split("/");
      const newyear = parseInt(year) - 543;
      return `${newyear}-${month}/${day}`;
    },
    deletearea() {
      //ทำการเอา ID ของแปลงลบแปลงออกจากDatabase และกลับไปที่หน้า Show all area
      const vm = this;
      vm.$router.push("/show-all-area");
    },
    async savedata() {
      //ทำการใส่ข้อมูลใหม่เข้าไปแทนที่ใน Database และกลับไปหน้า Show area
      console.log(
        "http://127.0.0.1:8000/farms/" +
          this.selectedidfarm +
          "/" +
          " this is uid " +
          this.uid
      );
      await axios
        .put("http://127.0.0.1:8000/farms/" + this.selectedidfarm + "/", {
          uid_store: this.uid,
          farm_id: this.idfarm,
          farm_name: this.areaname,
          province: this.selectprovince,
          district: this.selectdistrict,
          planting_date: this.date,
          farm_width: this.mapcenter.wide,
          farm_long: this.mapcenter.long,
          latitude: this.newpath[0].lat,
          longtitude: this.newpath[0].lng,
          latitude_mark1: this.newpath[1].lat,
          longtitude_mark1: this.newpath[1].lng,
          latitude_mark2: this.newpath[2].lat,
          longtitude_mark2: this.newpath[2].lng,
          latitude_mark3: this.newpath[3].lat,
          longtitude_mark3: this.newpath[3].lng,
          latitude_mark4: this.newpath[4].lat,
          longtitude_mark4: this.newpath[4].lng,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      const vm = this;
      vm.$router.push("/show-area");
    },
    changefrommetertolatlong(width, long) {
      //เปลี่ยน กว้างยาว เป็น lat long
      var R = 6371e3; // Radius of the Earth in meter
      var rlat1 = this.path[1].lat * (Math.PI / 180); // Convert degrees to radians
      var rlat2 = this.path[0].lat * (Math.PI / 180); // Convert degrees to radians
      var difflat = rlat2 - rlat1; // Radian difference (latitudes)
      var difflon = (this.path[0].lng - this.path[1].lng) * (Math.PI / 180); // Radian difference (longitudes)

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
      var newlat =
        this.path[0].lat + (this.path[1].lat - this.path[0].lat) * rationlat;
      var newlng =
        this.path[0].lng + (this.path[1].lng - this.path[0].lng) * rationlng;
      (this.newpath = [
        {
          lat: this.path[0].lat,
          lng: this.path[0].lng,
        },
        {
          lat: newlat, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
          lng: this.path[0].lng,
        },
        {
          lat: newlat,
          lng: newlng,
        },
        {
          lat: this.path[0].lat,
          lng: newlng, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
        },
        {
          lat: this.path[0].lat,
          lng: this.path[0].lng,
        },
      ]),
        (this.markers = [
          {
            Id: 1,
            name: "1",
            position: { lat: this.path[0].lat, lng: this.path[0].lng },
          },
        ]);
    },
    changepositionmap(newlat, newlng, wide, long) {
      this.mapcenter.lat = Number(newlat);
      this.mapcenter.lng = Number(newlng);
      (this.path = [
        {
          lat: Number(newlat),
          lng: Number(newlng),
        },
        {
          lat: Number(newlat) - 0.0009, //เปลี่ยน 0.01 เป็นที่หลังคำนวณ
          lng: Number(newlng) + 0.00094,
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