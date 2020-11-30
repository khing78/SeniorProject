<template>
  <div class="edit-area">
    <v-container>
      <v-btn>ลบแปลง</v-btn>
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
            v-model="this.mapcenter.lat"
            hint="กรุณาใส่ละติจูด (หากมี)"
            label="ละติจูด (หากมี)"
          ></v-text-field>
          <v-text-field
            v-model="this.mapcenter.lng"
            hint="กรุณาใส่ลองจิจูด (หากมี)"
            label="ลองจิจูด (หากมี)"
          ></v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="text-right">
          <v-btn id="backbutton" rounded href="../show-area">ย้อนกลับ</v-btn>
          <v-btn id="savebutton" rounded href="../show-area">บันทึก</v-btn>
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
    mapcenter: {lat: 16.466022,lng: 102.898313},
    areaname: "สมชาย",
    selectstate: "ขอนแก่น",
    itemsstate: ["ขอนแก่น", "เลย", "เชียงใหม่", "อุบลราชธานี"],
    selectdistrict: "บ้านแฮด",
    itemsdistrict: ["เมือง", "เวียงเก่า", "บ้านแฮด", "บ้านฝาง"],
    markers: [
        { Id: 1, name: "1", position: { lat: 16.466022, lng: 102.898313 } },
        { Id: 2, name: "2", position: { lat: 16.466037 , lng: 102.899724 } },
        { Id: 3,  name: "3", position: { lat: 16.465616 , lng: 102.899717 }},
        { Id: 4, name: "4", position: { lat: 16.465644,  lng: 102.898275 } },
      ],
  }),
  computed: {
      computedDateFormatted () {
        return this.formatDate(this.date)
      },
    },
  methods:{
    formatDate(date) {
      if (!date) return null;
      const [year, month, day] = date.split("-");
      const newyear = parseInt(year)+543
      return `${day}/${month}/${newyear}`;
    },
    addpinfun (){
      const lenghtmarker = this.markers.length
      const po = this.mapcenter
      if (this.markers.length == 0){
        this.markers.push ({Id: lenghtmarker+1, name: (lenghtmarker+1).toString(), position:po })
      }
      else{
        this.markers.push ({Id: lenghtmarker+1, name: (lenghtmarker+1).toString(), position:this.mapcenter })
      }
    },
    deletedpinfun(){
      const lenghtmarker = this.markers.length
      this.markers.pop ({Id: lenghtmarker+1})
    },
  }
};
</script>
<style scoped>
#addpinbutton {
  color: #ffffff;
  background-color: #2643b6;
}
#backbutton{
  margin-right: 2vw;
}
#savebutton{
  background-color: #1CE227;
}
#map{
  width: 100%; 
  height: 500px
}
</style>