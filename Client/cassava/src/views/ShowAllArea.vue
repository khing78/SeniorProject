<template>
  <v-main class="show-all-area">
    <v-container fluid>
      <v-row>
        <v-col class="addFarm" cols="12" md="3" sm="4">
          <v-btn
            color="#1CE227"
            style="font-size: 18px"
            rounded
            @click="moveto('addarea')"
            >+ เพิ่มแปลงใหม่</v-btn
          >
        </v-col>
        <v-col cols="12" md="3" sm="2">
          <v-combobox
            v-model="selectprovince"
            :items="allprovince"
            label="จังหวัด"
            outlined
            dense
          ></v-combobox>
        </v-col>
        <v-col cols="12" md="3" sm="2">
          <v-text-field
            v-model="selectdistrict"
            label="อำเภอ"
            outlined
            dense
          ></v-text-field>
        </v-col>
        <v-col cols="12" md="3" sm="4">
          <v-btn
            id="filterprovincebutton"
            @click="selectfilter(selectprovince, selectdistrict)"
            style="font-size: 18px"
          >
            ค้นหา
          </v-btn>
          <v-btn
            id="showeverything"
            @click="showeveryarea()"
            style="font-size: 18px"
          >
            ทั้งหมด
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" md="8" sm="8">
          <gmap-map
            :center="mapcenter"
            :zoom="16"
            :options="{
              styles: hide,
            }"
            style="width: 100%; height: 500px"
            map-type-id="satellite"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in areashow"
              :position="m.position"
              :clickable="false"
              :draggable="false"
              @click="moveto('Accepted', m.id)"
            ></gmap-marker>
          </gmap-map>
          <!-- For Map -->
        </v-col>
        <v-col cols="12" md="4" sm="4">
          <v-simple-table fixed-header id="table">
            <template v-slot:default>
              <thead>
                <tr>
                  <th class="text-center" id="areaname" style="font-size: 20px">
                    ชื่อแปลง
                  </th>
                  <th class="text-center" id="areaname" style="font-size: 20px">
                    รายละเอียด
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr
                  class="elevation-1"
                  v-for="item in areashow"
                  :key="item.Id"
                  style="text: center"
                  @click="moveto(item.id)"
                >
                  <td style="font-size: 18px">{{ item.name }}</td>
                  <td style="font-size: 18px">
                    อ.{{ item.district }} จ.{{ item.province }}
                  </td>
                </tr>
              </tbody>
            </template>
          </v-simple-table>
          <v-col class="text-center">
            <v-btn @click="moveto('Accepted')" :disabled="acbuttonmode"
              >ตกลง</v-btn
            >
          </v-col>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
import { mapGetters } from "vuex";
import firebase from "firebase/app";
import axios from "axios";
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
    acbuttonmode: true,
    selectprovince: "",
    selectdistrict: "",
    selectid: 0,
    namearea: "",
    selectgrade: "",
    plantingDate: "",
    selectedpath: [],
    mapcenter: { lat: 16.4411261, lng: 102.8644933 },
    detailarea: [],
    areashow: [],
  }),
  mounted() {
    this.fetchdatafromdatabase();
  },
  created() {
    //ทุกครั้งที่เข้าหน้ามาให้โหลดข้อมูลแปลงทั้งหมดจาก Database ใหม่
    this.fetchdatafromdatabase();
  },
  computed: {
    ...mapGetters({
      allprovince: "getProvince",
      newidfarm: "getIdFarm",
      uid: "getUid",
    }),
  },
  methods: {
    async fetchdatafromdatabase() {
      await this.checkloginstate();
      await axios
        .get("http://143.198.205.220:8000/farms/")
        .then((response) => {
          var i = 0;
          this.detailarea = [];
          this.areashow = [];
          console.log(firebase.auth().currentUser + "response: ", response);
          while (i < response.data.length) {
            if (response.data[i].uid_store == this.uid) {
              var id = i;
              var idfarm = response.data[i].farm_id;
              var plantingDate = response.data[i].planting_date;
              var name = response.data[i].farm_name;
              var province = response.data[i].province;
              var district = response.data[i].district;
              var latitude = response.data[i].latitude;
              var longtitude = response.data[i].longtitude;
              var position = { lat: Number(latitude), lng: Number(longtitude) };
              var path = [
                { lat: Number(latitude), lng: Number(longtitude) },
                {
                  lat: Number(response.data[i].latitude_mark1),
                  lng: Number(response.data[i].longtitude_mark1),
                },
                {
                  lat: Number(response.data[i].latitude_mark2),
                  lng: Number(response.data[i].longtitude_mark2),
                },
                {
                  lat: Number(response.data[i].latitude_mark3),
                  lng: Number(response.data[i].longtitude_mark3),
                },
                {
                  lat: Number(response.data[i].latitude_mark4),
                  lng: Number(response.data[i].longtitude_mark4),
                },
              ];
              this.areashow.push({
                id,
                idfarm,
                plantingDate,
                name,
                province,
                district,
                position,
                path,
              });
              this.detailarea.push({
                id,
                idfarm,
                plantingDate,
                name,
                province,
                district,
                position,
                path,
              });
            }
            i++;
          }
          console.log("show" + this.areashow[4].id);
        })
        .catch((err) => {
          console.error(err);
        });
    },
    selectfilter(province, district) {
      //กรองเฉพาะที่เป็นจังหวัดนี้, อำเภอที่เลือก
      var i = 0;
      this.areashow = [];
      if (district != "") {
        while (i < this.detailarea.length) {
          if (
            province == this.detailarea[i].province &&
            district == this.detailarea[i].district
          ) {
            this.areashow.push(this.detailarea[i]);
          }
          i++;
        }
      } else {
        while (i < this.detailarea.length) {
          if (province == this.detailarea[i].province) {
            this.areashow.push(this.detailarea[i]);
          }
          i++;
        }
      }
    },
    showeveryarea() {
      this.areashow = this.detailarea;
    },
    checkloginstate() {
      const vm = this;
      firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
          axios.get("http://143.198.205.220:8000/uids/").then((response) => {
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
    afterselectedfarm() {},
    moveto(i) {
      const vm = this;
      if (i == "addarea") {
        vm.$router.push("/add-area");
      } else if (typeof i == "number") {
        console.log(i)
        var m = 0;
        while (m < this.detailarea.length) {
          if (i == this.detailarea[m].id) {
            this.acbuttonmode = false;
            this.selectid = this.detailarea[m].idfarm;
            this.mapcenter = this.detailarea[m].position;
            this.plantingDate = this.detailarea[m].plantingDate;
            this.namearea = this.detailarea[m].name;
            this.selectedpath = this.detailarea[m].path;
          }
          m++;
        }
      } else if (i == "Accepted") {
        //เอาข้อมูลID ของแปลงไปดึงแปลงใน Database
        vm.$store.commit({
          type: "setIdFarm",
          idfarm: this.selectid,
        });
        vm.$store.commit({
          type: "setDatePlant",
          dateplant: this.plantingDate,
        });
        vm.$store.commit({
          type: "setNameArea",
          namearea: this.namearea,
        });
        vm.$store.commit({
          type: "setPath",
          path: this.selectedpath,
        });
        vm.$store.commit({
          type: "setPosition",
          position: this.mapcenter,
        });
        vm.$router.push("/show-area");
      }
    },
  },
};
</script>
<style scoped>
@media screen and (min-width: 601px) {
  #table {
    height: 400px;
    padding-bottom: 20px;
  }
  .addFarm{
    width: fit-content;
  }
}

@media screen and (max-width: 600px) {
  #table {
    height: 200px;
    padding-bottom: 20px;
  }
}

#areaname {
  background-color: #ffa9a9;
}
#filterprovincebutton {
  margin-right: 1vw;
}

</style>