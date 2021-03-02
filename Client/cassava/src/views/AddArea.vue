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
          <v-btn color="#1CE227" rounded @click="moveto('save'), addnewfarm()"
            >บันทึก</v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from "vuex";
import axios from "axios";
import firebase from "firebase/app";
import "firebase/auth";
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
    mapcenter: { lat: 16.466022, lng: 102.898313, wide: 100, long: 100 },
    //lat = กว้าง lng = ยาว
    path: [],
    newpath: [],
    positiona: {},
    markers: [
      { Id: 1, name: "1", position: { lat: 16.466022, lng: 102.898313 } },
    ],
    areaname: "",
    selectprovince: "",
    selectdistrict: "",
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
    async addnewfarm() {
      var user = firebase.auth().currentUser;
      console.log(user.uid + "  +  this lat ");
      console.log(this.newpath);
      await axios
        .post("http://188.166.246.244:6969/farms/", {
          uid_store: user.uid,
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
        .then((reponse) => {
          console.log(reponse);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    moveto(i) {
      const vm = this;
      if (i == "back") {
        vm.$router.push("/show-all-area");
      } else if (i == "save") {
        // ส่งข้อมูลไปที่ Database เพื่อเก็บข้อมูล
        vm.$router.push("/show-all-area");
      }
    },
    checkloginstate() {
      const vm = this;
      firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
          axios.get("http://188.166.246.244:6969/uids/").then((response) => {
            var i = 0;
            while (i < response.data.length) {
              if (response.data[i].uId == user.uid) {
                vm.$store.commit({
                  type: "setUserName",
                  username: response.data[i].username,
                });
                break;
              }
              i++;
            }
          });
          console.log(user.uid);
          vm.$store.commit({
            type: "setUid",
            uid: user.uid,
          });
        } else {
          vm.$router.push("/");
        }
      });
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
      console.log(rationlat);
      console.log(rationlng);
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
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year) + 543;
      return `${day}/${month}/${newyear}`;
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
    checkmap(k) {
      this.positiona = k;
      console.log(k);
    },
  },
  created() {
    this.checkloginstate();
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
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            },
          },
        ]),
        (this.path = [
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude - 0.0009,
            lng: position.coords.longitude + 0.00094,
          },
        ]),
        (this.newpath = [
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude - 0.0009, // = 100 meter
            lng: position.coords.longitude,
          },
          {
            lat: position.coords.latitude - 0.0009,
            lng: position.coords.longitude + 0.00094,
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude + 0.00094, // = 100 meter
          },
          {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          },
        ]),
        console.log(this.markers);
    });
    if (this.mapcenter.lat == null) {
      this.mapcenter.lat = 16.4411261;
      this.mapcenter.lng = 102.8644933;
      this.markers = [
        {
          Id: 1,
          name: "1",
          position: {
            lat: 16.4411261,
            lng: 102.8644933,
          },
        },
      ];
      this.path = [
        {
          lat: 16.466022,
          lng: 102.898313,
        },
        {
          lat: 16.466022 - 0.0009, // = 100 meter
          lng: 102.898313,
        },
        {
          lat: 16.466022 - 0.0009,
          lng: 102.898313 + 0.00094,
        },
        {
          lat: 16.466022,
          lng: 102.898313 + 0.00094, // = 100 meter
        },
        {
          lat: 16.466022,
          lng: 102.898313,
        },
      ];
      this.newpath = [
        {
          lat: 16.466022,
          lng: 102.898313,
        },
        {
          lat: 16.466022 - 0.0009, // = 100 meter
          lng: 102.898313,
        },
        {
          lat: 16.466022 - 0.0009,
          lng: 102.898313 + 0.00094,
        },
        {
          lat: 16.466022,
          lng: 102.898313 + 0.00094, // = 100 meter
        },
        {
          lat: 16.466022,
          lng: 102.898313,
        },
      ];
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
#provinceselecter {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}
</style>