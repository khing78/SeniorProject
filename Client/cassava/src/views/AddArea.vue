<template>
  <div class="add-area">
    <v-container>
      <v-row>
        <!-- For Map -->
        <v-col cols="12" md="9">
          <gmap-map
          id="map"
            :center="mapcenter"
            :zoom="12"
            style="width: 100%; height: 500px"
            map-type-id="satellite"
          >
            <gmap-marker
              :key="index"
              v-for="(m, index) in markers"
              :position="m.position"
              :clickable="true"
              :draggable="true"
              @click="checkmap(m.position)"
            ></gmap-marker>
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
                v-model="date"
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
            <v-col cols="12" md="6" class="text-center">
              <v-btn id="addpinbutton" rounded @click="addpinfun()"> เพิ่มหมุด </v-btn>
            </v-col>
            <v-col cols="12" md="6" class="text-center">
              <v-btn rounded @click="deletedpinfun()"> ลบหมุด </v-btn>
            </v-col>
          </v-row>
          <v-row>
            <v-container fluid>
              <v-row>
                <v-col>
                  <v-combobox
                    v-model="selectstate"
                    :items="itemsstate"
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
          <v-col cols="12">
            <v-btn @click="changepositionmap(mapcenter.lat,mapcenter.lng)">New Center</v-btn>
          </v-col>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn rounded style="margin-end: 10px" @click="moveto('back')">ยกเลิก</v-btn>
          <v-btn color="#1CE227" rounded @click="moveto('save')">บันทึก</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data: () => ({
    date: new Date().toISOString().substr(0, 10),
    menu: false,
    modal: false,
    menu2: false,
    mapcenter: {lat: 16.4411261,lng: 102.8644933},
    positiona:{},
    markers: [],
    areaname: "",
    selectstate: "",
    itemsstate: ["ขอนแก่น", "เลย", "เชียงใหม่", "อุบลราชธานี"],
    selectdistrict: "",
    itemsdistrict: ["เมือง", "เวียงเก่า", "บ้านแฮด", "บ้านฝาง"],
  }),
  methods:{
    moveto(i){
      const vm = this
      if (i == "back"){
        vm.$router.push("/show-all-area")
      }
      else if (i == "save"){
        vm.$router.push("/show-all-area")
      }
    },
    changepositionmap(newlat,newlng){
      this.mapcenter.lat = Number(newlat)
      this.mapcenter.lng = Number(newlng)
    },
    checkmap(k){
      this.positiona = k
      console.log(k)
      
    },
    addpinfun (){
      const lenghtmarker = this.markers.length
      const po = this.mapcenter
      if (this.markers.length == 0){
        this.markers.push ({Id: lenghtmarker+1, name: (lenghtmarker+1).toString(), position:po })
      }
      else{
        this.markers.push ({Id: lenghtmarker+1, name: (lenghtmarker+1).toString(), position:po })
      }
    },
    deletedpinfun(){
      const lenghtmarker = this.markers.length
      this.markers.pop ({Id: lenghtmarker})
    },
  },
  created(){
    navigator.geolocation.getCurrentPosition((position) => {
        this.mapcenter = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      })
      if (this.mapcenter.lat == null){
        this.mapcenter.lat = 16.4411261
        this.mapcenter.lng = 102.8644933
      }
  }
  
};
</script>
<style scoped>
#addpinbutton {
  color: #ffffff;
  background-color: #2643b6;
  margin-bottom: 1vh;
}
</style>